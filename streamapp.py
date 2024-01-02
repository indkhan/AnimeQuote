import streamlit as st
from main import openai_response

st.title("Anime Quote")

input_text = st.text_input("Enter Your Problem/Feeling here:")

if input_text:
    response = openai_response(input_text)

    

    st.write(response)
