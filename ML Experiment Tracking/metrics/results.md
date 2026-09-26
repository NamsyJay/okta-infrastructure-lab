# Results

### Experiment1:

<img width="1177" height="705" alt="Screenshot 2026-09-10 at 23-42-15 Compare Runs - MLflow" src="https://github.com/user-attachments/assets/bd32df14-9e5f-4815-a9ab-86fed1715eb4" />

1. Justifying Deployment Decisions
  - Data science isn't deterministic software; it's empirical experimentation.

- The Problem: A data scientist claims, "Model B is better than Model A." Without structured tracking, that claim is subjective.

- The Platform Fix: Visual parameter-versus-metric comparisons provide empirical proof. You can instantly see how changing a single variable (n_estimators = 50 vs 200) affects performance (accuracy).

### Experiment 2:

<img width="1204" height="693" alt="Screenshot 2026-09-10 at 23-41-38 Compare Runs - MLflow" src="https://github.com/user-attachments/assets/114825eb-50ab-4852-ae77-2ee3e0f5f53a" />

1. Immutable Model Lineage & Governance

  - The Run ID is the commit SHA of the ML world.

- The Problem: In an enterprise (e.g., banking or healthcare), you cannot just deploy a .pkl or .onnx file generated on someone's laptop. Regulators and security teams will ask: "Who trained this model, on what code commit, with what dataset, and using what hyperparameters?"

- The Platform Fix: The Run ID permanently ties the binary model artifact stored in S3/MinIO to its execution parameters, metric outputs, training duration, and Git commit.

2. Resource Utilization & Cost Optimization (FinOps)
  Notice the execution durations: 9.5s for 200 trees vs 8.8s for 100 trees.

- DevOps Translation: In large-scale training runs (e.g., fine-tuning LLMs or training multi-node XGBoost models on GPU clusters), runtime translates directly to compute cost ($ / GPU-hour).

- If doubling n_estimators increases training time/cost by 10% but yields zero statistical improvement in accuracy, the ML Architect will reject rf_n_est_200 to save compute budget and reduce inference latency in production.


## The Bottom Line: 
I am building an immutable audit log and performance telemetry system for non-deterministic AI assets before they reach production servers.
