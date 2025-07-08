import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from src.agent.agent import run_agent

def test_run_agent_end_to_end():
    result = run_agent("What happened in the 2022 FIFA World Cup?")
    assert isinstance(result, dict)
    assert "summary" in result
    assert "key_points" in result
    assert "sources" in result