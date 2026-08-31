# Observability With Business Meaning

#### 1. GPU Utilization (%)
GPU Utilization measures the percentage of time the GPU kernels were actively executing over a sample period.

#### 2. VRAM Utilization (Memory Usage)
VRAM metrics track memory allocated by PyTorch tensors versus the peak memory reserved by the CUDA memory allocator.

#### 3. Inference Latency (Time per Request)
Because PyTorch GPU operations are asynchronous, using basic Python ```time.time()`` will measure host-side execution and yield inaccurate results. 
You must sync CUDA streams or use ```torch.cuda.Event``` for true hardware latency.

#### 4. Throughput (Requests or Tokens per Second)
Throughput measures the volume of work processed per unit of time over a batch or timeframe.

```text
Requests per Second (RPS):$$\text{Requests per Second} = \frac{\text{Batch Size}}{\text{Latency in Seconds}}$$Tokens per Second (TPS - for LLMs / NLP models):$$\text{Tokens per Second} = \frac{\text{Total Generated Tokens}}{\text{Latency in Seconds}}$$
```

#### 5. Cost Per Inference / Request
Cost is derived from the hourly billing rate of the GPU instance
Calculate cost per request based on latency:
$$\text{Cost per Request} = \text{Cost per Second} \times \text{Latency in Seconds}$$


## Executive interpretation

| Metric                     |                  Your result | Business interpretation                                                                                                 |
| -------------------------- | ---------------------------: | ----------------------------------------------------------------------------------------------------------------------- |
| GPU                        | NVIDIA Tesla T4, ~15 GB VRAM | Relatively modest/older data-centre GPU, so good results here suggest the workload may not require premium accelerators |
| Peak VRAM                  |                   **168 MB** | Only about **1.1% of available VRAM** — enormous unused memory headroom                                                 |
| Single inference latency   |                  **5.83 ms** | Very fast compute-level response; potentially suitable for interactive/real-time workloads                              |
| Single-request throughput  |                **171 req/s** | Strong theoretical capacity if requests are processed individually                                                      |
| Batch-32 throughput        |          **402.69 images/s** | Batching significantly improves GPU utilisation and economics                                                           |
| Batch-32 execution time    |               **0.0795 sec** | GPU can process 32 units in ~80 ms in your test                                                                         |
| GPU utilisation after test |                       **0%** | Expected because `nvidia-smi` was captured after the workload ended; it does **not** prove the GPU wasn't used          |
| Peak reserved memory       |                   **168 MB** | Current model is nowhere near memory constrained                                                                        |
| Reported inference cost    |                Extremely low | Interesting directionally, but **not yet reliable enough for financial forecasting**                                    |
