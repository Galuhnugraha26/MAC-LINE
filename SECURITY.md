# Security Policy

## Supported context

MAC-LINE is a small local reference implementation; it is **not** a hardened production service or an industrial safety system. Security fixes affecting its current maintained branch are in scope for review.

## Reporting a vulnerability

**Do not disclose exploitable details, credentials, tokens, or sensitive information in a public Issue or PR.**

When the public GitHub repository is available and **Private Vulnerability Reporting** has been enabled by the owner, use the repository's **Security -> Report a vulnerability** workflow to submit information privately.

If private reporting is not enabled, use the **Security contact request** Issue form solely to ask the maintainer to enable a private reporting channel. **Do not include any vulnerability details, proof of concept, access credentials, or technical exploit steps** in that public issue. Wait for a private channel before sharing details.

Useful private details: affected version or commit, reproducible conditions, potential impact, and a minimal proof of concept that does not expose secrets.

## Security practices

- Do not commit passwords, API keys, `.env` files, personal information, or local MLflow databases.
- Do not deserialize arbitrary third-party `joblib`/pickle artifacts; only load model artifacts from a trusted source.
- Treat `--kubelet-insecure-tls` as a **local kind test-only** workaround. It is not a production-security recommendation.
- Report dependency vulnerabilities with affected versions and verified reproduction when possible.
- Do not run untrusted PR code with secrets or privileged access merely to test it.

## Disclosure

The maintainer will assess and coordinate fixes before public disclosure where appropriate. No response or resolution time is guaranteed by this volunteer-maintained project.
