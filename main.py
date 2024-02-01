## Integrate our code Open AI
import os
from constants import openai_key
from langchain_community.llms import OpenAI

import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

##streamlit framework

st.title("Langchain Demo with Open AI")
input_text=st.text_input("Search the topic you want")

##Open AI LLMs

llm=OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))
