import gradio as gr
from main import openai_response


import streamlit as st


def main():
    st.title("Anime And Manga Quote App")

    # User input
    user_input = st.text_input("Enter the feeling or problem:")

    # Check if user has entered a word
    if user_input:
        # Reverse the word
        mangaresponse = openai_response(user_input)

        # Display the reversed word
        st.success(f"{mangaresponse}")


if __name__ == "__main__":
    main()
