## THE GOAL: Why would I deploy an AI workload on a GPU instead of a CPU?
### Today’s small action: learn the CPU → GPU mental model. Spend 20–30 minutes understanding just four concepts: CPU, GPU, VRAM, and why AI workloads benefit from parallel processing.


- CPU: relatively few powerful workers, excellent at complicated/sequential/general-purpose tasks.
- GPU: thousands of smaller workers capable of doing enormous numbers of similar mathematical operations simultaneously.
- VRAM: A GPU has its own high-speed memory.

Simply Put
CPU → RAM
GPU → VRAM

- Data parallelism means giving different GPUs different portions of the data while they work on copies of the model.
- Model parallelism becomes necessary when, for example, the model is too large to fit into the VRAM of one GPU, so parts of the model are distributed across multiple GPUs.
- High throughput means we're optimizing for doing a huge amount of computational work in a given period—not necessarily making one individual instruction execute faster.

### High-Performance Computing (HPC) aggregates computing power—typically through clustered server nodes—to process complex mathematical models, large-scale simulations, and massive data workloads far beyond the capabilities of standard enterprise servers.

## AI infrastructure thinking
- When running an AI model, things such as the model weights, activations and other intermediate data consume GPU memory.

## Obstacles
- A GPU can be computationally powerful enough for a model but not have enough VRAM to hold what the workload requires.

- My questions are changing:
  "Do I need a GPU?"

- It is now:
  "Which GPU, how much VRAM, how many GPUs, and for what workload?"




