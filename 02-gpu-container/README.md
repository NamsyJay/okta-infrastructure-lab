<img width="785" height="649" alt="Screenshot 2026-09-03 at 20-35-58 Image Structure Modification Request - Kimi" src="https://github.com/user-attachments/assets/3761ca13-4f1e-4864-955f-37c753caeb89" />


## Objectives

- Containerize PyTorch CUDA Runtimes: Build lightweight, multi-stage Docker images using official NVIDIA CUDA base images.

- Configure GPU Runtime Passthrough: Leverage nvidia-container-toolkit to pass GPU devices into isolated container environments.

- Validate VRAM & Compute Allocation: Ensure proper device visiblity, isolated CUDA allocation, and execution inside container boundaries.

- Prepare Observability Hooks: Expose CUDA/DCGM metrics for Prometheus scraping to track VRAM consumption and GPU compute utilization.

- Stage for Kubernetes/EKS: Ensure container entrypoints and environment flags comply with Kubernetes [nvidia.com/gpu](https://nvidia.com/gpu) resource scheduling constraints.
