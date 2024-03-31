import os
# from dotenv import load_dotenv
# load_dotenv()

# OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]


from langchain.chat_models import ChatOpenAI
from langchain.schema import(
    AIMessage,
    HumanMessage,
    SystemMessage
)

import streamlit as st

st.header('NEWS Summarization Tool')
st.subheader('Convert Your News Summary into 60 Words Only!')
openai_api = st.text_input('Enter OPENAI API Key')

news_text = st.text_input('Enter Your News Here: ')

chat_messages=[
    SystemMessage(content='You are an expert assistant with expertize in summarizing news articles'),
    HumanMessage(content=f'Please provide a short and concise summary of the following news with 60 words and also give me the title also:\n TEXT: {news_text}')
]

llm=ChatOpenAI(model_name='gpt-3.5-turbo', openai_api_key=openai_api)

st.write(llm(chat_messages).content)

