# MAC-LINE Governance

## Project purpose

MAC-LINE is a minimal, reproducible example of cloud-native ML serving: AI4I 2020 -> Scikit-learn -> MLflow -> FastAPI -> Docker -> Kubernetes kind -> CPU-based HPA. Its purpose is to demonstrate reliable integration and transparent, verifiable evidence — not to grow into a general-purpose MLOps platform.

## Leadership

- **Founder and lead maintainer:** `@Galuhnugraha26`.
- The lead maintainer decides project direction, reviews changes, controls releases, and determines which contributions are merged.
- Contributors may propose work through issues, forks, and pull requests. A PR alone does not grant repository write or merge permissions.
- Additional maintainers, if ever added, require an explicit owner decision and the appropriate GitHub permission settings.

## Decision principles

1. **Evidence over appearance.** Claims of passing tests, model scores, and HPA behavior require reproducible evidence. Screenshots are supporting evidence, not substitutes for source code and commands.
2. **Small scope.** Prefer focused fixes and maintenance over feature proliferation.
3. **Safety and accuracy.** Do not present AI4I as real machine measurements; do not suggest deployment to physical equipment without validation.
4. **Traceability.** PRs must explain what changed, why it changed, and how it was checked.
5. **Contributor respect.** Discuss substantial work early; credit contributors; review constructive criticism fairly.
6. **Security.** Never commit credentials, personal data, local databases, or unreviewed opaque binaries. Treat serialized model files as trusted-code artifacts, not safe to load from arbitrary sources.

## Workflow and review

- Open an issue first for nontrivial changes. The lead maintainer may close duplicates, out-of-scope proposals, unsupported claims, or unsafe requests with an explanation.
- Contributors work on forks and request review via PRs.
- A PR should not be merged until relevant checks and manual review have been completed. Where no CI exists, the PR must document local validation; do not pretend there is automated protection.
- The default branch is intended to be protected using GitHub branch protection/rulesets where supported and appropriate. CODEOWNERS and this document do not, by themselves, enforce GitHub access controls.
- Only an authorized maintainer may merge to the default branch. The lead maintainer may postpone, request changes, or decline contributions.

## Releases and scope changes

A new release should have a concise summary, version identifier, and verified behavior. Any significant scope expansion must be discussed in an issue and explicitly approved by the maintainer before implementation.

## Relation to internal implementation names

**MAC-LINE** is the project's public-facing identity. Internal identifiers such as `modelserve` can remain unchanged for compatibility and repeatability; no rename is necessary for branding.

## Initial single-maintainer configuration

GitHub protection settings must match available maintainers. With a sole maintainer, do not configure a mandatory second-person approval that would prevent the maintainer from merging their own routine maintenance PRs. Prefer PR-based review, disable force-push/deletion, and require reproducible validation. Add mandatory external approval only when another authorized reviewer actually exists. Do not claim automated CI checks until workflows are present and passing.
