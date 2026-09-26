### Enterprise ML Experiment Tracking

```
                     Project 03
          Enterprise ML Experiment Tracking

                    Developer
                        │
                        ▼
                  Python / venv
                        │
                   test_minio.py
                        │
             ┌──────────┴──────────┐
             │                     │
             ▼                     ▼
          Git Repo              MLflow
             │                     │
        Commit SHA                  │
             │                     │
             └────────► MLflow Run ◄┘
                              │
                 ┌────────────┼────────────┐
                 │            │            │
                 ▼            ▼            ▼
              Metrics       Tags       Artifacts
                 │            │            │
          test_metric=1   git_commit       │
                                           ▼
                                         MinIO
                                    Object Storage
```

1. Isolated Python environment

Project 03 runs inside a Python venv.
Instead of relying on whatever packages happen to be installed on the machine, the project has its own runtime environment.

```
requirements.txt
```

### 2. Git repository isolation

Originally Git had accidentally been initialized at:

3. .gitignore

We deliberately separated source-controlled assets from local runtime state.

Tracked:
```
.gitignore
requirements.txt
train.py
test_minio.py
```

Ignored:
```
venv/
mlruns/
mlflow.db
.env
.env.*
__pycache__/
*.pyc
minio-data/
```

This is important because things such as virtual environments, secrets, local databases and runtime state do not belong in Git.

### 4.MLflow Tracking Server

- We successfully created MLflow runs and logged a metric
- Also saw the history of failed and successful runs in the MLflow UI.

That itself is useful:

```
Experiment
    │
    ├── failed run
    ├── failed run
    ├── failed run
    │
    └── successful run
```

Experiment tracking preserves the history instead of showing only the final successful attempt.

### 5. MinIO artifact storage.
Initially, MLflow's artifacts were effectively local. I then connected MLflow to MinIO as S3-compatible object storage.

So I proved:
```
Python
   │
   ▼
MLflow
   │
   │ log_artifact()
   ▼
MinIO
   │
   ▼
Bucket / Run Artifacts
```

This shows MLflow tracks the experiment; object storage stores the potentially large artifacts produced by experiments.


### 6. Git → MLflow lineage
We retrieved the repository's Git SHA:

```
git rev-parse HEAD
```
and modified test_minio.py to retrieve that programmatically:

```
git_commit = subprocess.check_output(
    ["git", "rev-parse", "HEAD"],
    text=True
).strip()
```

Then attached it to the MLflow run:

```
mlflow.set_tag("git_commit", git_commit)
```

The Experiment flow
```
Git Commit
     │
     ▼
MLflow Run
     │
     ├── Metric
     ├── Metadata
     └── Artifact
             │
             ▼
           MinIO
```

Now we're starting to establish lineage.

### 7. We caught an important reproducibility problem

```
commit: abc123
```

Modify test_minio.py and run the experiment without committing those modifications.

MLflow might record:

```
git_commit = abc123
```

but abc123 isn't actually the exact code that executed.
That's why we established:

```
Modify code
    ↓
git diff
    ↓
Commit
    ↓
Working tree clean
    ↓
Run experiment
    ↓
Record commit SHA
```

That's a much stronger reproducibility story.
