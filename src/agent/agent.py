from src.agent.nodes.generate_queries import generate_queries
from src.agent.nodes.retrieve_documents import retrieve_documents
from src.agent.nodes.reflect import reflect
from src.agent.nodes.summarize_findings import summarize_findings
import sys
import json

def run_agent(question: str, max_iter=2):
    queries = generate_queries(question)
    all_docs = []
    for i in range(max_iter):
        print(f"\n🌐 Search iteration {i+1} with queries: {queries}")
        docs = retrieve_documents(queries)
        all_docs.extend(docs)

        print(f"\n🤔 Reflecting on {len(all_docs)} documents...")
        reflect_result = reflect(question, all_docs)

        need_more = reflect_result.get("need_more", False)
        new_queries = reflect_result.get("new_queries", [])

        if not need_more or not new_queries:
            break

        queries = new_queries

    print("\n🧠 Summarizing findings...")
    summary = summarize_findings(all_docs)
    return summary

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Please provide a research question.\nUsage:\n  python agent.py \"Your question here\"")
        sys.exit(1)

    question = sys.argv[1]
    result = run_agent(question)

    print("\n📦 Final Output:")
    print(json.dumps(result, indent=2))
