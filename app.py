import time
import random
from datetime import date, datetime

import streamlit as st
from PIL import Image


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="A Little Birthday Surprise",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# Custom CSS
# =========================================================

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
        max-width: 1400px;
    }

    .hero-box {
        background: linear-gradient(135deg, #fff1f2 0%, #ffe4e6 35%, #fdf2f8 100%);
        border-radius: 28px;
        padding: 2.2rem;
        border: 1px solid rgba(244, 114, 182, 0.25);
        box-shadow: 0 18px 50px rgba(244, 114, 182, 0.18);
        margin-bottom: 1.2rem;
    }

    .hero-title {
        font-size: 3rem;
        font-weight: 900;
        color: #9f1239;
        line-height: 1.1;
        margin-bottom: 0.5rem;
    }

    .hero-subtitle {
        font-size: 1.15rem;
        color: #831843;
        line-height: 1.6;
        max-width: 900px;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.78);
        border-radius: 24px;
        padding: 1.3rem;
        border: 1px solid rgba(244, 114, 182, 0.22);
        box-shadow: 0 14px 35px rgba(100, 116, 139, 0.12);
        height: 100%;
    }

    .section-title {
        font-size: 1.35rem;
        font-weight: 800;
        color: #9f1239;
        margin-bottom: 0.7rem;
    }

    .small-note {
        color: #64748b;
        font-size: 0.95rem;
        line-height: 1.5;
    }

    .cute-badge {
        display: inline-block;
        background: #ffe4e6;
        color: #9f1239;
        padding: 0.35rem 0.75rem;
        border-radius: 999px;
        font-size: 0.88rem;
        font-weight: 700;
        margin: 0.25rem 0.25rem 0.25rem 0;
    }

    .wish-card {
        background: linear-gradient(135deg, #ffffff, #fff1f2);
        border-radius: 24px;
        padding: 1.4rem;
        border: 1px solid rgba(225, 29, 72, 0.18);
        box-shadow: 0 12px 28px rgba(225, 29, 72, 0.09);
        margin-bottom: 1rem;
    }

    .wish-text {
        font-size: 1.1rem;
        color: #881337;
        line-height: 1.65;
        font-weight: 500;
    }

    .memory-card {
        background: #ffffff;
        border-left: 6px solid #fb7185;
        border-radius: 18px;
        padding: 1rem 1.1rem;
        box-shadow: 0 8px 20px rgba(15, 23, 42, 0.08);
        margin-bottom: 0.85rem;
    }

    .memory-title {
        font-size: 1.05rem;
        font-weight: 800;
        color: #9f1239;
    }

    .memory-body {
        color: #475569;
        line-height: 1.55;
        margin-top: 0.3rem;
    }

    .footer-note {
        text-align: center;
        padding: 1rem;
        color: #831843;
        font-weight: 700;
    }

    div.stButton > button {
        border-radius: 14px;
        border: 0;
        background: linear-gradient(135deg, #fb7185, #db2777);
        color: white;
        font-weight: 800;
        padding: 0.65rem 1.1rem;
        box-shadow: 0 8px 18px rgba(219, 39, 119, 0.25);
    }

    div.stButton > button:hover {
        border: 0;
        color: white;
        transform: translateY(-1px);
    }

    .floating-hearts {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        pointer-events: none;
        z-index: 999999;
    }

    .heart {
        position: absolute;
        animation: floatHeart 8s linear infinite;
        color: rgba(244, 63, 94, 0.45);
        font-size: 24px;
    }

    .heart:nth-child(1) { left: 8%; animation-delay: 0s; }
    .heart:nth-child(2) { left: 22%; animation-delay: 1.5s; }
    .heart:nth-child(3) { left: 45%; animation-delay: 3s; }
    .heart:nth-child(4) { left: 68%; animation-delay: 2s; }
    .heart:nth-child(5) { left: 84%; animation-delay: 4s; }

    @keyframes floatHeart {
        0% {
            transform: translateY(100vh) scale(0.7);
            opacity: 0;
        }
        20% {
            opacity: 1;
        }
        100% {
            transform: translateY(-10vh) scale(1.25);
            opacity: 0;
        }
    }
    </style>

    <div class="floating-hearts">
        <div class="heart">💗</div>
        <div class="heart">🎈</div>
        <div class="heart">✨</div>
        <div class="heart">🎂</div>
        <div class="heart">💝</div>
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# Editable Content
# =========================================================

DEFAULT_NAME = "Someone Special"

DEFAULT_FINAL_MESSAGE = """
Happy Birthday to one of the most special people in my life.

May this new year bring you more peace, more smiles, more confidence, 
and more beautiful moments than you can even imagine. You deserve kindness, 
success, laughter, and every little thing that makes your heart feel light.

This tiny website is just a small way to say: you matter, your presence is special, 
and today is worth celebrating beautifully.
"""

MEMORIES = [
    {
        "title": "The Smile Memory",
        "body": "Some people make ordinary moments feel brighter. Your smile is one of those little things that can change the mood of a whole day.",
    },
    {
        "title": "The Kindness Memory",
        "body": "The way you care, listen, and stay thoughtful makes you different in the best possible way.",
    },
    {
        "title": "The Favorite Person Energy",
        "body": "You have a calm, warm, and rare kind of presence. That is something worth celebrating today.",
    },
]

REASONS = [
    "You make simple moments feel meaningful.",
    "You have a heart that deserves good things.",
    "Your presence makes people feel comfortable.",
    "You are thoughtful in ways that matter.",
    "You deserve a birthday full of smiles.",
    "You are special without even trying too hard.",
]

SURPRISE_MESSAGES = [
    "Today’s forecast: 100% chance of cake, smiles, and cute surprises.",
    "Birthday scan completed: Specialness level is extremely high.",
    "Warning: Too much birthday charm detected.",
    "System result: This person deserves the happiest day.",
    "Happiness mode activated successfully.",
]


# =========================================================
# Helper Functions
# =========================================================

def days_until_birthday(birthday_date: date) -> int:
    today = date.today()
    this_year_birthday = birthday_date.replace(year=today.year)

    if this_year_birthday < today:
        this_year_birthday = birthday_date.replace(year=today.year + 1)

    return (this_year_birthday - today).days


def show_metric_progress(label: str, value: int, emoji: str):
    st.markdown(f"**{emoji} {label}**")
    st.progress(value)
    st.caption(f"{value}%")


def birthday_scan():
    scan_text = st.empty()
    progress = st.progress(0)

    steps = [
        "Checking smile frequency...",
        "Measuring birthday glow...",
        "Detecting cute energy...",
        "Calculating specialness score...",
        "Preparing surprise result...",
    ]

    for i in range(101):
        progress.progress(i)
        scan_text.write(random.choice(steps))
        time.sleep(0.012)

    scan_text.success("Birthday scan completed successfully 🎉")


# =========================================================
# Sidebar Personalization
# =========================================================

with st.sidebar:
    st.header("Customize Website")

    person_name = st.text_input(
        "Birthday person's name",
        value=DEFAULT_NAME,
    )

    birthday_date = st.date_input(
        "Birthday date",
        value=date(date.today().year, 8, 15),
    )

    relation_label = st.selectbox(
        "Tone",
        [
            "Sweet and cute",
            "Friendly and warm",
            "Funny and playful",
            "Soft and emotional",
        ],
    )

    st.caption("You can edit the messages inside the Python code to make it more personal.")


# =========================================================
# Hero Section
# =========================================================

st.markdown(
    f"""
    <div class="hero-box">
        <div class="hero-title">🎂 Happy Birthday, {person_name}!</div>
        <div class="hero-subtitle">
            A small birthday website made with smiles, surprises, memories, and a little bit of magic.
            No machine learning model here — only real-time cuteness, interactive wishes, and birthday happiness.
        </div>
        <br>
        <span class="cute-badge">🎈 Streamlit Birthday System</span>
        <span class="cute-badge">💝 Surprise Generator</span>
        <span class="cute-badge">✨ Memory Album</span>
        <span class="cute-badge">🎁 Virtual Gift Box</span>
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# Tabs
# =========================================================

tab_home, tab_memory, tab_surprise, tab_wish, tab_final = st.tabs(
    [
        "🏠 Birthday Home",
        "📸 Memory Album",
        "🎁 Surprise Box",
        "💌 Wish Generator",
        "🌙 Final Message",
    ]
)


# =========================================================
# Tab 1: Birthday Home
# =========================================================

with tab_home:
    left_col, right_col = st.columns([1.05, 1], gap="large")

    with left_col:
        st.markdown(
            """
            <div class="glass-card">
                <div class="section-title">📸 Upload a Favorite Picture</div>
                <div class="small-note">
                    This works like the image upload section of a disease detection app, 
                    but here the image is used only for a cute birthday preview.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        uploaded_file = st.file_uploader(
            "Upload a photo or memory image",
            type=["jpg", "jpeg", "png"],
        )

        if uploaded_file is not None:
            image = Image.open(uploaded_file).convert("RGB")
            st.image(
                image,
                caption=f"A beautiful memory for {person_name}",
                use_container_width=True,
            )
        else:
            st.info("Upload a photo to make the page more personal.")

    with right_col:
        st.markdown(
            """
            <div class="glass-card">
                <div class="section-title">🔍 Real-Time Birthday Happiness Scan</div>
                <div class="small-note">
                    This is a playful replacement for the model prediction panel.
                    Instead of disease classes, the system shows birthday happiness indicators.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("Start Birthday Scan"):
            birthday_scan()
            st.balloons()

        st.markdown("### Birthday Result")

        show_metric_progress("Smile Probability", 100, "😊")
        show_metric_progress("Specialness Score", 99, "💖")
        show_metric_progress("Birthday Vibe Level", 98, "🎉")

        st.success(random.choice(SURPRISE_MESSAGES))

    st.divider()

    d_left, d_right, d_third = st.columns(3)

    remaining_days = days_until_birthday(birthday_date)

    with d_left:
        st.metric("Days Until Birthday", remaining_days)

    with d_right:
        st.metric("Birthday Mode", "Activated")

    with d_third:
        st.metric("Cute Energy", "100%")


# =========================================================
# Tab 2: Memory Album
# =========================================================

with tab_memory:
    st.markdown("## 📸 Memory Album")

    st.write(
        "This section can be edited with real memories, small stories, inside jokes, "
        "or meaningful moments."
    )

    for memory in MEMORIES:
        st.markdown(
            f"""
            <div class="memory-card">
                <div class="memory-title">💗 {memory["title"]}</div>
                <div class="memory-body">{memory["body"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### Add a New Memory")

    new_memory = st.text_area(
        "Write a short memory here",
        placeholder="Example: That day when we laughed so much over something so small...",
    )

    if st.button("Save Memory for This Session"):
        if new_memory.strip():
            st.success("Memory added for this session 💝")
            st.markdown(
                f"""
                <div class="memory-card">
                    <div class="memory-title">✨ New Memory</div>
                    <div class="memory-body">{new_memory}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.warning("Please write a memory first.")


# =========================================================
# Tab 3: Surprise Box
# =========================================================

with tab_surprise:
    st.markdown("## 🎁 Virtual Surprise Box")

    st.write(
        "Click the button to open a random birthday surprise. "
        "This makes the website feel interactive and personal."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Open Gift Box 1 🎁"):
            st.success("Gift unlocked: A day full of smiles and peace.")

    with col2:
        if st.button("Open Gift Box 2 💝"):
            st.success("Gift unlocked: A reminder that you are deeply appreciated.")

    with col3:
        if st.button("Open Gift Box 3 ✨"):
            st.success("Gift unlocked: A future full of beautiful moments.")

    st.divider()

    st.markdown("### 🎲 Random Reason Generator")

    if st.button("Tell Him Why He Is Special"):
        st.info(random.choice(REASONS))


# =========================================================
# Tab 4: Wish Generator
# =========================================================

with tab_wish:
    st.markdown("## 💌 Personalized Birthday Wish Generator")

    st.write(
        "Choose a tone and generate a short birthday wish. "
        "You can copy it and use it in the final message."
    )

    wish_style = st.radio(
        "Select wish style",
        [
            "Cute",
            "Emotional",
            "Funny",
            "Simple",
        ],
        horizontal=True,
    )

    wishes = {
        "Cute": f"Happy Birthday, {person_name}! May your day be as sweet as cake, as bright as candles, and as special as you are.",
        "Emotional": f"Happy Birthday, {person_name}. I hope this year brings you peace, confidence, happiness, and everything your heart quietly wishes for.",
        "Funny": f"Happy Birthday, {person_name}! Congratulations on becoming older, wiser, and still somehow cute enough to get a whole website.",
        "Simple": f"Happy Birthday, {person_name}. Wishing you a beautiful day and a year filled with happiness, success, and good memories.",
    }

    if st.button("Generate Wish"):
        st.markdown(
            f"""
            <div class="wish-card">
                <div class="wish-text">{wishes[wish_style]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.balloons()

    st.divider()

    st.markdown("### Write Your Own Wish")

    custom_wish = st.text_area(
        "Your message",
        value=f"Happy Birthday, {person_name}! You are truly special, and I hope this day makes you feel appreciated, happy, and celebrated.",
        height=160,
    )

    if st.button("Preview My Wish"):
        st.markdown(
            f"""
            <div class="wish-card">
                <div class="wish-text">{custom_wish}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# =========================================================
# Tab 5: Final Message
# =========================================================

with tab_final:
    st.markdown("## 🌙 Final Birthday Message")

    st.markdown(
        f"""
        <div class="wish-card">
            <div class="wish-text">
                {DEFAULT_FINAL_MESSAGE.replace("Happy Birthday", f"Happy Birthday, {person_name}")}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Final Surprise")

    if st.button("Click for Final Surprise 🎉"):
        st.balloons()
        st.success(f"Happy Birthday, {person_name}! This whole little website was made just to make you smile.")

    st.markdown(
        """
        <div class="footer-note">
            Made with Streamlit, birthday magic, and a lot of care 🎂✨
        </div>
        """,
        unsafe_allow_html=True,
    )
