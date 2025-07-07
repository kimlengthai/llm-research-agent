import os
from dotenv import load_dotenv

# Use the new recommended package for ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.2,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

template = PromptTemplate.from_template(
    """Break down the following user question into 3 to 5 short English search queries.

Question: {question}

Return only a JSON list of strings."""
)

def generate_queries(question: str):
    chain = template | llm
    response = chain.invoke({"question": question})
    return eval(response.content)  # assumes output is a valid list


if __name__ == "__main__":
    result = generate_queries("Who won the 2022 FIFA World Cup?")
    print(result)