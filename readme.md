# 📄 PDF Insights Analyzer — LLM-Powered PDF Q&A

An AI-powered application that lets you **interact with any PDF document** using natural language. Powered by **Groq-hosted LLMs**, semantic search with **FAISS**, and a clean **Streamlit UI** — this tool enables intelligent querying of long, unstructured documents in seconds.

## ✨ Key Features

- 🧠 **LLM-Based Q&A**: Ask questions about any PDF and get accurate, contextual answers.
- 🔍 **Semantic Search**: Uses HuggingFace embeddings + FAISS for high-relevance retrieval.
- ⚡ **Groq Integration**: Leverages `llama3` models via Groq’s blazing-fast inference API.
- 🖥️ **Interactive UI**: Simple and responsive interface built with Streamlit.
- 📚 **Source Visibility**: Trace answers back to original document chunks.

## 🛠️ Tech Stack

| Tool/Library     | Purpose                         |
|------------------|---------------------------------|
| Python 3.10+     | Core language                   |
| LangChain        | LLM chaining & retrieval        |
| HuggingFace      | Sentence embeddings             |
| FAISS            | Vector similarity search        |
| Groq API         | LLM backend (`llama3` models)   |
| Streamlit        | UI frontend                     |
| PyMuPDF          | PDF text extraction             |
| dotenv           | Environment config              |

## 📦 Setup Instructions

### 1. Clone the Repository *(or download manually)*

```bash
git clone https://github.com/Shuv13/PDF-Insights-Analyzer.git
cd pdf-insights-analyzer
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
# Activate
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama3-8b-8192
```

🔁 Check [Groq Console](https://console.groq.com) for your API key and supported models.

### 5. Running the App

```bash
streamlit run main.py
```

The app will launch in your browser at `http://localhost:8501`.

## 🧠 Example Use Cases

- 📊 Analyze business reports
- 📄 Ask questions about legal contracts
- 📚 Summarize academic papers
- 📑 Extract key info from technical specs

## 📁 Project Structure

```bash
.
├── main.py              # Streamlit interface
├── qa_chain.py          # LangChain + Groq setup
├── utils.py             # PDF text extractor
├── requirements.txt     # Dependencies
├── .env.example         # Environment variable template
└── README.md
```

## 🚀 Roadmap / Future Features

- Support for multi-PDF querying
- Chat history & conversation memory
- PDF annotation highlighting
- Drop-in model selector (Groq, OpenAI, etc.)

## 📜 License

This project is licensed under the MIT License — free for personal and commercial use.
