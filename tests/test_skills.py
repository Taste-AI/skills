from __future__ import annotations

import re
from pathlib import Path
from typing import get_args

import httpx
import pytest
from fastmcp import Client

from mcp_gateway.server import BrandSection, build_mcp
from mcp_gateway.upstream import DesignApiClient

SKILLS = sorted((Path(__file__).parents[1] / "skills").glob("*/SKILL.md"))
SECTIONS = set(get_args(BrandSection))

# A tool shows up as a call (`extract_brand(url)`) or as a backticked name that
# starts with a tool verb, which also catches retired names like `get_brand`.
_CALL = re.compile(r"\b([a-z]+(?:_[a-z]+)+)\(")
_NAMED = re.compile(r"`((?:extract|poll|get|list|search|verify|lookup|submit|find)_[a-z_]+)`")
_SECTIONS_ARG = re.compile(r"sections=\[([^\]]*)\]")
_QUOTED = re.compile(r"[\"']([a-z_]+)[\"']")


async def _registered_tools() -> set[str]:
    api = DesignApiClient(
        "http://up",
        client=httpx.AsyncClient(
            transport=httpx.MockTransport(lambda request: httpx.Response(200))
        ),
        search_timeout=240.0,
    )
    async with Client(build_mcp(api)) as client:
        return {tool.name for tool in await client.list_tools()}


def test_the_plugin_ships_three_skills() -> None:
    assert [path.parent.name for path in SKILLS] == [
        "brand-adherence",
        "brand-search",
        "taste-director",
    ]


@pytest.mark.parametrize("skill", SKILLS, ids=lambda path: path.parent.name)
async def test_skill_names_only_registered_tools(skill: Path) -> None:
    text = skill.read_text()
    named = set(_CALL.findall(text)) | set(_NAMED.findall(text))
    assert named - await _registered_tools() == set()


@pytest.mark.parametrize("skill", SKILLS, ids=lambda path: path.parent.name)
def test_skill_names_only_brand_sections(skill: Path) -> None:
    text = skill.read_text()
    named = {
        name
        for arg in _SECTIONS_ARG.findall(text)
        for name in _QUOTED.findall(arg)
    }
    for line in text.splitlines():
        if "legal names" in line:
            named |= set(re.findall(r"`([a-z_]+)`", line))
    assert named - SECTIONS == set()
