<img width="906" height="554" alt="Project-001" src="https://github.com/user-attachments/assets/4dd8d68c-729e-42c4-83d2-564e79155d16" />

# AI Infrastructure Lab

> A hands-on journey from traditional DevOps infrastructure into AI infrastructure engineering — starting from compute fundamentals and progressing toward production AI platforms.

## About

This repository documents my practical journey into AI Infrastructure Engineering.

Rather than starting by deploying large language models or building complex Kubernetes platforms, I am beginning with the infrastructure fundamentals underneath AI workloads:

**PyTorch → Tensors → CPU → GPU → VRAM → Parallel Computation → Measurement**

The goal is to understand not only how to run AI workloads, but how to reason about the compute, memory, performance, cost, scalability, and operational characteristics behind them.

---

## Project 01 — CPU vs GPU Compute

### Objective

The first experiment investigates a simple question:

> **What changes when the same tensor workload is executed on a CPU versus a GPU?**

The workload uses PyTorch matrix multiplication across increasingly large tensors.

This provides a simple way to observe how workload size and parallel computation affect execution performance.

---

## Architecture

```text
                    PyTorch
                       │
                    Tensors
                       │
             ┌─────────┴─────────┐
             │                   │
          CPU Path            GPU Path
             │                   │
            RAM                 VRAM
             │                   │
      Matrix Multiply      Matrix Multiply
             │                   │
        Execution Time       Execution Time
             │                   │
             └─────────┬─────────┘
                       │
                    Compare
``` 

## Lab Environments
CPU Environment
Linux
Python
PyTorch
CPU execution
System RAM

## GPU Environment
Lightning AI Studio
NVIDIA Tesla T4
CUDA
PyTorch
16 GB-class GPU memory
GPU execution


## Experiment 1 — Understanding Tensors
### The project began with two small 2×2 tensors:

```text
import torch

a = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
b = torch.tensor([[5.0, 6.0], [7.0, 8.0]])

result = torch.matmul(a, b)

print(result)
print("Device:", result.device)
```

```text
PyTorch
   ↓
Tensor
   ↓
CPU
   ↓
RAM
   ↓
Computation
```

## Experiment 2 — Moving the Workload to GPU
### The tensors were then explicitly transferred to the CUDA device:

```text
a = a.to("cuda")
b = b.to("cuda")

result = torch.matmul(a, b)

print("Result device:", result.device)

Result:

Before:
Tensor A device: cpu
Tensor B device: cpu

After:
Tensor A device: cuda:0
Tensor B device: cuda:0

Result device: cuda:0
```

- This demonstrated an important infrastructure principle:
  - GPU availability does not automatically mean GPU utilization.

## Experiment 3 — CPU vs GPU Benchmark
### Matrix sizes tested:
- 100 × 100
- 500 × 500
- 1,000 × 1,000
- 2,500 × 2,500
- 5,000 × 5,000

```text
|   Matrix Size |  Local CPU |  NVIDIA T4 | Approx. Speedup |
| ------------: | ---------: | ---------: | --------------: |
|     100 × 100 | 0.000494 s | 0.000351 s |            1.4× |
|     500 × 500 | 0.009561 s | 0.000213 s |           44.9× |
| 1,000 × 1,000 | 0.026101 s | 0.000545 s |           47.9× |
| 2,500 × 2,500 | 0.422842 s | 0.004550 s |           92.9× |
| 5,000 × 5,000 | 3.915636 s | 0.079346 s |           49.3× |
```

### These are initial single-run measurements across two different compute environments. They demonstrate the experiment but should not be interpreted as a general CPU-vs-GPU performance claim.


## What I Learned
### 1. GPU availability ≠ GPU utilization

Provisioning a GPU does not automatically move application workloads onto it.

## 2. GPUs are not simply "faster CPUs"
### Their advantage becomes especially important for workloads containing large amounts of parallelizable numerical computation.

## 3. Workload size matters
### Small workloads may not benefit significantly from accelerator hardware because GPU execution has its own overheads.

## 4. VRAM is an infrastructure resource
### GPU workloads introduce another important capacity constraint:

```text
CPU ↔ System RAM
GPU ↔ VRAM
```

Compute capability alone is therefore not enough when selecting accelerator infrastructure.

## 5. Measurement methodology matters

### GPU operations can execute asynchronously.
Accurate timing requires synchronization:

```text
torch.cuda.synchronize()
```
Without synchronization, benchmark results can be misleading.


