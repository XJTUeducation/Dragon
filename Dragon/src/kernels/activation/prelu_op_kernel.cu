#ifdef WITH_CUDA

#include "core/context_cuda.h"
#include "utils/op_kernel.h"
#include "utils/math_functions.h"

namespace dragon {

namespace kernel {

/*! PRelu <T = float32, Device = CUDA> */

template <typename T>
__global__ void _PRelu(
    const int               count,
    const int               channels,
    const int               dim,
    const T*                x,
    const T*                w,
    T*                      y) {
    CUDA_1D_KERNEL_LOOP(idx, count) {
        y[idx] = (x[idx] > 0) * x[idx] +
            (x[idx] < 0) * x[idx] * w[0];
    }
}

template <typename T>
__global__ void _PReluNCHW(
    const int               count,
    const int               channels,
    const int               dim,
    const T*                x,
    const T*                w,
    T*                      y) {
    CUDA_1D_KERNEL_LOOP(idx, count) {
        const int c = (idx / dim) % channels;
        y[idx] = (x[idx] > 0) * x[idx] +
            (x[idx] < 0) * x[idx] * w[c];
    }
}

template <typename T>
__global__ void _PReluNHWC(
    const int               count,
    const int               channels,
    const int               dim,
    const T*                x,
    const T*                w,
    T*                      y) {
    CUDA_1D_KERNEL_LOOP(idx, count) {
        const int c = idx % channels;
        y[idx] = (x[idx] > 0) * x[idx] +
            (x[idx] < 0) * x[idx] * w[c];
    }
}

template<> void PRelu<float, CUDAContext>(
    const int               count,
    const int               channels,
    const int               dim,
    const bool              channel_shared,
    const string&           data_format,
    const float*            x,
    const float*            w,
    float*                  y,
    CUDAContext*            ctx) {
    if (channel_shared) {
        _PRelu<float> 
            << < CUDA_BLOCKS(count), CUDA_THREADS,
                 0, ctx->cuda_stream() >> >
            (count, channels, dim, x, w, y);
    } else {
        if (data_format == "NCHW") {
            _PReluNCHW<float>
                << < CUDA_BLOCKS(count), CUDA_THREADS,
                     0, ctx->cuda_stream() >> >
                (count, channels, dim, x, w, y);
        } else if (data_format == "NHWC") {
            _PReluNHWC<float>
                << < CUDA_BLOCKS(count), CUDA_THREADS,
                     0, ctx->cuda_stream() >> >
                (count, channels, dim, x, w, y);
        } else LOG(FATAL) << "Unknown data format: " << data_format;
    }
}

/*! PReluGrad <T = float32, Device = CUDA> */

template <typename T>
__global__ void _PReluGrad(
    const int               count,
    const int               channels,
    const int               dim,
    const T*                dy,
    const T*                x,
    const T*                w,
    T*                      dx) {
    CUDA_1D_KERNEL_LOOP(idx, count) {
        dx[idx] = dy[idx] * (
            (x[idx] > 0) + (x[idx] <= 0) * w[0]
        );
    }
}

template <typename T>
__global__ void _PReluGradNCHW(
    const int               count,
    const int               channels,
    const int               dim,
    const T*                dy,
    const T*                x,
    const T*                w,
    T*                      dx) {
    CUDA_1D_KERNEL_LOOP(idx, count) {
        const int c = (idx / dim) % channels;
        dx[idx] = dy[idx] * (
            (x[idx] > 0) + (x[idx] <= 0) * w[c]
        );
    }
}

template <typename T>
__global__ void _PReluGradNHWC(
    const int               count,
    const int               channels,
    const int               dim,
    const T*                dy,
    const T*                x,
    const T*                w,
    T*                      dx) {
    CUDA_1D_KERNEL_LOOP(idx, count) {
        const int c = idx % channels;
        dx[idx] = dy[idx] * ((x[idx] > 0) + (x[idx] <= 0) * w[c]);
    }
}

template<> void PReluGrad<float, CUDAContext>(
    const int               count,
    const int               channels,
    const int               dim,
    const bool              channel_shared,
    const string&           data_format,
    const float*            dy,
    const float*            x,
    const float*            w,
    float*                  dx,
    CUDAContext*            ctx) {
    if (channel_shared) {
        _PReluGrad<float>
            << < CUDA_BLOCKS(count), CUDA_THREADS,
                 0, ctx->cuda_stream() >> >
            (count, channels, dim, dy, x, w, dx);
    } else {
        if (data_format == "NCHW") {
            _PReluGradNCHW<float>
                << < CUDA_BLOCKS(count), CUDA_THREADS,
                     0, ctx->cuda_stream() >> >
                (count, channels, dim, dy, x, w, dx);
        } else if (data_format == "NHWC") {
            _PReluGradNHWC<float>
                << < CUDA_BLOCKS(count), CUDA_THREADS,
                     0, ctx->cuda_stream() >> >
                (count, channels, dim, dy, x, w, dx);
        } else LOG(FATAL) << "Unknown data format: " << data_format;
    }
}

/*! PReluWGrad <T = float32, Device = CUDA> */

template <typename T>
__global__ void _PReluWGradBcast(
    const int               count,
    const int               rows,
    const int               row_offset,
    const T*                dy,
    const T*                x,
    T*                      bcast_dw) {
    CUDA_1D_KERNEL_LOOP(idx, count) {
        bcast_dw[idx] = dy[idx] * x[idx] * (x[idx] <= 0);
        for (int n = 1; n < rows; n++) {
            const int cur_idx = idx + n * row_offset;
            bcast_dw[idx] +=
                dy[cur_idx] * x[cur_idx] * (x[cur_idx] <= 0);
        }
    }
}

template<> void PReluWGrad<float, CUDAContext>(
    const int               rows,
    const int               row_offset,
    const int               channels,
    const int               dim,
    const bool              channel_shared,
    const string&           data_format,
    const float*            dy,
    const float*            x,
    const float*            multiplier,
    float*                  bcast_dw,
    float*                  dw,
    CUDAContext*            ctx) {
    const int cdim = channels * dim;
    _PReluWGradBcast<float>
        << < CUDA_BLOCKS(cdim), CUDA_THREADS,
             0, ctx->cuda_stream() >> >
        (cdim, rows, row_offset, dy, x, bcast_dw);
    if (channel_shared) {
        float w_sum;
        math::Dot<float, CUDAContext>(channels * dim,
            bcast_dw, multiplier, &w_sum, ctx);
        math::AddScalar<float, CUDAContext>(1, w_sum, dw, ctx);
    } else {
        if (data_format == "NCHW") {
            math::Gemv<float, CUDAContext>(
                CblasNoTrans, channels, dim,
                    1.f, bcast_dw, multiplier,
                        1.f, dw, ctx);
        } else if (data_format == "NHWC") {
            math::Gemv<float, CUDAContext>(
                CblasTrans, dim, channels,
                    1.f, bcast_dw, multiplier, 
                        1.f, dw, ctx);
        } else LOG(FATAL) << "Unknown data format: " << data_format;
    }
}

}  // namespace kernel

}  // namepsace dragon

#endif  // WITH_CUDA