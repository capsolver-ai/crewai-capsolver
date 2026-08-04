from __future__ import annotations

import asyncio
import json
from typing import Type

from capsolver_agent.schema import create_executor
from crewai.tools import BaseTool
from pydantic import BaseModel, Field, PrivateAttr


class SolveCaptchaInput(BaseModel):
    captcha_type: str = Field(description="reCaptchaV2, reCaptchaV3, or cloudflare")
    website_url: str
    website_key: str


class SolveCaptchaTool(BaseTool):
    name: str = "Solve CAPTCHA"
    description: str = "Solve a CAPTCHA for an authorized workflow and return a token."
    args_schema: Type[BaseModel] = SolveCaptchaInput
    _executor: object = PrivateAttr()

    def __init__(self, api_key: str | None = None, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self._executor = create_executor(api_key=api_key)

    def _run(self, captcha_type: str, website_url: str, website_key: str) -> str:
        result = asyncio.run(self._executor.execute("solve_captcha", {
            "captcha_type": captcha_type, "website_url": website_url, "website_key": website_key,
        }))
        return json.dumps(result)


def get_capsolver_tools(api_key: str | None = None) -> list[BaseTool]:
    return [SolveCaptchaTool(api_key=api_key)]

__version__ = "0.1.0"
