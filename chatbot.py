import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq


#load env
load_dotenv()

st.set_page_config(
    page_title="chatbot",
    page_icon="🤖",
    layout="centered"
)
st.title("💬 Genrative AI Chat bot")

# init chat history

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for mesg in st.session_state.chat_history:
    with st.chat_message(mesg["role"]):
        st.markdown(mesg["content"])
    
# llm init 
llm = ChatGroq(model="llama-3.3-70b-versatile",temperature=0.1)

user_promt = st.chat_input("Ask Ai...")

if user_promt:
    st.chat_message("user").markdown(user_promt)
    st.session_state.chat_history.append({"role":"user","content":user_promt})

    response = llm.invoke(
        input =[{"role":"system","content":"You are a helpful assistant"},* st.session_state.chat_history]
    )

    assistent_response = response.content

    st.session_state.chat_history.append({"role":"assistant","content":assistent_response})

    with st.chat_message("assistant"):
        st.markdown(assistent_response)




