import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model_name="gpt-4",
    temperature=0.2,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

prompt_template = """
You are a research assistant. Given the following documents retrieved by a web search:

{documents}

Decide if the documents sufficiently answer the user's question: "{question}"

If yes, respond with JSON exactly like:
{{"need_more": false, "new_queries": []}}

If no, respond with JSON exactly like:
{{"need_more": true, "new_queries": ["refined query 1", "refined query 2", ...]}}

Return only valid JSON.
"""

prompt = PromptTemplate.from_template(prompt_template)

def reflect(question: str, documents: list):
    docs_text = "\n\n".join([f"- {doc['content']}" for doc in documents])
    input_vars = {"question": question, "documents": docs_text}
    response = llm.invoke(prompt.format(**input_vars))
    import json
    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        # Basic fallback if JSON invalid
        return {"need_more": False, "new_queries": []}