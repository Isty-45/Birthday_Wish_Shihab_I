import calendar
import random
import time
from datetime import date
from pathlib import Path

import streamlit as st


# =========================================================
# Basic Information
# =========================================================

PERSON_NAME = "Al Shihab"

BIRTHDAY_MONTH = 8
BIRTHDAY_DAY = 26

FIRST_MET_DATE = date(2021, 3, 2)
LEFT_COUNTRY_DATE = date(2022, 12, 12)

UNIVERSITY_NAME = "University of Georgia"
COUNTRY_NAME = "USA"

HOME_IMAGE_PATH = Path("assets/al_shihab.jpg")


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title=f"Happy Birthday {PERSON_NAME}",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# Helper Functions
# =========================================================

def get_next_birthday():
    today = date.today()
    birthday_this_year = date(today.year, BIRTHDAY_MONTH, BIRTHDAY_DAY)

    if birthday_this_year < today:
        return date(today.year + 1, BIRTHDAY_MONTH, BIRTHDAY_DAY)

    return birthday_this_year


def days_between(start_date, end_date=None):
    if end_date is None:
        end_date = date.today()
    return (end_date - start_date).days


def create_august_calendar_html(year):
    cal = calendar.Calendar(firstweekday=6)  # Sunday first
    month_days = cal.monthdayscalendar(year, BIRTHDAY_MONTH)

    html = """
    <div class="calendar-card">
        <div class="calendar-header">
            <div class="calendar-month">August</div>
            <div class="calendar-year">Birthday Month</div>
        </div>
        <div class="calendar-grid calendar-weekdays">
            <div>Sun</div><div>Mon</div><div>Tue</div><div>Wed</div><div>Thu</div><div>Fri</div><div>Sat</div>
        </div>
        <div class="calendar-grid">
    """

    for week in month_days:
        for day in week:
            if day == 0:
                html += '<div class="calendar-day empty"></div>'
            elif day == BIRTHDAY_DAY:
                html += f"""
                <div class="calendar-day birthday-day">
                    <span>{day}</span>
                    <small>🎂</small>
                </div>
                """
            else:
                html += f'<div class="calendar-day"><span>{day}</span></div>'

    html += """
        </div>
        <div class="calendar-caption">
            August 26 is marked because this day belongs to Al Shihab 🎈
        </div>
    </div>
    """

    return html


def typewriter_message(message, delay=0.018):
    placeholder = st.empty()
    typed_text = ""

    for char in message:
        typed_text += char
        placeholder.markdown(
            f"""
            <div class="typewriter-box">
                {typed_text}
            </div>
            """,
            unsafe_allow_html=True,
        )
        time.sleep(delay)


def birthday_scan():
    scan_text = st.empty()
    progress = st.progress(0)

    scan_steps = [
        "Reading birthday energy...",
        "Finding the cutest birthday signal...",
        "Checking smile probability...",
        "Scanning memories from March 2, 2021...",
        "Measuring long-distance birthday warmth...",
        "Preparing birthday result...",
    ]

    for i in range(101):
        progress.progress(i)
        scan_text.write(random.choice(scan_steps))
        time.sleep(0.012)

    scan_text.success("Birthday scan completed successfully 🎉")


def show_metric_progress(label, value, emoji):
    st.markdown(f"**{emoji} {label}**")
    st.progress(value)
    st.caption(f"{value}%")


