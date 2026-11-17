import datetime
import streamlit as st
from google import genai

# Setup client
client = genai.Client(api_key="AIzaSyA94b7VQI_kKdXVfPH7QvWahUlnUd7e6lQ")

# List of zodiac signs
zodiac_signs = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

zodiac_data = {
    "Aries": {"emoji": "♈", "element": "Fire", "modality": "Cardinal", "planet": "Mars", "lucky_color": "Red", "lucky_number": "9", "power_phrase": "I lead with fearless energy.", "daily_vibe": "Bold action creates momentum today."},
    "Taurus": {"emoji": "♉", "element": "Earth", "modality": "Fixed", "planet": "Venus", "lucky_color": "Green", "lucky_number": "6", "power_phrase": "I build comfort with patience.", "daily_vibe": "A steady approach brings beauty and reward."},
    "Gemini": {"emoji": "♊", "element": "Air", "modality": "Mutable", "planet": "Mercury", "lucky_color": "Yellow", "lucky_number": "5", "power_phrase": "I connect ideas with curiosity.", "daily_vibe": "Conversation opens new possibilities."},
    "Cancer": {"emoji": "♋", "element": "Water", "modality": "Cardinal", "planet": "Moon", "lucky_color": "Silver", "lucky_number": "2", "power_phrase": "I nurture with intuition.", "daily_vibe": "Emotional clarity leads the way."},
    "Leo": {"emoji": "♌", "element": "Fire", "modality": "Fixed", "planet": "Sun", "lucky_color": "Gold", "lucky_number": "1", "power_phrase": "I shine with confidence.", "daily_vibe": "Your charisma attracts positive attention."},
    "Virgo": {"emoji": "♍", "element": "Earth", "modality": "Mutable", "planet": "Mercury", "lucky_color": "Navy", "lucky_number": "5", "power_phrase": "I organize with focus.", "daily_vibe": "Small improvements lead to big wins."},
    "Libra": {"emoji": "♎", "element": "Air", "modality": "Cardinal", "planet": "Venus", "lucky_color": "Blue", "lucky_number": "7", "power_phrase": "I balance beauty and kindness.", "daily_vibe": "Harmony and connection feel strong."},
    "Scorpio": {"emoji": "♏", "element": "Water", "modality": "Fixed", "planet": "Pluto", "lucky_color": "Black", "lucky_number": "8", "power_phrase": "I transform with depth.", "daily_vibe": "Your intuition reveals hidden power."},
    "Sagittarius": {"emoji": "♐", "element": "Fire", "modality": "Mutable", "planet": "Jupiter", "lucky_color": "Purple", "lucky_number": "3", "power_phrase": "I explore with optimism.", "daily_vibe": "Adventure and growth are aligned."},
    "Capricorn": {"emoji": "♑", "element": "Earth", "modality": "Cardinal", "planet": "Saturn", "lucky_color": "Brown", "lucky_number": "4", "power_phrase": "I achieve with discipline.", "daily_vibe": "Steady progress wins the day."},
    "Aquarius": {"emoji": "♒", "element": "Air", "modality": "Fixed", "planet": "Uranus", "lucky_color": "Teal", "lucky_number": "11", "power_phrase": "I innovate with vision.", "daily_vibe": "Your ideas can inspire others."},
    "Pisces": {"emoji": "♓", "element": "Water", "modality": "Mutable", "planet": "Neptune", "lucky_color": "Sea green", "lucky_number": "7", "power_phrase": "I dream with compassion.", "daily_vibe": "Creativity flows through your day."}
}

# Theme options are shown in the left panel instead of the sidebar.
current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")

# Styling for modes will be applied after the theme selector is rendered.

# Logo and header
logo_html = """
<div style='display:flex; align-items:center; gap:18px; margin-bottom:24px;'>
    <div style='width:80px; height:80px; border-radius:50%; background: radial-gradient(circle at 30% 30%, #facc15, #fb7185 45%, #60a5fa 100%); display:flex; align-items:center; justify-content:center; box-shadow: 0 0 20px rgba(252, 197, 21, 0.35);'>
        <span style='font-size:34px; color:#111827; font-weight:800;'>✨</span>
    </div>
    <div>
        <h1 style='margin:0; font-size:2.2rem; letter-spacing:0.02em;'>Astrology Chatbot</h1>
        <p style='margin:6px 0 0; color:#94a3b8;'>Personalized astrology insight for your name, birthdate, and sign.</p>
    </div>
</div>
"""
st.markdown(logo_html, unsafe_allow_html=True)

# User inputs - Left and Center Layout
col1, col_main = st.columns([1, 2])

with col1:
    st.markdown("<p style='font-weight:700; font-size:1.1rem; margin-bottom:12px;'>Your Details</p>", unsafe_allow_html=True)
    name = st.text_input("Enter your name:")
    birthdate = st.date_input(
        "Enter your birthdate:",
        value=datetime.date.today(),
        min_value=datetime.date(1900, 1, 1),
        max_value=datetime.date.today(),
    )
    zodiac = st.selectbox("Select your zodiac sign:", zodiac_signs)

