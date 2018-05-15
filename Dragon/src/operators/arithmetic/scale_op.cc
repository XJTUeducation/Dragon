#include "operators/arithmetic/scale_op.h"
#include "core/workspace.h"
#include "utils/filler.h"
#include "utils/op_kernel.h"

namespace dragon {

template <class Context> template <typename T>
void ScaleOp<Context>::RunWithType() {
    start_axis = axis;
    if (start_axis < 0) start_axis += (int)Input(0).ndim();
    if (num_axes == -1) num_axes = (int)Input(0).ndim() - start_axis;
    else if (num_axes == 0) num_axes = 1;

    CHECK_LT(start_axis, (int)Input(0).ndim());
    CHECK_LE(start_axis + num_axes, (int)Input(0).ndim());

    const vector<TIndex>::const_iterator& dim_start = Input(0).dims().begin() + start_axis;
    const vector<TIndex>::const_iterator& dim_end = dim_start + num_axes;
    vector<TIndex> param_dims(dim_start, dim_end);

    TENSOR_FILL(Input(1), param_dims);
    if (InputSize() > 2) {
        TENSOR_FILL(Input(2), param_dims);
        inner_dim = Input(0).count(start_axis + num_axes);
        INIT_MULTIPLIER(bias_multiplier, inner_dim);
    }

    if (InputSize() > 2) {
        kernel::Scale<T, Context>(start_axis, &Input(0), &Input(1),
                                        &Input(2), bias_multiplier,
                                                        Output(0));
    } else {
        kernel::Scale<T, Context>(start_axis, &Input(0), &Input(1),
                                                  nullptr, nullptr,
                                                        Output(0));
    }
}

template <class Context>
void ScaleOp<Context>::RunOnDevice() {
    Output(0)->ReshapeLike(Input(0));

    if (XIsType(Input(0), float)) RunWithType<float>();
    else if (XIsType(Input(0), float16)) RunWithType<float16>();
    else LOG(FATAL) << DTypeHelper(Input(0), { "float32", "float16" });
}

DEPLOY_CPU(Scale);
#ifdef WITH_CUDA
DEPLOY_CUDA(Scale);
#endif
OPERATOR_SCHEMA(Scale).NumInputs(2, 3).NumOutputs(1);

template <class Context> template <typename T>
void ScaleGradientOp<Context>::BiasRunWithType() {
    Output(2)->ReshapeLike(Input(1));
    INIT_MULTIPLIER(bias_multiplier, inner_dim);
    auto* BMul_data = this->bias_multiplier->template data<T, Context>();
    auto* dYdata = Input(-1).template data<T, Context>();
    auto* dBias = Output(2)->template mutable_data<T, Context>();

    for (int n = 0; n < outer_dim; n++) {
        math::Gemv<T, Context>(CblasNoTrans, scale_dim, inner_dim,
                                                              1.0, 
                                                dYdata, BMul_data, 
                                                              1.0, 
                                                           dBias);
        dYdata += dim;
    }
}

template <class Context> template <typename T>
void ScaleGradientOp<Context>::ScaleRunWithType() {
    Output(0)->ReshapeLike(Input(0));
    Output(1)->ReshapeLike(Input(1));
    INIT_MULTIPLIER(sum_multiplier, sum_dim);
    sum_result.Reshape(vector<TIndex>(1, outer_dim * scale_dim));
    bool is_eltwise = (Input(0).count() == Input(1).count());
    auto* dYdata = Input(-1).template data<T, Context>();
    auto* Xdata = Input(0).template data<T, Context>();
    auto* dScale = Output(1)->template mutable_data<T, Context>();
    auto* dXdata = Output(0)->template mutable_data<T, Context>();
    auto* tmp_data = (is_eltwise ? dScale : dXdata);
    auto* SMul_data = sum_multiplier->template mutable_data<T, Context>();

    math::Mul<T, Context>(Output(0)->count(), dYdata, Xdata, tmp_data);

    if (!is_eltwise) {
        T* SRes_data = nullptr;
        if (inner_dim == 1) {
            SRes_data = tmp_data;
        } else if (sum_result.count() == 1) {    //  handle inner only
            dScale = Output(1)->template mutable_data<T, CPUContext>();
            T result = math::Dot<T, Context>(inner_dim, tmp_data, SMul_data);
            *dScale += result;
        } else {
            SRes_data = (outer_dim == 1) ?  //  handle scale only
                dScale : sum_result.template mutable_data<T, Context>();
            math::Gemv<T, Context>(CblasNoTrans, sum_result.count(), inner_dim,
                                                                           1.0,
                                                           tmp_data, SMul_data,
                                               SRes_data == dScale ? 1.0 : 0.0,
                                                                    SRes_data);
        } 
        if (outer_dim != 1) {
            if (scale_dim == 1) {    //  handle outer only
                T result = math::Dot<T, Context>(outer_dim, SMul_data, SRes_data);
                *dScale += result;
            } else {
                math::Gemv<T, Context>(CblasTrans, outer_dim, scale_dim,
                                                                    1.0,
                                                   SRes_data, SMul_data,
                                                                    1.0,
                                                                dScale);
            }
        }
    }
}

template <class Context> template <typename T>
void ScaleGradientOp<Context>::RunWithType() {
    Output(0)->ReshapeLike(Input(0));

    kernel::ScaleGrad<T, Context>(start_axis,
           &Input(-1), &Input(1), Output(0));
}

template <class Context>
void ScaleGradientOp<Context>::RunOnDevice() {
    start_axis = axis;
    if (start_axis < 0) start_axis += (int)Input(0).ndim();
    if (num_axes == -1) num_axes = (int)Input(0).ndim() - start_axis;
    else if (num_axes == 0) num_axes = 1;

    CHECK_LT(start_axis, (int)Input(0).ndim());
    CHECK_LE(start_axis + num_axes, (int)Input(0).ndim());

    outer_dim = Input(0).count(0, start_axis);
    inner_dim = Input(0).count(start_axis + num_axes);
    scale_dim = Input(1).count();
    sum_dim = std::max(outer_dim, inner_dim);
    dim = scale_dim * inner_dim;

    if (XIsType(Input(0), float)) {
        if (Output(2)->name() != "ignore") BiasRunWithType<float>();
        if (Output(1)->name() != "ignore") ScaleRunWithType<float>();
        if (Output(0)->name() != "ignore") RunWithType<float>();  
    } else {
        LOG(FATAL) << DTypeHelper(Input(0), { "float32" });
    }
}

DEPLOY_CPU(ScaleGradient);
#ifdef WITH_CUDA
DEPLOY_CUDA(ScaleGradient);
#endif
OPERATOR_SCHEMA(ScaleGradient).NumInputs(3).NumOutputs(3);

class GetScaleGradient final : public GradientMakerBase {
 public:
    GRADIENT_MAKER_CTOR(GetScaleGradient);
    vector<OperatorDef> MakeDefs() override {
        return SingleDef(def.type() + "Gradient", "",
            vector<string> {I(0), I(1), GO(0)},
            vector<string> {GI(0), GI(1), GI(2)});
    }
};
REGISTER_GRADIENT(Scale, GetScaleGradient);

}    // namespace dragon