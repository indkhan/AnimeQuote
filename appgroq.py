import streamlit as st
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
# Set up Groq client - use environment variable for API key
client = Groq()

def get_anime_quote(feeling):
    # Prompt for Groq to generate a relevant anime quote
    prompt = f"""
    Generate an uplifting or inspiring quote from an anime or manga character 
    that relates to the feeling: "{feeling}". 
    Format the response as: "Quote" \n    ~~Character [Anime/Manga Name]
    DO NOT PUT ANYTHING OTHER THEN THE FORMAT IN THE RESPONSE
    """
    
    # Make API call to Groq
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="mixtral-8x7b-32768",  # Or another appropriate model
        max_tokens=200,
    )
    
    # Extract and return the generated quote
    return chat_completion.choices[0].message.content

# Streamlit UI
st.title("Anime Quote Generator")

feeling = st.text_input("How are you feeling?")

if feeling:
    if st.button("Get Quote"):
        with st.spinner("Generating quote..."):
            try:
                quote = get_anime_quote(feeling)
                st.success("Here's a quote for you:")
                st.write(quote)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

st.sidebar.write("This app uses Groq to generate anime quotes based on your feelings.")