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