with col_main:
    st.markdown(f"<div class='section-title'>Today: {current_date}</div>", unsafe_allow_html=True)
    
    # Zodiac card in center
    sign_info = zodiac_data.get(zodiac, {})
    st.markdown(
        f"""
        <div class='wow-card'>
            <div style='display:flex; align-items:center; justify-content:space-between; gap:12px;'>
                <div>
                    <div style='font-size:3rem; line-height:1;'>{sign_info.get('emoji', '✨')}</div>
                </div>
                <div style='text-align:right;'>
                    <h2 style='margin:0; font-size:1.8rem;'>{zodiac}</h2>
                    <div style='color: #94a3b8; margin-top:4px;'>{sign_info.get('element')} • {sign_info.get('modality')} • {sign_info.get('planet')}</div>
                </div>
            </div>
            <div class='sign-summary'>
                <p style='margin:0 0 10px;'><strong>Lucky Color:</strong> {sign_info.get('lucky_color')} &nbsp; • &nbsp; <strong>Lucky Number:</strong> {sign_info.get('lucky_number')}</p>
                <p style='margin:0 0 10px;'><strong>Power Phrase:</strong> {sign_info.get('power_phrase')}</p>
                <p style='margin:0; color: #cbd5e1;'><strong>Daily Vibe:</strong> {sign_info.get('daily_vibe')}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Question input in center
    user_question = st.text_input("Ask your astrology question:")
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        insight_clicked = st.button("Get Astrological Insight", use_container_width=True)
    with col_btn2:
        overview_clicked = st.button("Show Sign Overview", use_container_width=True)

# Apply dark mode styling - kept at top for early application
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"], .stApp, .main, .block-container, [data-testid="stSidebar"], [data-testid="stToolbar"] {
        background-color: #0f172a !important;
        color: #e2e8f0 !important;
    }
    .css-1d391kg, .css-ffhzg2, .css-18e3th9, .css-1lcbmhc {
        background-color: #0f172a !important;
        color: #e2e8f0 !important;
    }
    .stButton>button {
        background-color: #475569 !important;
        color: #f8fafc !important;
        border: 1px solid #64748b !important;
    }
    input, textarea, select, .stSelectbox>div>div, .stDateInput>div>div {
        background-color: #1e293b !important;
        color: #e2e8f0 !important;
        border: 1px solid #334155 !important;
    }
    .stSelectbox>div>div>div, .stSelectbox>div>div>div>div, .stDateInput>div>div>div {
        background-color: #1e293b !important;
        color: #e2e8f0 !important;
    }
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] div,
    [data-testid="stSidebar"] .stMarkdown,
    [data-testid="stSidebar"] .stText,
    [data-testid="stSidebar"] .stHeader,
    [data-testid="stSidebar"] .stCaption,
    label, .stTextInput>label, .stSelectbox>label, .stDateInput>label, .stRadio>label, .stCheckbox>label, .streamlit-expanderHeader, .css-1xarl3l {
        color: #e2e8f0 !important;
    }
    ::placeholder {
        color: #cbd5e1 !important;
        opacity: 1 !important;
    }
    .stSelectbox>div>div, .stMultiSelect>div>div, .stRadio>div, .stCheckbox>div {
        color: #e2e8f0 !important;
    }
    .css-1n76uvr, .css-1q8dd3e, .css-10trblm, .css-16zrtkt {
        color: #e2e8f0 !important;
    }
    .wow-card {
        border-radius: 28px;
        background: linear-gradient(180deg, rgba(15,23,42,0.95), rgba(30,41,59,0.95));
        border: 1px solid rgba(148,163,184,0.18);
        box-shadow: 0 18px 50px rgba(15,23,42,0.45);
        padding: 24px;
    }
    .section-title {
        font-size: 26px;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 12px;
    }
    .star-tag {
        display: inline-block;
        padding: 8px 14px;
        border-radius: 999px;
        background: rgba(148,163,184,0.18);
        color: #e2e8f0;
        font-size: 0.95rem;
        margin-right: 8px;
    }
    .sign-summary {
        margin-top: 18px;
        padding: 18px;
        border-radius: 18px;
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(148,163,184,0.12);
    }
    </style>
    """,
    unsafe_allow_html=True,
)



if insight_clicked:
    if not name.strip():
        st.warning("Please enter your name.")
    elif not user_question.strip():
        st.warning("Please enter a question.")
    else:
        try:
            try:
                birthdate_text = birthdate.strftime('%B %d, %Y')
            except Exception:
                st.warning("Please choose a valid birthdate.")
            else:
                prompt = (
                    f"As a knowledgeable astrologer, provide insightful advice or information based on astrology "
                    f"for {name.strip()}, who was born on {birthdate_text} and has the {zodiac} zodiac sign. "
                    f"Question: {user_question}"
                )

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                )

                st.markdown("<div class='wow-card' style='margin-top:24px;'><strong style='color:#fbbf24;'>✨ Astrological Insight for " + name.strip() + ":</strong>", unsafe_allow_html=True)
                st.markdown(f"<p style='color:#e2e8f0;'>{response.text}</p></div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"❌ Error generating response: {e}")

if overview_clicked:
    st.markdown(
        f"""
        <div class='wow-card' style='margin-top:24px;'>
            <h3 style='margin-top:0; color:#fbbf24;'>✨ Instant Zodiac Overview</h3>
            <div class='star-tag'>Element: {sign_info.get('element')}</div>
            <div class='star-tag'>Modality: {sign_info.get('modality')}</div>
            <div class='star-tag'>Ruling Planet: {sign_info.get('planet')}</div>
            <div style='margin-top:18px; color: #94a3b8;'>This sign is driven by strong cosmic themes today. Use your lucky color and power phrase to stay aligned with your higher self.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


