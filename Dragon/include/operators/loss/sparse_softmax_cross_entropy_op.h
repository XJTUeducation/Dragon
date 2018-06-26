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

#ifndef DRAGON_OPERATORS_LOSS_SPARSE_SOFTMAX_CROSS_ENTROPY_OP_H_
#define DRAGON_OPERATORS_LOSS_SPARSE_SOFTMAX_CROSS_ENTROPY_OP_H_

#include "core/operator.h"

namespace dragon {

template <class Context>
class SparseSoftmaxCrossEntropyOp : public Operator<Context> {
 public:
    SparseSoftmaxCrossEntropyOp(const OperatorDef& op_def, Workspace* ws)
        : Operator<Context>(op_def, ws),
          axis(OperatorBase::GetSingleArg<int>("axis", 1)),
          normalization(OperatorBase::GetSingleArg<string>("normalization", "VALID")) {
        vector<int> args = OperatorBase::GetRepeatedArg<int>("ignore_labels");
        if (args.size()) {
            ignore.Reshape(vector<TIndex>(1, args.size()));
            int* ignore_data = ignore.mutable_data<int, CPUContext>();
            for (int i = 0; i < args.size(); i++) ignore_data[i] = args[i];
        }
    }
    USE_OPERATOR_FUNCTIONS;

    void SoftmaxRun();
    void SoftmaxRunFP16();

    void RunOnDevice() override;
    template <typename Tx, typename Ty> void RunWithType();

 protected:
    TIndex axis, outer_dim, inner_dim;
    Tensor ignore, valid, losses;
    Tensor* prob;
    unique_ptr<OperatorBase> softmax_op;
    string normalization;
};

template <class Context>
class SparseSoftmaxCrossEntropyGradientOp : public Operator<Context> {
 public:
    SparseSoftmaxCrossEntropyGradientOp(const OperatorDef& op_def, Workspace* ws)
        : Operator<Context>(op_def, ws),
          axis(OperatorBase::GetSingleArg<int>("axis", 1)),
          normalization(OperatorBase::GetSingleArg<string>("normalization", "VALID")) {
        vector<int> args = OperatorBase::GetRepeatedArg<int>("ignore_labels");
        if (args.size()) {
            ignore.Reshape(vector<TIndex>(1, args.size()));
            int* ignore_data = ignore.mutable_data<int, CPUContext>();
            for (int i = 0; i < args.size(); i++) ignore_data[i] = args[i];
        }
    }
    USE_OPERATOR_FUNCTIONS;

    void RunOnDevice() override;
    template <typename Tx, typename Ty> void RunWithType();

 protected:
    TIndex axis, outer_dim, inner_dim;
    Tensor ignore, valid;
    Tensor* prob;
    string normalization;
};

}    // namespace dragon

#endif    // DRAGON_OPERATORS_LOSS_SPARSE_SOFTMAX_CROSS_ENTROPY_OP_H_