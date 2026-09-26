<div align="center">
<img width="785" height="649" alt="Screenshot 2026-09-03 at 20-35-58 Image Structure Modification Request - Kimi" src="https://github.com/user-attachments/assets/3761ca13-4f1e-4864-955f-37c753caeb89" />

This directory covers the implementation of Project 02 in the ai-infrastructure-lab series. It bridges standalone PyTorch benchmarking and container runtime orchestration, establishing how model serving runtimes access underlying host GPUs, allocate VRAM, expose metrics, and prepare for orchestration on Kubernetes (EKS).


## Objectives

1. Containerize PyTorch CUDA Runtimes: Build lightweight, multi-stage Docker images using official NVIDIA CUDA base images.

2. Configure GPU Runtime Passthrough: Leverage nvidia-container-toolkit to pass GPU devices into isolated container environments.

3. Validate VRAM & Compute Allocation: Ensure proper device visiblity, isolated CUDA allocation, and execution inside container boundaries.

4. Prepare Observability Hooks: Expose CUDA/DCGM metrics for Prometheus scraping to track VRAM consumption and GPU compute utilization.

5. Stage for Kubernetes/EKS: Ensure container entrypoints and environment flags comply with Kubernetes [nvidia.com/gpu](https://nvidia.com/gpu) resource scheduling constraints.
