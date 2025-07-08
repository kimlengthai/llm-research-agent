import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from src.agent.nodes.retrieve_documents import retrieve_documents

def test_retrieve_documents_output():
    queries = ["2022 FIFA World Cup winner", "final match result"]
    docs = retrieve_documents(queries)
    assert isinstance(docs, list)
    assert len(docs) > 0
    for doc in docs:
        assert "query" in doc
        assert "content" in doc
        assert "source" in doc