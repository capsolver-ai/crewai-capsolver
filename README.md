<div align="center">

# crewai-capsolver

**Official CapSolver tools for CrewAI agents, crews, and flows — add CAPTCHA recovery to autonomous workflows.**

[![Status](https://img.shields.io/badge/status-release--candidate-blue)](#project-status)
[![License](https://img.shields.io/badge/license-ISC-green.svg)](LICENSE)
[![Docs](https://img.shields.io/badge/docs-CapSolver-7c3aed)](https://docs.capsolver.com/en/guide/ai/capsolver-for-ai-agents/)
[![Responsible use](https://img.shields.io/badge/use-authorized%20automation-0a7)](#responsible-use)

[Quick start](#quick-start) · [Architecture](#architecture) · [Examples](#examples) · [Documentation](#documentation) · [Contributing](#contributing)

</div>

## Why this integration exists

Agents can navigate, click, and type, but verification challenges can interrupt a successful workflow. This repository adds CapSolver as a recovery layer for CrewAI. Your application keeps its browser session, orchestration, model, and business logic while CapSolver handles supported challenges and returns control to the original task.

Initial adapter code, tests, CI, and release automation are included.

## Highlights

- Native CrewAI integration rather than a generic copy-and-paste snippet.
- Shared maintained engine through capsolver-agent; solving logic is not duplicated.
- Async-friendly execution for browser and agent workloads.
- Structured results for tracing, bounded retries, and debugging.
- Token mode and browser recovery where supported.
- Designed for lawful, user-authorized, terms-compliant automation.

## Project status

| Item | Value |
|---|---|
| Lifecycle | publish-now |
| Ecosystem | CrewAI |
| Language | Python |
| Shared runtime | capsolver-agent |
| Maintainer | [capsolver-ai](https://github.com/capsolver-ai) |
| Coverage | reCAPTCHA v2/v3 and Cloudflare Turnstile, subject to shared runtime |

## Installation

~~~bash
pip install crewai-capsolver
export CAPSOLVER_API_KEY="CAP-..."
~~~

Never commit an API key. Browser-backed Python projects may also need: playwright install chromium.

## Quick start

~~~python
# Representative API. Scaffolds finalize this during their release gate.
integration = get_capsolver_tools()
~~~

See [examples](examples/) for full flows. Use only pages and accounts you own or are explicitly authorized to automate.

## Architecture

~~~mermaid
flowchart LR
    A["CrewAI application"] -->|"verification detected"| B["crewai-capsolver"]
    B -->|"structured call"| C["capsolver-agent"]
    C -->|"solve request"| D["CapSolver API"]
    D -->|"token and traceable result"| C
    C -->|"fill or return"| B
    B -->|"resume task"| A
~~~

This repository owns framework conversion, examples, compatibility tests, and release cadence. Canonical detection, solving, fill-back, retries, and errors remain in shared CapSolver packages.

## Capabilities

| Capability | Purpose | Browser |
|---|---|---:|
| solve_captcha | Solve from known type, URL, and site key | No |
| detect_captchas | Detect supported challenges | Yes |
| solve_on_page | Detect, solve, and fill | Yes |
| get_balance | Read account balance | No |
| get_supported_captchas | Inspect registered handlers | No |

## Examples

Released adapters should contain minimal registration, token mode, browser recovery where applicable, structured error handling, mocked tests, and an opt-in authorized live test.

## Configuration

| Variable | Required | Description |
|---|---:|---|
| CAPSOLVER_API_KEY | Yes | CapSolver API key |
| OPENAI_API_KEY | Example-dependent | Only for examples using OpenAI models |

Never log keys, cookies, proxy passwords, solved tokens, personal information, or private URLs.

## Error handling

Retry only transient network, timeout, and rate-limit failures with bounded backoff. Do not retry invalid parameters indefinitely. Retain request identifiers for diagnosis and redact sensitive fields from exported logs. See [troubleshooting](docs/troubleshooting.md).

## Compatibility and releases

- Semantic Versioning after the first stable release.
- CI tests supported runtime versions.
- Dependabot tracks framework and Actions updates.
- Tags publish through trusted publishing where available.
- Pre-1.0 upstream breaking changes may require minor releases.

## Responsible use

You must obtain authorization, follow applicable law and target-site terms, apply reasonable rate limits, and protect account data. Do not use this project for unauthorized access, abusive automation, or evasion of protections around private accounts or data.

## Documentation

- [CapSolver for AI Agents](https://docs.capsolver.com/en/guide/ai/capsolver-for-ai-agents/)
- [Quick Start](https://docs.capsolver.com/en/guide/ai/introduction-and-quick-start/)
- [Core SDK](https://docs.capsolver.com/en/guide/ai/core-sdk/)
- [Agent Tools](https://docs.capsolver.com/en/guide/ai/agent-tools/)
- [MCP Service](https://docs.capsolver.com/en/guide/ai/mcp-service/)
- [Architecture](docs/architecture.md)
- [Security](SECURITY.md)
- [Support](SUPPORT.md)

## Contributing

Read [CONTRIBUTING](CONTRIBUTING.md) and [Code of Conduct](CODE_OF_CONDUCT.md). Issues and pull requests must use redacted fixtures and never contain credentials or private target data.

## License

[ISC](LICENSE)
