import os
from serpapi import GoogleSearch
from dotenv import load_dotenv
from typing import List, Dict

load_dotenv()

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

def retrieve_documents(queries: List[str]) -> List[Dict[str, str]]:
    results = []
    for query in queries:
        params = {
            "engine": "google",
            "q": query,
            "api_key": SERPAPI_API_KEY,
            "num": 3  # number of results per query
        }
        search = GoogleSearch(params)
        search_results = search.get_dict()

        # Extract snippet/description from top results
        for organic_result in search_results.get("organic_results", [])[:3]:
            snippet = organic_result.get("snippet", "")
            link = organic_result.get("link", "")
            results.append({
                "query": query,
                "content": snippet,
                "source": link
            })
    return results

# Test run
if __name__ == "__main__":
    test_queries = ["2022 FIFA World Cup winner", "final match result"]
    docs = retrieve_documents(test_queries)
    for doc in docs:
        print(f"Query: {doc['query']}\nSource: {doc['source']}\nContent: {doc['content']}\n")