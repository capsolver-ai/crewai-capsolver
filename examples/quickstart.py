"""Use CapSolver Agent execution inside CrewAI tools."""

import asyncio
import json
import os

from capsolver_agent import create_executor
from crewai import Agent, Crew, Process, Task
from crewai.tools import tool


capsolver = create_executor()


@tool("get_capsolver_balance")
def get_capsolver_balance() -> str:
    """Return the current CapSolver balance for the authorized account."""
    result = asyncio.run(capsolver.execute("get_balance", {}))
    return json.dumps(result, ensure_ascii=False)


@tool("solve_captcha")
def solve_captcha(captcha_type: str, website_url: str, website_key: str) -> str:
    """Solve a supported CAPTCHA in a lawful, user-authorized workflow."""
    result = asyncio.run(
        capsolver.execute(
            "solve_captcha",
            {
                "captcha_type": captcha_type,
                "website_url": website_url,
                "website_key": website_key,
            },
        )
    )
    return json.dumps(result, ensure_ascii=False)


def main() -> None:
    specialist = Agent(
        role="Authorized workflow recovery specialist",
        goal="Use CapSolver tools only when the user supplied the required target details.",
        backstory="You support lawful, terms-compliant automation and never invent target data.",
        tools=[get_capsolver_balance, solve_captcha],
        llm=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        verbose=True,
    )
    task = Task(
        description=os.getenv(
            "DEMO_PROMPT",
            "Use the available CapSolver tool to check the account balance.",
        ),
        expected_output="A concise explanation of the structured CapSolver result.",
        agent=specialist,
    )
    result = Crew(agents=[specialist], tasks=[task], process=Process.sequential).kickoff()
    print(result)


if __name__ == "__main__":
    main()
