// ------------------------------------------------------------
// Copyright (c) 2017-present, SeetaTech, Co.,Ltd.
//
// Licensed under the BSD 2-Clause License.
// You should have received a copy of the BSD 2-Clause License
// along with the software. If not, See,
//
//      <https://opensource.org/licenses/BSD-2-Clause>
//
// -------------------------------------------------------------

#ifndef DRAGON_OPERATORS_NORM_L2_NORM_H_
#define DRAGON_OPERATORS_NORM_L2_NORM_H_

#include "core/operator.h"

namespace dragon {

template <class Context>
class L2NormOp final : public Operator<Context> {
 public:
    L2NormOp(const OperatorDef& op_def, Workspace* ws)
        : Operator<Context>(op_def, ws),
          axis(OperatorBase::GetSingleArg<int>("axis", 0)),
          num_axes(OperatorBase::GetSingleArg<int>("num_axes", -1)),
          eps(OperatorBase::GetSingleArg<float>("eps", 1e-5f)),
          mode(OperatorBase::GetSingleArg<string>("mode", "SUM")) {}
    USE_OPERATOR_FUNCTIONS(Context);

    void RunOnDevice() override;
    template <typename T> void RunWithType();

 protected:
    float eps;
    TIndex axis, num_axes, end_axis;
    string mode;
    bool across_inner;
    Tensor* norm, *buffer, *multiplier;
    TIndex outer_dim, dim, inner_dim, spatial_dim;
};

template <class Context>
class L2NormGradientOp final : public Operator<Context> {
 public:
    L2NormGradientOp(const OperatorDef& op_def, Workspace* ws)
        : Operator<Context>(op_def, ws),
          axis(OperatorBase::GetSingleArg<int>("axis", 0)),
          num_axes(OperatorBase::GetSingleArg<int>("num_axes", -1)),
          mode(OperatorBase::GetSingleArg<string>("mode", "SUM")) {}
    USE_OPERATOR_FUNCTIONS(Context);

    void RunOnDevice() override;
    template <typename T> void RunWithType();

 protected:
    TIndex axis, num_axes, end_axis;
    string mode;
    bool across_inner;
    Tensor* norm, *multiplier, *buffer, *buffer_inner;
    TIndex outer_dim, dim, inner_dim;
};

}    // namespace dragon

#endif    // DRAGON_OPERATORS_NORM_L2_NORM_H_