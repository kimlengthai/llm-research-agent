import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from src.agent.nodes.generate_queries import generate_queries

def test_generate_queries_output():
    result = generate_queries("What happened in the 2022 FIFA World Cup?")
    assert isinstance(result, list)
    assert 2 <= len(result) <= 6
    assert all(isinstance(q, str) for q in result)