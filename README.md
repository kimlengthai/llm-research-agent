# LLM Research Agent

A command-line research assistant agent that accepts a natural language question, generates search queries, retrieves documents, reflects on their sufficiency, and synthesizes a concise answer with citations in JSON format.

---

## ✨ Features

* **Query Generation:** Leverages Together.ai's Mistral model to break down user questions into 3–5 targeted search queries.
* **Document Retrieval:** Fetches web documents for the generated queries (currently a placeholder/mock implementation).
* **Reflection:** Includes a Reflect node that analyzes retrieved documents to determine if additional queries or search cycles are needed (supports up to 2 iterations).
* **Summarization:** Synthesizes findings into a concise English answer with Markdown-style citations.
* **Pipeline Orchestration:** Manages the entire research flow sequentially, including up to two search-reflect cycles.
* **Testing:** Comprehensive unit tests cover key nodes and pipeline stages.
* **Together.ai Integration:** Configured to use the Together.ai API for LLM interactions, with API keys managed via environment variables.
* **CLI Interface:** Easily run the agent from your terminal with a single command.

---

## 🚀 Project Structure

llm-research-agent/
├── src/
│ └── agent/
│ └── nodes/
│ ├── generate_queries.py
│ ├── retrieve_documents.py
│ ├── reflect.py
│ └── summarize_findings.py
├── tests/
├── .env
├── requirements.txt
├── README.md
└── design_doc.md

---

## 🛠️ Setup Instructions

Follow these steps to get your LLM Research Agent up and running:

1.  **Clone the repository:**

    ```bash
    git clone <your-repo-url>
    cd llm-research-agent
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Add API Keys:** Configure your API keys for Together.ai and SerpAPI (if implementing full web search) in a `.env` file at the project root.

---

## 💡 Usage

Run the agent with your research question:

```bash
python3 -m src.agent.agent "Who won the 2022 FIFA World Cup?"

```

## 💡 Testing

pip install pytest
pytest tests/

## 🗺️ Next Steps (Planned Enhancements)

Full Web Search Integration: Implement robust web search capabilities (e.g., using SerpAPI).

Advanced Error Handling: Incorporate more sophisticated error handling and rate-limit mitigation.

Slot-aware Reflect Node: Enhance the Reflect node for improved factual completeness.

Docker Packaging: Provide Docker support for easy packaging and deployment.

Additional Features: Explore and implement further features and performance optimizations.

## Credits

Developed by Kimleng Thai as part of a take-home assignment, demonstrating prompt engineering, tool orchestration, and software engineering best practices.