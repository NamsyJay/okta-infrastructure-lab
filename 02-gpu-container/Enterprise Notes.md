### Enterprise Objectives

- Build a reproducible container image for a GPU-enabled ML workload.
- Explain the responsibilities of the host NVIDIA driver, CUDA runtime/toolkit, container runtime, and ML framework.
- Expose host GPU resources securely to containers using the NVIDIA Container Toolkit.
- Verify GPU availability and CUDA compatibility from inside the container using PyTorch.
- Observe GPU utilisation, VRAM allocation, and workload execution behaviour.
- Benchmark CPU and GPU execution to determine whether GPU acceleration provides meaningful performance improvement.
- Troubleshoot common GPU-container compatibility issues across drivers, CUDA versions, container images, and PyTorch.
- Prepare the workload architecture for migration to Kubernetes/EKS using GPU worker nodes, resource requests, NVIDIA device plugins, scheduling constraints, and observability.

Outcome
Production ML workloads should not depend on manually configured development machines.

Containerising the workload provides a reproducible execution environment containing the application code, Python dependencies, PyTorch version, and required CUDA userspace libraries while allowing the host infrastructure to provide the physical GPU and NVIDIA driver.

This establishes the foundation required for running GPU workloads consistently across development environments, GPU-enabled cloud instances, CI/CD pipelines, and eventually Kubernetes/EKS.
