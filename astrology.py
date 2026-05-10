import streamlit as st
from google import genai

# Setup client
client = genai.Client(api_key="AIzaSyCSElHmYeDKEh0EF-msGmwsIN5eW35UISE")

# List of zodiac signs
zodiac_signs = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

st.title("Astrology Chatbot")

# User inputs
zodiac = st.selectbox("Select your zodiac sign:", zodiac_signs)
user_question = st.text_input("Ask your astrology question:")

if st.button("Get Astrological Insight"):
    if user_question.strip():
        try:
            # Craft the prompt
            prompt = f"As a knowledgeable astrologer, provide insightful advice or information based on astrology for someone with the {zodiac} zodiac sign. Question: {user_question}"

            # Generate content using the model
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            st.success("Astrological Insight:")
            st.write(response.text)
        except Exception as e:
            st.error(f"❌ Error generating response: {e}")
    else:
        st.warning("Please enter a question.")