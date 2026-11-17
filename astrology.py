import streamlit as st
from google import genai
import datetime

# Configure the Streamlit page
st.set_page_config(page_title="Cosmic Guide ✨", page_icon="🔮", layout="centered")

# Custom CSS for a Colorful Cosmic & Mystical Theme
st.markdown("""
    <style>
    /* Main Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        color: #f3e5f5;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a103c 0%, #2d1458 100%);
        border-right: 1px solid #ffd70044;
    }
    
    /* Headers & Titles */
    h1 {
        color: #ffd700 !important;
        text-shadow: 0px 0px 12px rgba(255, 215, 0, 0.5);
        font-family: 'Georgia', serif;
    }
    h2, h3 {
        color: #e0aaff !important;
    }
    
    /* Chat Message Containers */
    [data-testid="stChatMessage"] {
        background-color: rgba(255, 255, 255, 0.07);
        border: 1px solid rgba(224, 170, 255, 0.25);
        border-radius: 15px;
        padding: 12px;
        margin-bottom: 10px;
    }
    
    /* Input Fields & Labels */
    .stTextInput label, .stDateInput label, .stTimeInput label, .stSelectbox label {
        color: #ffd700 !important;
        font-weight: bold;
    }
    
    /* Divider Styling */
    hr {
        border-color: rgba(255, 215, 0, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

st.title("✨ Astrology Chatbot ✨")
st.markdown("🔮 Ask me anything about your zodiac sign, horoscopes, or cosmic destiny!")

# Sidebar for API Key, Personal Details & Clear Button at the bottom
with st.sidebar:
    st.header("🔑 API Configuration")
    api_key = st.text_input(
        "Enter your Gemini API Key", 
        type="password", 
        placeholder="AIzaSy...",
        help="Paste your Google Gemini API key here. You can replace it anytime if your quota runs out."
    )
        
    st.divider()
    
    st.header("🌌 Your Cosmic Blueprint")
    st.markdown("Enter your details for personalized readings:")
    user_name = st.text_input("Name", placeholder="E.g., Luna")
    birth_date = st.date_input(
        "Date of Birth", 
        value=None, 
        min_value=datetime.date(1900, 1, 1), 
        max_value=datetime.date.today()
    )
    birth_time = st.time_input("Time of Birth", value=None)
    birth_location = st.text_input("Place of Birth", placeholder="City, Country")
    zodiac_sign = st.selectbox(
        "Sun Sign (Optional)", 
        options=["", "Aries ♈", "Taurus ♉", "Gemini ♊", "Cancer ♋", "Leo ♌", 
                 "Virgo ♍", "Libra ♎", "Scorpio ♏", "Sagittarius ♐", 
                 "Capricorn ♑", "Aquarius ♒", "Pisces ♓"],
        help="Select your Sun Sign if you know it. Otherwise, leave it blank."
    )
    
    # Placing Clear History neatly at the bottom of the sidebar
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    avatar = "🌟" if message["role"] == "user" else "🔮"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is your astrological question?"):
    # Check if API key is entered
    if not api_key:
        st.warning("⚠️ Please enter your Gemini API Key in the sidebar first to connect with the cosmos!")
        st.stop()

    # Display user message in chat message container
    st.chat_message("user", avatar="🌟").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # System prompt enforcing short 10-point format
    system_prompt = (
        "You are a mystical, wise, and knowledgeable astrologer. Answer the user's questions about astrology, "
        "zodiac signs, horoscopes, and cosmic events.\n"
        "STRICT FORMATTING RULE: Do NOT write long paragraphs. Always give your entire answer in EXACTLY 10 short, "
        "easy-to-understand bullet points (1 to 10). Keep each point crisp, clear, and concise (1-2 lines max per point) "
        "with relevant emojis.\n"
    )
    
    # Add personal details to the system prompt if provided
    user_context = []
    if user_name: user_context.append(f"Name: {user_name}")
    if birth_date: user_context.append(f"Date of Birth: {birth_date.strftime('%B %d, %Y')}")
    if birth_time: user_context.append(f"Time of Birth: {birth_time.strftime('%I:%M %p')}")
    if birth_location: user_context.append(f"Place of Birth: {birth_location}")
    if zodiac_sign: user_context.append(f"Sun Sign: {zodiac_sign}")
    
    if user_context:
        system_prompt += "\nThe user has provided the following personal details:\n"
        system_prompt += "\n".join(user_context)
        system_prompt += "\n\nPersonalize the 10 points based on these birth details.\n\n"
    else:
        system_prompt += "\n\n"

    conversation_text = system_prompt
    for msg in st.session_state.messages:
        role_name = "User" if msg["role"] == "user" else "Astrologer"
        conversation_text += f"{role_name}: {msg['content']}\n"
    
    conversation_text += "Astrologer: "

    with st.chat_message("assistant", avatar="🔮"):
        message_placeholder = st.empty()
        
        try:
            # Initialize client dynamically using the API key from the sidebar
            client = genai.Client(api_key=api_key.strip())
            
            with st.spinner("Reading the stars..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash", 
                    contents=conversation_text
                )
            response_text = response.text
            message_placeholder.markdown(response_text)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response_text})
        except Exception as e:
            st.error(f"🌠 Cosmic connection failed (Check your API Key or Quota): {e}")