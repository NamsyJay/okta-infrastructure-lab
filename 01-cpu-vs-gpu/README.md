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
