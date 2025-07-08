import os
from openai import OpenAI
from dotenv import load_dotenv
from typing import List, Dict

load_dotenv()

client = OpenAI(
    api_key=os.getenv("TOGETHER_API_KEY"),
    base_url="https://api.together.xyz/v1"
)

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"

def summarize_findings(docs: List[Dict[str, str]]) -> Dict:
    context = "\n\n".join([f"{i+1}. {doc['content']} (Source: {doc['source']})"
                           for i, doc in enumerate(docs)])

    prompt = f"""
You are a research assistant. Read the information below and generate a structured summary.

Information:
{context}

Return a JSON object with the following structure:
{{
  "summary": "...",
  "key_points": ["...", "..."],
  "sources": ["..."]
}}
Only return the JSON. Do not include any explanations.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )

    content = response.choices[0].message.content.strip()

    try:
        return eval(content)  # or use json.loads() with a fallback
    except Exception:
        print("⚠️ Failed to parse summary as JSON:")
        print(content)
        return {}
        
# Test run
if __name__ == "__main__":
    test_docs = [
        {
            "query": "2022 FIFA World Cup winner",
            "content": "Argentina won the 2022 FIFA World Cup, defeating France in a dramatic final match that ended 3-3 and went to penalties.",
            "source": "https://www.fifa.com/worldcup/news"
        },
        {
            "query": "final match result",
            "content": "The final score was 3-3, and Argentina won 4-2 in a penalty shootout.",
            "source": "https://www.bbc.com/sport/football"
        }
    ]

    result = summarize_findings(test_docs)
    print(result)