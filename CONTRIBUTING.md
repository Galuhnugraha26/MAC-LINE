# Contributing to MAC-LINE

Thank you for helping improve MAC-LINE — a compact cloud-native machine-learning inference pipeline. Contributions are welcome when they are clear, reproducible, and consistent with the project's deliberately small scope.

## Scope

The current reference workflow is: AI4I 2020 data retrieval, Scikit-learn training, MLflow experiment tracking, FastAPI inference, Docker image, local kind Kubernetes deployment, and CPU-based HPA verification.

Good contributions include reproducible bug fixes, API correctness and input validation, compatibility fixes, documentation, dependency maintenance, test coverage, and small corrections to container or Kubernetes configuration. Requests for new dashboards, LLMs, cloud accounts, or major services are outside the current scope unless the maintainer explicitly changes the roadmap.

## Before you start

- Search existing issues and PRs; avoid duplicates.
- For changes that alter behavior or scope, open an issue explaining the problem and a proposed approach before implementation.
- Keep PRs small and focused; do not bundle unrelated refactors.
- Do not claim that a test, experiment, or deployment succeeded unless you actually ran it.

## Contribution workflow

1. Fork the public repository into your account.
2. Create a descriptive branch from the current default branch (for example, `fix/api-input-validation`).
3. Make the smallest change that solves the documented problem.
4. Validate the change locally and record the commands and results.
5. Open a PR against the project's default branch using the PR template. Link the related issue where relevant.
6. Address review comments. Only an authorized maintainer merges changes into the default branch.

## Local setup and verification

Read `README.md` first. Python 3.12 is the reference Python version used for the verified Windows workflow. The project has separate dependency lists for training and serving.

At minimum, run the following for Python file changes:

```powershell
.\.venv\Scripts\python.exe -m py_compile app.py train.py fetch_data.py
```

When changing training or inference, reproduce the relevant training or endpoint checks and provide the observed response or metrics. When changing Docker, rebuild the image and test the API in a container. When changing Kubernetes manifests, validate YAML and, when practical, report `kubectl` results from a test cluster. If a check cannot be run, state that explicitly; never mark it passed.

The original machine-learning benchmark is **synthetic** (AI4I 2020). Do not imply field-validated industrial failure prediction. Do not introduce target leakage or silently alter the feature set or evaluation data split.

## PR quality requirements

A pull request should describe the problem, the focused change, the verification evidence, documentation impact, and any trade-offs. New behavior should have a reproducible test or a justified, documented manual verification. New dependencies require a concise rationale and license/security consideration.

AI-assisted contributions are welcome when the author understands, verifies, and takes responsibility for the work. In the PR template, declare substantial AI-assisted code or documentation changes, or state **None**. Explain how you personally reviewed and validated generated content. Do not post unverified AI-generated test results or benchmark claims. Write review discussion in your own words.

## Community conduct

Communicate respectfully and focus reviews on technical evidence. See `CODE_OF_CONDUCT.md`.

## Security reports

Do **not** publish vulnerability exploit details or credentials in a public issue. Follow `SECURITY.md`.

## Maintainer authority and credit

The project is maintained by `@Galuhnugraha26`. Contributions retain their authorship through Git history and PR attribution. Opening a PR does not guarantee acceptance; decisions follow `GOVERNANCE.md`.

## No automatic approval or mandatory CLA

Issues and PRs are proposals, not commitments to accept work. The project does not currently require a contributor license agreement (CLA) or signed commits; do not assume such a policy exists. If a licensing policy changes, it must be documented before applying it to future contributions.
