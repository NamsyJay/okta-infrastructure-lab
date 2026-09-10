## Reproducible MLflow experiment

### Aim: Compare Three visible MLflow runs.

### Outcome:An enterprise must know which training run produced it, which parameters were used, what metrics justified the decision and which artifacts belong to that run.

### Experiment: Take one simple ML model and use MLflow to track three training runs where you change only one parameter between runs.

## Core Business Value
#### 1. Regulatory Compliance & Audit Readiness
In regulated industries (finance, healthcare, insurance), you must prove how a model was built, not just that it works: 
- Experiment tracking provides automated documentation of every training run: which data snapshot, which code version, which hyperparameters produced which model.

Enterprise scenario: A fraud detection model is flagged during an external audit. With MLflow, you pull up the exact run: "Version X was trained on dataset v2.3, with n_estimators=150, achieving 94.2% accuracy on test set Y, approved by Data Scientist Z on date D." Without tracking, that investigation takes days or weeks.

#### 2. Collaboration & Knowledge Retention
In a team of 15 data scientists:
- Private knowledge becomes institutional knowledge: Run history moves out of individual notebooks and spreadsheets into a shared, searchable record
- Team members can build on each other's work instead of duplicating experiments or starting from scratch.
- When someone leaves the company, their experimental history doesn't leave with them

Business outcome: Faster onboarding, reduced redundant compute costs, and accelerated time-to-production for new models
