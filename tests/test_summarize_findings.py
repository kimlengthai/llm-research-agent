import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from src.agent.nodes.summarize_findings import summarize_findings

def test_summarize_findings_output():
    test_docs = [
        {
            "query": "2022 FIFA World Cup winner",
            "content": "Argentina won the 2022 FIFA World Cup, defeating France in a dramatic final match.",
            "source": "https://example.com/article1"
        },
        {
            "query": "final match result",
            "content": "The final score was 3-3, and Argentina won on penalties.",
            "source": "https://example.com/article2"
        }
    ]
    summary = summarize_findings(test_docs)
    assert isinstance(summary, dict)
    assert "summary" in summary
    assert "key_points" in summary
    assert "sources" in summary
    assert isinstance(summary["key_points"], list)
    assert isinstance(summary["sources"], list)