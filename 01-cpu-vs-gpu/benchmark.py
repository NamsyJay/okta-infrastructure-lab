import time
import torch

sizes = [100, 500, 1000, 2500, 5000]

device = torch.device("cuda")

print("PyTorch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("GPU:", torch.cuda.get_device_name(0))
print("Benchmark device:", device)
print()

for size in sizes:
    print(f"Matrix size: {size} x {size}")

    # Create tensors directly in GPU VRAM
    a = torch.randn(size, size, device=device)
    b = torch.randn(size, size, device=device)

    # Warm-up operation
    _ = torch.matmul(a, b)
    torch.cuda.synchronize()

    # Start timing only after warm-up
    start = time.perf_counter()

    result = torch.matmul(a, b)

    # Wait for GPU computation to finish
    torch.cuda.synchronize()

    end = time.perf_counter()

    gpu_time = end - start

    print("Device:", result.device)
    print(f"GPU time: {gpu_time:.6f} seconds")
    print("-" * 40)