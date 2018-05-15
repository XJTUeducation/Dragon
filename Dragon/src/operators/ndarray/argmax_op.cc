#include "operators/ndarray/argmax_op.h"
#include "utils/op_kernel.h"

namespace dragon {

template <class Context> template <typename T>
void ArgmaxOp<Context>::RunWithType() {
    if (top_k != 1) {
        //  it's difficult to implement device code when top_k > 1
        auto* Xdata = Input(0).template data<T, CPUContext>();
        auto* Ydata = Output(0)->template mutable_data<T, CPUContext>();
        kernel::Argmax<T, CPUContext>(count, axis_dim, inner_dim, top_k, Xdata, Ydata);
    } else {
        auto* Xdata = Input(0).template data<T, Context>();
        auto* Ydata = Output(0)->template mutable_data<T, Context>();
        kernel::Argmax<T, Context>(count, axis_dim, inner_dim, top_k, Xdata, Ydata);
    }
}

template <class Context>
void ArgmaxOp<Context>::RunOnDevice() {
    if (axis != -1) {
        axis_dim = Input(0).dim(axis);
        inner_dim = Input(0).count(axis) / axis_dim;
    } else {
        axis_dim = Input(0).count();
        inner_dim = 1;
    }
    count = Input(0).count() / axis_dim;
    vector<TIndex> dims = Input(0).dims();
    if (!keep_dims) {
        if (axis != -1) {
            if (top_k == 1) dims.erase(dims.begin() + axis);
            else dims[axis] = top_k;
        } else {
            dims = vector<TIndex>(1, top_k);
        }
    } else {
        if (axis == -1) dims = vector<TIndex>(Input(0).ndim(), 1);
        dims[axis] = top_k;
    }
    Output(0)->Reshape(dims);

    if (XIsType(Input(0), float)) RunWithType<float>();
    else LOG(FATAL) << DTypeHelper(Input(0), { "float32" });
}

DEPLOY_CPU(Argmax);
#ifdef WITH_CUDA
DEPLOY_CUDA(Argmax);
#endif
OPERATOR_SCHEMA(Argmax).NumInputs(1).NumOutputs(1);

NO_GRADIENT(Argmax);

}    // namespace dragon