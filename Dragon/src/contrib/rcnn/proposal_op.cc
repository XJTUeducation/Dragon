#include "core/workspace.h"
#include "utils/op_kernel.h"
#include "contrib/rcnn/proposal_op.h"
#include "contrib/rcnn/bbox_utils.h"

namespace dragon {

template <class Context> template <typename T>
void ProposalOp<Context>::RunWithType(
    const T*                scores,
    const T*                bbox_deltas) {
    using BT = float;
    TIndex total_rois = 0;
    auto* im_info = Input(-1).template data<BT, CPUContext>();
    auto* Ydata = Output(0)->template mutable_data<BT, CPUContext>();
    for (int n = 0; n < num_images; ++n) {
        const BT im_height = im_info[0];
        const BT im_width = im_info[1];
        const BT scale = im_info[2];
        const BT min_box_h = min_size * scale;
        const BT min_box_w = min_size * scale;
        int num_rois = 0;
        if (strides.size() == 1) {
            // Case 1: single stride (Faster R-CNN)
            const TIndex feat_height = Input(0).dim(2);
            const TIndex feat_width = Input(0).dim(3);
            const TIndex K = feat_height * feat_width;
            const TIndex A = ratios.size() * scales.size();
            const TIndex num_proposals = K * A;
            const TIndex pre_nms_topn = std::min(num_proposals, pre_nms_top_n);
            anchors_.Reshape({ A, 4 });
            proposals_.Reshape({ num_proposals, 5 });

            rcnn::GenerateAnchors<BT>(strides[0],
                (int)ratios.size(), (int)scales.size(),
                    &ratios[0], &scales[0],
                        anchors_.template mutable_data<BT, CPUContext>());

            rcnn::GenerateProposals<BT, Context>(
                A, feat_height, feat_width, strides[0],
                    im_height, im_width, min_box_h, min_box_w,
                        scores, bbox_deltas,
                anchors_.template mutable_data<BT, Context>(),
                proposals_.template mutable_data<BT, Context>(), ctx());

            rcnn::SortProposals(0, num_proposals - 1, pre_nms_top_n,
                proposals_.template mutable_data<BT, CPUContext>());

            rcnn::ApplyNMS<BT, Context>(
                pre_nms_topn, post_nms_top_n, nms_thresh,
                    proposals_.template mutable_data<BT, Context>(),
                        roi_indices_.template mutable_data<int, CPUContext>(),
                            num_rois, ctx());

            rcnn::RetrieveRoIs<BT>(num_rois, n,
                proposals_.template mutable_data<BT, CPUContext>(),
                    roi_indices_.template mutable_data<int, CPUContext>(), Ydata);

        } else if (strides.size() > 1) {
            // Case 2: multiple stride (FPN / Mask R-CNN / RetinaNet)
            CHECK_EQ(strides.size(), (int)InputSize() - 3)
                << "\nGiven " << strides.size() << " strides and "
                << InputSize() - 3 << " feature inputs";
            CHECK_EQ(strides.size(), scales.size())
                << "\nGiven " << strides.size() << " strides and "
                << scales.size() << " scales";
            // CLS_probs: [1, total_proposals]
            // BBOX_deltas: [1, 4, total_proposals]
            TIndex total_proposals = Input(-3).dim(1), acc_proposals = 0;
            const TIndex pre_nms_topn = std::min(total_proposals, pre_nms_top_n);;
            proposals_.Reshape({ total_proposals, 5 });
            auto* proposals = proposals_.template mutable_data<BT, CPUContext>();

            for (int i = 0; i < strides.size(); i++) {
                const TIndex feat_height = Input(i).dim(2);
                const TIndex feat_width = Input(i).dim(3);
                const TIndex K = feat_height * feat_width;
                const TIndex A = ratios.size();
                const TIndex num_proposals = K * A;
                anchors_.Reshape({ A, 4 });

                rcnn::GenerateAnchors<BT>(strides[i],
                    (int)ratios.size(), 1, &ratios[0], &scales[0],
                        anchors_.template mutable_data<BT, CPUContext>());

                rcnn::GenerateGridAnchors<BT>(
                    A, feat_height, feat_width, strides[i],
                        anchors_.template mutable_data<BT, CPUContext>(),
                            proposals);

                acc_proposals += num_proposals;
                proposals += (num_proposals * 5);
            }

            CHECK_EQ(acc_proposals, total_proposals)
                << "\nExcepted " << total_proposals << " proposals from the network, "
                << "but generated " << acc_proposals << " proposals.";

            rcnn::GenerateProposals_v2<float, Context>(total_proposals,
                im_height, im_width, min_box_h, min_box_w,
                    scores, bbox_deltas,
                proposals_.template mutable_data<BT, Context>(), ctx());

            rcnn::SortProposals(0, total_proposals - 1, pre_nms_top_n,
                proposals_.template mutable_data<BT, CPUContext>());

            rcnn::ApplyNMS<BT, Context>(pre_nms_topn, post_nms_top_n, nms_thresh,
                proposals_.template mutable_data<BT, Context>(),
                    roi_indices_.template mutable_data<int, CPUContext>(),
                        num_rois, ctx());

            rcnn::RetrieveRoIs<BT>(num_rois, n,
                proposals_.template mutable_data<BT, CPUContext>(),
                    roi_indices_.template mutable_data<int, CPUContext>(), Ydata);

        } else {
            LOG(FATAL) << "There should be given at least one stride for proposals.";
        }
        total_rois += num_rois;
        Ydata += (num_rois * 5);
        im_info += Input(-1).dim(1);
    }
    Output(0)->Reshape(vector<TIndex>({ total_rois, 5 }));

    // Distribute rois into K bins
    if (OutputSize() > 1) {
        CHECK_EQ(max_level - min_level + 1, (int)OutputSize())
            << "\nExcepted " << OutputSize() << " outputs for levels between "
            << "[" << min_level << ", " << max_level << "].";
        vector< vector<TIndex> > roi_bins(OutputSize(), vector<TIndex>());
        vector<BT*> outputs;
        Tensor collective_rois;
        collective_rois.ReshapeLike(*Output(0));
        auto* rois = collective_rois.template mutable_data<BT, CPUContext>();

        ctx()->template Copy<BT, CPUContext, CPUContext>(
            collective_rois.count(), rois,
                Output(0)->template data<BT, CPUContext>());

        rcnn::CollectRoIs<BT>(total_rois,
            min_level, max_level,
                canonical_level, canonical_scale,
                    rois, roi_bins);

        for (int i = 0; i < OutputSize(); i++) {
            Output(i)->Reshape({ std::max((int)roi_bins[i].size(), 1), 5 });
            outputs.push_back(Output(i)->template mutable_data<BT, CPUContext>());
        }
        rcnn::DistributeRoIs(roi_bins, rois, outputs);
    }
}

template <class Context>
void ProposalOp<Context>::RunOnDevice() {
    ctx()->set_stream_id(0);  // Enforce SyncStream

    num_images = Input(0).dim(0);
    CHECK_EQ(Input(-1).dim(0), num_images)
        << "\nExcepted " << num_images << " groups image info, "
        << "but got " << Input(-1).dim(0) << ".";
    roi_indices_.Reshape({ post_nms_top_n });
    Output(0)->Reshape({ num_images * post_nms_top_n, 5 });

    if (XIsType(Input(-3), float)) {
        auto* scores = Input(-3).template data<float, Context>();
        auto* bbox_deltas = Input(-2).template data<float, Context>();
        RunWithType<float>(scores, bbox_deltas);
    } else if (XIsType(Input(-3), float16)) {
        auto* scores = Input(-3).template data<float16, Context>();
        auto* bbox_deltas = Input(-2).template data<float16, Context>();
        // Convert logits to float32
        auto WSdata = ws()->template caches<float, Context>({
           Input(-3).count(), Input(-2).count() });
        kernel::TypeA2B<float16, float, Context>(
            Input(-3).count(), scores, WSdata[0], ctx());
        kernel::TypeA2B<float16, float, Context>(
            Input(-2).count(), bbox_deltas, WSdata[1], ctx());
        RunWithType<float>(WSdata[0], WSdata[1]);
    } else LOG(FATAL) << DTypeHelper(Input(0), { "float32", "float16" });
}

DEPLOY_CPU(Proposal);
#ifdef WITH_CUDA
DEPLOY_CUDA(Proposal);
#endif

OPERATOR_SCHEMA(Proposal).NumInputs(3, INT_MAX).NumOutputs(1, INT_MAX);

}  // namespace dragon