import os
import json
from io import BytesIO
from datetime import datetime

from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

load_dotenv()

# ---------------------------
# Localization (i18n)
# ---------------------------
from translations import get_translations

MODELS = [
    "llama-3.3-70b-versatile",
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768",
]

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

# ---------------------------
# Session state
# ---------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "lang" not in st.session_state:
    st.session_state.lang = "en"

# ---------------------------
# Sidebar (settings)
# ---------------------------
with st.sidebar:
    lang_choice = st.radio("Language / اللغة", ["English", "العربية"], horizontal=True)
    st.session_state.lang = "ar" if lang_choice == "العربية" else "en"
    t = get_translations(st.session_state.lang)

    st.header(t["settings"])
    model = st.selectbox(t["model"], MODELS)
    temperature = st.slider(t["temperature"], 0.0, 1.0, 0.1, 0.1)

    st.metric(t["messages_count"], len(st.session_state.chat_history))

    col1, col2 = st.columns(2)
    with col1:
        if st.button(t["clear_chat"], use_container_width=True):
            st.session_state.chat_history = []
            st.rerun()
    with col2:
        if st.session_state.chat_history:
            export_data = json.dumps(
                {
                    "exported_at": datetime.now().isoformat(),
                    "messages": st.session_state.chat_history,
                },
                ensure_ascii=False,
                indent=2,
            )
            st.download_button(
                t["export_chat"],
                data=export_data,
                file_name="chat_export.json",
                mime="application/json",
                use_container_width=True,
            )

    # PDF export (full width, below the buttons)
    if st.session_state.chat_history:
        try:
            from reportlab.lib.pagesizes import letter
            from reportlab.pdfgen import canvas

            buf = BytesIO()
            c = canvas.Canvas(buf, pagesize=letter)
            text = c.beginText(40, 750)
            text.setFont("Helvetica", 10)
            text.textLine(f"Exported at: {datetime.now().isoformat()}")
            text.moveCursor(0, 10)
            for msg in st.session_state.chat_history:
                role = msg.get("role", "").upper()
                for line in str(msg.get("content", "")).splitlines():
                    text.textLine(f"{role}: {line}")
                    if text.getY() < 60:  # new page when near bottom
                        c.drawText(text)
                        c.showPage()
                        text = c.beginText(40, 750)
                        text.setFont("Helvetica", 10)
                text.moveCursor(0, 6)
            c.drawText(text)
            c.showPage()
            c.save()
            pdf_bytes = buf.getvalue()
            buf.close()

            st.download_button(
                t["export_pdf"],
                data=pdf_bytes,
                file_name="chat_export.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
        except ImportError:
            st.warning("Install reportlab (pip install reportlab) to enable PDF export.")

t = get_translations(st.session_state.lang)
is_rtl = st.session_state.lang == "ar"

# ---------------------------
# RTL support for Arabic
# ---------------------------
if is_rtl:
    st.markdown(
        """
        <style>
        .stChatMessage, .stMarkdown, h1, p { direction: rtl; text-align: right; }
        .stChatInput textarea { direction: rtl; text-align: right; }
        </style>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------
# Header
# ---------------------------
st.title(t["title"])
st.caption(t["subtitle"])

if not st.session_state.chat_history:
    st.info(t["welcome"])

# ---------------------------
# Render chat history
# ---------------------------
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------------------
# LLM
# ---------------------------
llm = ChatGroq(model=model, temperature=temperature)

# ---------------------------
# Chat input + streaming response
# ---------------------------
user_prompt = st.chat_input(t["input_placeholder"])

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    messages = [
        {"role": "system", "content": t["system_prompt"]},
        *st.session_state.chat_history,
    ]

    with st.chat_message("assistant"):
        placeholder = st.empty()
        full_response = ""
        try:
            for chunk in llm.stream(messages):
                full_response += chunk.content or ""
                placeholder.markdown(full_response + "▌")
            placeholder.markdown(full_response)
        except Exception as e:
            full_response = f"⚠️ Error: {e}"
            placeholder.error(full_response)

    st.session_state.chat_history.append(
        {"role": "assistant", "content": full_response}
    )