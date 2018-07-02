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

#ifndef DRAGON_OPERATORS_LOSS_SPARSE_SOFTMAX_FOCAL_LOSS_OP_H_
#define DRAGON_OPERATORS_LOSS_SPARSE_SOFTMAX_FOCAL_LOSS_OP_H_

#include "operators/loss/sparse_softmax_cross_entropy_op.h"

namespace dragon {

template <class Context>
class SparseSoftmaxFocalLossOp final : public SparseSoftmaxCrossEntropyOp<Context> {
 public:
    SparseSoftmaxFocalLossOp(const OperatorDef& def, Workspace* ws)
        : SparseSoftmaxCrossEntropyOp<Context>(def, ws),
           axis(OperatorBase::Arg<int>("axis", 1)),
           normalization(OperatorBase::Arg<string>(
               "normalization", "VALID")),
           alpha(OperatorBase::Arg<float>("alpha", 0.5)),
           gamma(OperatorBase::Arg<float>("gamma", 0.0)),
           neg_id(OperatorBase::Arg<int>("neg_id", -1)) {
        pos_alpha = alpha * 2.0;
        neg_alpha = (1 - alpha) * 2.0;
    }
    USE_OPERATOR_FUNCTIONS;

    void RunOnDevice() override;
    template <typename T> void RunWithType();

 protected:
    float alpha, gamma;
    int neg_id;
    float pos_alpha, neg_alpha;
    TIndex axis, outer_dim, inner_dim;
    Tensor* scale;
    string normalization;
};

template <class Context>
class SparseSoftmaxFocalLossGradientOp final : public SparseSoftmaxCrossEntropyGradientOp<Context> {
 public:
    SparseSoftmaxFocalLossGradientOp(const OperatorDef& def, Workspace* ws)
         : SparseSoftmaxCrossEntropyGradientOp<Context>(def, ws),
           axis(OperatorBase::Arg<int>("axis", 1)),
           normalization(OperatorBase::Arg<string>(
               "normalization", "VALID")),
           gamma(OperatorBase::Arg<float>("gamma", 0.0)),
           eps(OperatorBase::Arg<float>("eps", float(1e-10))),
           neg_id(OperatorBase::Arg<int>("neg_id", -1)) {}
    USE_OPERATOR_FUNCTIONS;

    void RunOnDevice() override;
    template <typename T> void RunWithType();

 protected:
    float gamma, eps;
    int neg_id;
    TIndex axis, outer_dim, inner_dim;
    Tensor* scale;
    string normalization;
};

}    // namespace dragon

#endif    // DRAGON_OPERATORS_LOSS_SPARSE_SOFTMAX_FOCAL_LOSS_OP_H_