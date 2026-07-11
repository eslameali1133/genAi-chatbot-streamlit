# 💬 GenAI Chatbot — Bilingual (Arabic/English) Streamlit App

A fast, streaming AI chatbot built with **Streamlit**, **LangChain**, and **Groq**, featuring full Arabic/English localization with RTL support — built as a hands-on project while upskilling in Generative AI (LLM APIs, LangChain, RAG).

## ✨ Features

- 🌐 **Full Arabic & English localization** — every UI string (title, placeholders, buttons, system prompt) switches with one click
- ↔️ **RTL layout support** — chat bubbles, input, and text align correctly for Arabic
- ⚡ **Streaming responses** — tokens appear live as the model generates, instead of waiting for the full reply
- 🧠 **Model selector** — switch between `llama-3.3-70b-versatile`, `llama-3.1-8b-instant`, and `mixtral-8x7b-32768` on the fly
- 🎚️ **Adjustable creativity** — temperature slider to control response randomness
- 📊 **Live message counter** in the sidebar
- 🗑️ **Clear chat** — reset the conversation instantly
- ⬇️ **Export chat as JSON** — download the full conversation with a timestamp
- 📄 **Export chat as PDF** — download a formatted PDF transcript of the conversation
- 🛡️ **Graceful error handling** — API failures show inline instead of crashing the app
- 🧩 **Modular localization** — all translations live in `translations.py`, so adding a new language means editing one file, not the app logic

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/) — UI framework
- [LangChain](https://www.langchain.com/) (`langchain-groq`) — LLM orchestration
- [Groq](https://groq.com/) — fast LLM inference (Llama 3.3, Mixtral)
- [python-dotenv](https://pypi.org/project/python-dotenv/) — environment variable management
- [ReportLab](https://www.reportlab.com/) — PDF generation

## 📁 Project Structure

```
chat_bot_with_streamlit/
├── app.py              # Main Streamlit app — UI, chat logic, streaming
├── translations.py     # All localized strings (English & Arabic)
├── .env                # GROQ_API_KEY (not committed)
├── requirements.txt    # Python dependencies
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/eslameali1133/genAi-chatbot-streamlit.git
cd genAi-chatbot-streamlit
```

### 2. Create a virtual environment & install dependencies
```bash
python -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Add your Groq API key
Create a `.env` file in the project root:
```
GROQ_API_KEY=your_api_key_here
```
Get a free key at [console.groq.com](https://console.groq.com/).

### 4. Run the app
```bash
streamlit run app.py
```

## 🌍 Adding a New Language

Open `translations.py` and add a new key to the `TRANSLATIONS` dict with the same set of fields as `"en"` / `"ar"`. No changes needed in `app.py`.

## 🗺️ Roadmap

- [ ] RAG mode — chat with uploaded Arabic/English PDFs
- [ ] Voice input/output (Arabic speech-to-text via Groq Whisper)
- [ ] Persistent chat history (SQLite)
- [ ] Egyptian dialect (عامية) toggle
- [ ] Token/cost usage tracking
- [ ] Side-by-side model comparison mode
- [ ] Proper Arabic font support in PDF export (Amiri + arabic-reshaper + python-bidi)

## 📄 License

MIT

## 👤 Author

**Eslam Ali** —  AI Enginner & Mobile Tech Lead
[LinkedIn]([https://www.linkedin.com/](https://www.linkedin.com/in/eslam-ali-064bb7120/)) · [GitHub](https://github.com/eslameali1133)
