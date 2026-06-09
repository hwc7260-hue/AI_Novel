# from dotenv import load_dotenv
# load_dotenv()

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

# subject = "AI"
# result = chat_model.invoke(subject + "에 대한 소설을 써줘")
# print(result.content)

import streamlit as st

st.title("소설 생성기")
subject = st.text_input("소설의 주제를 입력하세요")
st.write("소설의 주제 : " + subject)

if st.button("생성하기"):
    with st.spinner("소설을 생성하는 중입니다..."):
        result = chat_model.invoke( subject + "에 대한 소설을 써줘")
        st.write(result.content)