# =========================================================
# CSS Styling
# =========================================================

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1.2rem;
        max-width: 1450px;
    }

    .hero-box {
        background: linear-gradient(135deg, #fff1f2 0%, #ffe4e6 35%, #fdf2f8 100%);
        border-radius: 30px;
        padding: 2.2rem;
        border: 1px solid rgba(244, 114, 182, 0.25);
        box-shadow: 0 18px 55px rgba(244, 114, 182, 0.18);
        margin-bottom: 1.2rem;
        position: relative;
        overflow: hidden;
    }

    .hero-box:before {
        content: "🎂";
        position: absolute;
        font-size: 8rem;
        right: 2rem;
        top: 0.6rem;
        opacity: 0.16;
    }

    .hero-title {
        font-size: 3.1rem;
        font-weight: 900;
        color: #9f1239;
        line-height: 1.08;
        margin-bottom: 0.6rem;
    }

    .hero-subtitle {
        font-size: 1.13rem;
        color: #831843;
        line-height: 1.65;
        max-width: 900px;
    }

    .cute-badge {
        display: inline-block;
        background: #ffe4e6;
        color: #9f1239;
        padding: 0.36rem 0.78rem;
        border-radius: 999px;
        font-size: 0.9rem;
        font-weight: 800;
        margin: 0.25rem 0.25rem 0.25rem 0;
    }

    .glass-card {
        background: rgba(255, 255, 255, 0.82);
        border-radius: 26px;
        padding: 1.35rem;
        border: 1px solid rgba(244, 114, 182, 0.22);
        box-shadow: 0 14px 35px rgba(100, 116, 139, 0.12);
        height: 100%;
    }

    .section-title {
        font-size: 1.35rem;
        font-weight: 900;
        color: #9f1239;
        margin-bottom: 0.65rem;
    }

    .small-note {
        color: #64748b;
        font-size: 0.96rem;
        line-height: 1.55;
    }

    .image-frame {
        background: linear-gradient(135deg, #ffffff, #fff1f2);
        padding: 0.7rem;
        border-radius: 28px;
        border: 1px solid rgba(244, 63, 94, 0.16);
        box-shadow: 0 16px 35px rgba(225, 29, 72, 0.12);
    }

    .placeholder-photo {
        height: 390px;
        border-radius: 24px;
        background: linear-gradient(135deg, #ffe4e6, #fdf2f8);
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        color: #9f1239;
        border: 2px dashed rgba(225, 29, 72, 0.35);
        text-align: center;
    }

    .placeholder-initials {
        font-size: 4rem;
        font-weight: 900;
        margin-bottom: 0.4rem;
    }

    .timeline-card {
        background: #ffffff;
        border-left: 7px solid #fb7185;
        border-radius: 20px;
        padding: 1rem 1.15rem;
        box-shadow: 0 8px 22px rgba(15, 23, 42, 0.08);
        margin-bottom: 0.85rem;
    }

    .timeline-date {
        font-weight: 900;
        color: #9f1239;
        font-size: 1.03rem;
    }

    .timeline-text {
        color: #475569;
        line-height: 1.55;
        margin-top: 0.25rem;
    }

    .memory-card {
        background: linear-gradient(135deg, #ffffff, #fff7ed);
        border-radius: 24px;
        padding: 1.2rem 1.25rem;
        border: 1px solid rgba(251, 113, 133, 0.18);
        box-shadow: 0 12px 28px rgba(15, 23, 42, 0.08);
        margin-bottom: 1rem;
    }

    .memory-title {
        color: #9f1239;
        font-size: 1.16rem;
        font-weight: 900;
        margin-bottom: 0.35rem;
    }

    .memory-body {
        color: #475569;
        line-height: 1.65;
        font-size: 1rem;
    }

    .wish-card {
        background: linear-gradient(135deg, #ffffff, #fff1f2);
        border-radius: 26px;
        padding: 1.4rem;
        border: 1px solid rgba(225, 29, 72, 0.18);
        box-shadow: 0 12px 28px rgba(225, 29, 72, 0.09);
        margin-bottom: 1rem;
    }

    .wish-text {
        font-size: 1.1rem;
        color: #881337;
        line-height: 1.75;
        font-weight: 500;
    }

    .calendar-card {
        background: linear-gradient(135deg, #ffffff, #fff1f2);
        border-radius: 28px;
        padding: 1.2rem;
        border: 1px solid rgba(244, 63, 94, 0.18);
        box-shadow: 0 14px 32px rgba(225, 29, 72, 0.10);
    }

    .calendar-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 0.9rem;
    }

    .calendar-month {
        color: #9f1239;
        font-weight: 900;
        font-size: 1.55rem;
    }

    .calendar-year {
        background: #ffe4e6;
        color: #9f1239;
        padding: 0.35rem 0.7rem;
        border-radius: 999px;
        font-weight: 800;
        font-size: 0.86rem;
    }

    .calendar-grid {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 0.45rem;
    }

    .calendar-weekdays {
        color: #9f1239;
        font-weight: 900;
        font-size: 0.82rem;
        text-align: center;
        margin-bottom: 0.45rem;
    }

    .calendar-day {
        min-height: 54px;
        border-radius: 15px;
        background: #ffffff;
        border: 1px solid rgba(244, 114, 182, 0.16);
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        color: #475569;
        font-weight: 800;
    }

    .calendar-day.empty {
        background: transparent;
        border: none;
    }

    .birthday-day {
        background: linear-gradient(135deg, #fb7185, #db2777);
        color: white;
        transform: scale(1.06);
        box-shadow: 0 10px 25px rgba(219, 39, 119, 0.30);
    }

    .birthday-day small {
        font-size: 1rem;
        margin-top: 0.1rem;
    }

    .calendar-caption {
        text-align: center;
        color: #831843;
        margin-top: 0.9rem;
        font-weight: 800;
        font-size: 0.95rem;
    }

    .capsule-box {
        background: radial-gradient(circle at top left, #ffe4e6, #ffffff 42%, #fdf2f8 100%);
        border-radius: 30px;
        padding: 1.7rem;
        border: 1px solid rgba(244, 63, 94, 0.20);
        box-shadow: 0 18px 45px rgba(225, 29, 72, 0.13);
        text-align: center;
    }

    .capsule-title {
        color: #9f1239;
        font-size: 1.8rem;
        font-weight: 900;
        margin-bottom: 0.5rem;
    }

    .capsule-subtitle {
        color: #64748b;
        line-height: 1.6;
        margin-bottom: 1rem;
    }

    .typewriter-box {
        background: #ffffff;
        border-radius: 24px;
        padding: 1.5rem;
        border: 1px solid rgba(225, 29, 72, 0.18);
        box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08);
        color: #831843;
        font-size: 1.08rem;
        line-height: 1.8;
        font-weight: 500;
        text-align: left;
        white-space: pre-wrap;
    }

    .quote-strip {
        background: #fff1f2;
        border-radius: 22px;
        padding: 1rem 1.2rem;
        color: #9f1239;
        font-weight: 800;
        text-align: center;
        border: 1px solid rgba(244, 63, 94, 0.15);
        margin-bottom: 1rem;
    }

    .footer-note {
        text-align: center;
        padding: 1rem;
        color: #831843;
        font-weight: 800;
    }

    div.stButton > button {
        border-radius: 15px;
        border: 0;
        background: linear-gradient(135deg, #fb7185, #db2777);
        color: white;
        font-weight: 900;
        padding: 0.68rem 1.1rem;
        box-shadow: 0 8px 18px rgba(219, 39, 119, 0.25);
    }

    div.stButton > button:hover {
        border: 0;
        color: white;
        transform: translateY(-1px);
    }

    .floating-items {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        pointer-events: none;
        z-index: 999999;
    }

    .float-item {
        position: absolute;
        animation: floatItem 9s linear infinite;
        color: rgba(244, 63, 94, 0.45);
        font-size: 25px;
    }

    .float-item:nth-child(1) { left: 8%; animation-delay: 0s; }
    .float-item:nth-child(2) { left: 22%; animation-delay: 1.6s; }
    .float-item:nth-child(3) { left: 45%; animation-delay: 3s; }
    .float-item:nth-child(4) { left: 68%; animation-delay: 2.2s; }
    .float-item:nth-child(5) { left: 84%; animation-delay: 4s; }

    @keyframes floatItem {
        0% {
            transform: translateY(100vh) scale(0.75);
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

    <div class="floating-items">
        <div class="float-item">💗</div>
        <div class="float-item">🎈</div>
        <div class="float-item">✨</div>
        <div class="float-item">🎂</div>
        <div class="float-item">💌</div>
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# Fixed Personalized Data
# =========================================================

today = date.today()
next_birthday = get_next_birthday()
days_to_birthday = (next_birthday - today).days
days_since_first_met = days_between(FIRST_MET_DATE)
days_since_left_country = days_between(LEFT_COUNTRY_DATE)

memories = [
    {
        "title": "2 March 2021 — The First Meeting",
        "body": (
            "That day became the beginning of a small but meaningful chapter. "
            "Sometimes one meeting is enough to stay remembered for years."
        ),
    },
    {
        "title": "The Long Gap After That Day",
        "body": (
            "After 2 March 2021, you have not seen each other again till now. "
            "Still, some people remain special not because they are always nearby, "
            "but because their presence leaves a quiet place in memory."
        ),
    },
    {
        "title": "12 December 2022 — A New Chapter in the USA",
        "body": (
            "On 12 December 2022, he left the country for the USA. "
            "That day marked a big change, a new journey, and a brave step toward his future."
        ),
    },
    {
        "title": "University of Georgia",
        "body": (
            f"Now he is studying at {UNIVERSITY_NAME}. "
            "That is something to feel proud of — a journey of effort, learning, independence, and growth."
        ),
    },
    {
        "title": "26 August — His Birthday",
        "body": (
            "August 26 is not just another date on the calendar. "
            "It is a day to wish him happiness, success, good health, peace, and a year full of beautiful progress."
        ),
    },
]

birthday_wish = f"""
Happy Birthday, {PERSON_NAME}! 🎂

Even though many days have passed since that first meeting on 2 March 2021, 
some memories still stay quietly meaningful. Today is your day, and I hope it brings you happiness, 
peace, confidence, and a lot of reasons to smile.

You have already started a brave chapter far from home, studying at the University of Georgia in the USA. 
May this new year of your life make you stronger, wiser, happier, and closer to every dream you are working for.

Wishing you a birthday as special as your journey.
"""

final_letter = f"""
Dear {PERSON_NAME},

Some dates do not need to be repeated often to remain special.

2 March 2021 was one of those dates — the first meeting, the first memory, and the beginning of a story that time did not completely erase.

Then came 12 December 2022, the day you left the country for the USA. Since then, life has placed distance, new routines, new people, and a new world around you. Now you are building your future at the University of Georgia, and that journey deserves respect.

On this birthday, the wish is simple but sincere:

May you never feel alone in the path you are walking.
May your efforts become achievements.
May your tired days end with peace.
May your new year bring good people, good health, good grades, and good memories.
May you become everything you are hoping to become.

Happy Birthday, {PERSON_NAME}.
This small page was made to remind you that your day matters, your journey matters, and you are remembered warmly.
"""


# =========================================================
# Hero Section
# =========================================================

st.markdown(
    f"""
    <div class="hero-box">
        <div class="hero-title">🎂 Happy Birthday, {PERSON_NAME}!</div>
        <div class="hero-subtitle">
            A tiny personalized birthday website made with memories, distance, warmth, and a little bit of birthday magic.
            From 2 March 2021 to today, some dates still remain special.
        </div>
        <br>
        <span class="cute-badge">🎈 August 26</span>
        <span class="cute-badge">📍 First met: 2 March 2021</span>
        <span class="cute-badge">✈️ USA journey: 12 December 2022</span>
        <span class="cute-badge">🎓 University of Georgia</span>
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
        "📖 Memory Album",
        "🎁 Surprise Box",
        "💌 Birthday Wish",
        "🌙 Final Message",
    ]
)


# =========================================================
# Birthday Home
# =========================================================

with tab_home:
    left_col, right_col = st.columns([1.05, 1], gap="large")

    with left_col:
        st.markdown(
            """
            <div class="glass-card">
                <div class="section-title">📸 Birthday Home Photo</div>
                <div class="small-note">
                    This photo is loaded directly from the app folder. 
                    Save the image as <b>assets/al_shihab.jpg</b>.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")

        if HOME_IMAGE_PATH.exists():
            st.markdown('<div class="image-frame">', unsafe_allow_html=True)
            st.image(str(HOME_IMAGE_PATH), caption=f"Happy Birthday, {PERSON_NAME} 🎂", use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.markdown(
                """
                <div class="placeholder-photo">
                    <div class="placeholder-initials">AS</div>
                    <div><b>Photo will appear here</b></div>
                    <div style="margin-top:0.35rem;">Save image as <code>assets/al_shihab.jpg</code></div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with right_col:
        st.markdown(
            """
            <div class="glass-card">
                <div class="section-title">🗓️ Birthday Calendar</div>
                <div class="small-note">
                    August is his birthday month, and 26 August is marked specially.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.write("")
        st.markdown(create_august_calendar_html(next_birthday.year), unsafe_allow_html=True)

    st.divider()

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.metric("Birthday Date", "26 August")

    with m2:
        st.metric("Days Until Birthday", days_to_birthday)

    with m3:
        st.metric("Days Since First Meeting", days_since_first_met)

    with m4:
        st.metric("Days Since USA Journey", days_since_left_country)

    st.divider()

    st.markdown("## 🔍 Birthday Happiness Scan")

    scan_left, scan_right = st.columns([1, 1], gap="large")

    with scan_left:
        if st.button("Start Birthday Scan 🎂"):
            birthday_scan()
            st.balloons()

    with scan_right:
        show_metric_progress("Birthday Glow", 100, "✨")
        show_metric_progress("Special Memory Value", 99, "💗")
        show_metric_progress("Long-Distance Warmth", 98, "🌙")

        st.success("Result: This birthday deserves a beautiful wish and a very special smile.")


# =========================================================
# Memory Album
# =========================================================

with tab_memory:
    st.markdown("## 📖 Memory Album")

    st.markdown(
        """
        <div class="quote-strip">
            Some memories are not measured by how often people meet, but by how deeply a date stays remembered.
        </div>
        """,
        unsafe_allow_html=True,
    )

    for memory in memories:
        st.markdown(
            f"""
            <div class="memory-card">
                <div class="memory-title">💗 {memory["title"]}</div>
                <div class="memory-body">{memory["body"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    st.markdown("## 🧭 Small Timeline")

    timeline_items = [
        ("2 March 2021", "First meeting — the date where this memory began."),
        ("12 December 2022", "He left the country for the USA and started a new chapter."),
        ("Now", f"He is studying at {UNIVERSITY_NAME}."),
        ("26 August", "His birthday — a day to wish him happiness, success, and peace."),
    ]

    for timeline_date, timeline_text in timeline_items:
        st.markdown(
            f"""
            <div class="timeline-card">
                <div class="timeline-date">{timeline_date}</div>
                <div class="timeline-text">{timeline_text}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# =========================================================
# Surprise Box
# =========================================================

with tab_surprise:
    st.markdown("## 🎁 Birthday Surprise Box")

    st.write(
        "Each box reveals a small birthday message. "
        "This keeps the website interactive without needing any machine learning model."
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        if st.button("Open Box 1 🎁"):
            st.success("Unlocked: A wish for peace, happiness, and a soft smile today.")

    with c2:
        if st.button("Open Box 2 ✨"):
            st.success("Unlocked: A proud reminder — studying far from home takes courage.")

    with c3:
        if st.button("Open Box 3 🎈"):
            st.success("Unlocked: May this birthday bring him closer to every dream he is working for.")

    st.divider()

    st.markdown("## 🎲 Random Birthday Line")

    birthday_lines = [
        "A birthday is not only about age; it is about the journey that shaped the person.",
        "Distance changes location, not the value of a meaningful memory.",
        "August 26 deserves cake, smiles, peace, and a little extra happiness.",
        "From Bangladesh to the USA, his journey is already something special.",
        "May this year be kinder, brighter, and more successful for him.",
    ]

    if st.button("Generate a Birthday Line 💌"):
        st.info(random.choice(birthday_lines))


# =========================================================
# Birthday Wish
# =========================================================

with tab_wish:
    st.markdown("## 💌 Birthday Wish for Al Shihab")

    st.markdown(
        f"""
        <div class="wish-card">
            <div class="wish-text">
                {birthday_wish}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()

    st.markdown("## ✨ Short Wish Version")

    short_wish = f"""
    Happy Birthday, {PERSON_NAME}! 🎂  
    Wishing you happiness, peace, success, and a beautiful year ahead. 
    From the first meeting on 2 March 2021 to your journey at the University of Georgia, 
    your story has become even more special. May this birthday bring you closer to your dreams.
    """

    st.markdown(
        f"""
        <div class="wish-card">
            <div class="wish-text">
                {short_wish}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# Final Message
# =========================================================

with tab_final:
    st.markdown("## 🌙 Final Message: A Birthday Time Capsule")

    st.markdown(
        """
        <div class="capsule-box">
            <div class="capsule-title">💌 A Message Across Time and Distance</div>
            <div class="capsule-subtitle">
                This final section works like a small digital time capsule. 
                It connects the first meeting, the USA journey, the birthday date, and one sincere message.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    t1, t2, t3 = st.columns(3)

    with t1:
        st.markdown(
            """
            <div class="timeline-card">
                <div class="timeline-date">Memory Key 1</div>
                <div class="timeline-text">2 March 2021<br>First meeting</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with t2:
        st.markdown(
            """
            <div class="timeline-card">
                <div class="timeline-date">Memory Key 2</div>
                <div class="timeline-text">12 December 2022<br>USA journey</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with t3:
        st.markdown(
            """
            <div class="timeline-card">
                <div class="timeline-date">Memory Key 3</div>
                <div class="timeline-text">26 August<br>Birthday</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    if "final_opened" not in st.session_state:
        st.session_state.final_opened = False

    if st.button("Open the Time Capsule 💌"):
        st.session_state.final_opened = True
        st.balloons()

    if st.session_state.final_opened:
        typewriter_message(final_letter)
    else:
        st.info("Click the button above to open the final birthday message.")

    st.markdown(
        """
        <div class="footer-note">
            Made with Streamlit, memories, distance, and a warm birthday wish 🎂✨
        </div>
        """,
        unsafe_allow_html=True,
    )
