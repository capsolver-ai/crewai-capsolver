# CrewAI + CapSolver Agent examples

[![Demo repository](https://img.shields.io/badge/type-runnable%20demo-0A7BBB)](#repository-scope)
[![CI](https://github.com/capsolver-ai/crewai-capsolver/actions/workflows/ci.yml/badge.svg)](https://github.com/capsolver-ai/crewai-capsolver/actions/workflows/ci.yml)
[![License: ISC](https://img.shields.io/badge/license-ISC-green.svg)](LICENSE)

Runnable CrewAI examples showing how an agent, task, or crew can call the official [`capsolver-agent`](https://github.com/capsolver-ai/capsolver-agent) executor.

> This is an examples repository, not a separately released `crewai-capsolver` package.

## Repository scope

The demo wraps shared CapSolver operations with CrewAI's `@tool` decorator. It does not copy SDK behavior or maintain another adapter version.

## Quick start

```bash
git clone https://github.com/capsolver-ai/crewai-capsolver.git
cd crewai-capsolver
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Export the values in [`.env.example`](.env.example), then run `python examples/quickstart.py`.

## Key integration code

```python
from capsolver_agent import create_executor
from crewai.tools import tool

capsolver = create_executor()

@tool("get_capsolver_balance")
def get_capsolver_balance() -> str:
    return str(asyncio.run(capsolver.execute("get_balance", {})))
```

See [`examples/quickstart.py`](examples/quickstart.py) for a complete Crew and two CapSolver tools.

## Project layout

```text
examples/quickstart.py   CrewAI agent, task, crew, and tools
requirements.txt         Shared SDK repositories plus CrewAI
tests/test_demo.py        Offline validation
.github/workflows/ci.yml  Demo checks
```

## Documentation

- [CapSolver Agent tools](https://docs.capsolver.com/en/guide/ai/agent-tools/)
- [CapSolver for AI agents](https://docs.capsolver.com/en/guide/ai/capsolver-for-ai-agents/)
- [CrewAI tools](https://docs.crewai.com/en/concepts/tools)

## Responsible use

Use these tools only in lawful, user-authorized workflows that respect target-site terms. Never commit secrets or private target data.

## Contributing, support, and license

See [CONTRIBUTING.md](CONTRIBUTING.md), [SUPPORT.md](SUPPORT.md), and [SECURITY.md](SECURITY.md). Licensed under the [ISC License](LICENSE).

CrewAI is a third-party project. This repository is maintained by CapSolver and is not affiliated with or endorsed by CrewAI.
