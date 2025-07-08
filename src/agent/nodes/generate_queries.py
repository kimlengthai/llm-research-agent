import os
import json
import re
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize Together.ai client using OpenAI SDK interface
client = OpenAI(
    api_key=os.getenv("TOGETHER_API_KEY"),
    base_url="https://api.together.xyz/v1"
)

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.1"

def generate_queries(question: str):
    prompt = f"""Break down the following user question into 3 to 5 short English search queries.

Question: {question}

Return only a JSON list of strings."""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
    )

    content = response.choices[0].message.content.strip()

    try:
        # Try parsing as JSON first
        return json.loads(content)
    except json.JSONDecodeError:
        # Fallback: parse numbered list format
        print("⚠️ Could not parse JSON. Fallback to numbered list parsing.")
        print("Response content:", content)
        queries = []
        for line in content.splitlines():
            match = re.match(r"^\d+\.\s*(.+)", line)
            if match:
                queries.append(match.group(1).strip())
        return queries

if __name__ == "__main__":
    test_question = "Who won the 2022 FIFA World Cup?"
    queries = generate_queries(test_question)
    print("Generated queries:", queries)