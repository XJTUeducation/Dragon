/*!
 * Copyright (c) 2017-present, SeetaTech, Co.,Ltd.
 *
 * Licensed under the BSD 2-Clause License.
 * You should have received a copy of the BSD 2-Clause License
 * along with the software. If not, See,
 *
 *      <https://opensource.org/licenses/BSD-2-Clause>
 *
 * ------------------------------------------------------------
 */

#ifndef DRAGON_OPERATORS_MPI_BASE_MPI_OP_H_
#define DRAGON_OPERATORS_MPI_BASE_MPI_OP_H_

#ifdef WITH_MPI

#include "core/operator.h"
#include "mpi/mpi.h"

namespace dragon {

template <class Context>
class ModelMPIBase : public Operator<Context> {
 public:
    ModelMPIBase(const OperatorDef& def, Workspace* ws)
        : Operator<Context>(def, ws),
          comm((MPI_Comm)OperatorBase::Arg<int64_t>("comm", 0)),
          group((MPI_Group)OperatorBase::Arg<int64_t>("group", 0)),
          dtype(OperatorBase::Arg<string>("dtype", "FLOAT32")) {

        if (comm == MPI_COMM_NULL) return;
        MPI_Comm_size(MPI_COMM_WORLD, &world_size);
        MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);
        MPI_Comm_size(comm, &comm_size);
        MPI_Comm_rank(comm, &comm_rank);

        MPI_Group world_group;
        MPI_Comm_group(MPI_COMM_WORLD, &world_group);
        int world_root = OperatorBase::Arg<int>("root", 0);
        MPI_Group_translate_ranks(world_group, 1, &world_root, group, &comm_root);

        CHECK(comm_root != MPI_UNDEFINED) << "MPI root is not included in layer group.";
    }

    MPI_Datatype mpi_dtype() {
        if (dtype == "FLOAT32") return MPI_FLOAT;
        else LOG(FATAL) << "Unsupported input type: " << dtype;
        return MPI_DATATYPE_NULL;
    }

 public:
    MPI_Comm comm;
    MPI_Group group;
    int comm_size, comm_rank, comm_root;
    int world_size, world_rank;
    string dtype;
};

#define USE_MODEL_MPI_FUNCTIONS \
    using ModelMPIBase<Context>::comm; \
    using ModelMPIBase<Context>::mpi_dtype; \
    using ModelMPIBase<Context>::comm_size; \
    using ModelMPIBase<Context>::comm_rank; \
    using ModelMPIBase<Context>::comm_root; \
    using ModelMPIBase<Context>::dtype

}  // namespace dragon

#endif  // WITH_MPI

#endif  // DRAGON_OPERATORS_MPI_BASE_MPI_OP_H_