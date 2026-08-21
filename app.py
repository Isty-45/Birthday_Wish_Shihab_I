import calendar
import json
import random
from datetime import date
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


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

# Anchor assets to this Python file instead of the process working directory.
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
HOME_IMAGE_NAME = "al_shihab.jpg"


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

def get_next_birthday(today=None):
    today = today or date.today()
    birthday_this_year = date(today.year, BIRTHDAY_MONTH, BIRTHDAY_DAY)
    return (
        date(today.year + 1, BIRTHDAY_MONTH, BIRTHDAY_DAY)
        if birthday_this_year < today
        else birthday_this_year
    )


def days_between(start_date, end_date=None):
    end_date = end_date or date.today()
    return max(0, (end_date - start_date).days)


def find_home_image():
    """Return a deployed image path safely.

    Streamlit Community Cloud runs on Linux, so filenames are case-sensitive.
    The preferred deployed filename is assets/al_shihab.jpg.
    """
    preferred = ASSETS_DIR / HOME_IMAGE_NAME
    if preferred.is_file():
        return preferred

    # Backward-compatible names from the original project.
    possible_names = (
        "al_shihab.jpg.jpeg",
        "al_shihab.jpeg",
        "al_shihab.png",
        "Al_Shihab.jpg",
        "Al_Shihab.jpeg",
        "Al_Shihab.png",
    )
    for name in possible_names:
        candidate = ASSETS_DIR / name
        if candidate.is_file():
            return candidate

    return None


def multiline_to_html(text):
    """Preserve line breaks for trusted, locally-authored text."""
    import html

    return html.escape(text.strip()).replace("\n", "<br>")


def create_august_calendar_html(year):
    cal = calendar.Calendar(firstweekday=6)  # Sunday first
    month_days = cal.monthdayscalendar(year, BIRTHDAY_MONTH)

    html_parts = [
        """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <style>
                * { box-sizing: border-box; }
                body {
                    margin: 0;
                    padding: 0;
                    font-family: Arial, sans-serif;
                    background: transparent;
                }
                .calendar-card {
                    background: linear-gradient(135deg, #ffffff 0%, #eff6ff 100%);
                    border-radius: 30px;
                    padding: 24px;
                    border: 1px solid rgba(37, 99, 235, 0.24);
                    box-shadow: 0 18px 42px rgba(37, 99, 235, 0.14);
                    width: 100%;
                }
                .calendar-header {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    gap: 12px;
                    margin-bottom: 24px;
                }
                .calendar-month {
                    color: #1e3a8a;
                    font-weight: 900;
                    font-size: 30px;
                    line-height: 1;
                }
                .calendar-year {
                    background: #dbeafe;
                    color: #1e40af;
                    padding: 10px 18px;
                    border-radius: 999px;
                    font-weight: 900;
                    font-size: 15px;
                    white-space: nowrap;
                }
                .calendar-weekday-grid,
                .calendar-day-grid {
                    display: grid;
                    grid-template-columns: repeat(7, minmax(0, 1fr));
                    gap: 10px;
                }
                .calendar-weekday-grid {
                    margin-bottom: 12px;
                    text-align: center;
                }
                .calendar-weekday-grid div {
                    color: #1d4ed8;
                    font-size: 15px;
                    font-weight: 900;
                }
                .calendar-day {
                    min-height: 66px;
                    border-radius: 17px;
                    background: #ffffff;
                    border: 1px solid rgba(37, 99, 235, 0.18);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    flex-direction: column;
                    color: #334155;
                    font-weight: 900;
                    font-size: 18px;
                }
                .empty-day {
                    background: transparent;
                    border: none;
                }
                .birthday-day {
                    background: linear-gradient(135deg, #38bdf8, #2563eb);
                    color: #ffffff;
                    box-shadow: 0 14px 30px rgba(37, 99, 235, 0.36);
                    border: none;
                    transform: scale(1.03);
                }
                .birthday-day span {
                    font-size: 20px;
                    line-height: 1;
                }
                .birthday-day small {
                    font-size: 18px;
                    margin-top: 8px;
                    line-height: 1;
                }
                .calendar-caption {
                    text-align: center;
                    color: #1e3a8a;
                    margin-top: 24px;
                    font-weight: 900;
                    font-size: 17px;
                    line-height: 1.45;
                }
                @media (max-width: 700px) {
                    .calendar-card { padding: 16px; border-radius: 22px; }
                    .calendar-day-grid, .calendar-weekday-grid { gap: 6px; }
                    .calendar-day { min-height: 50px; font-size: 15px; }
                    .calendar-month { font-size: 24px; }
                    .calendar-year { padding: 8px 12px; font-size: 13px; }
                }
            </style>
        </head>
        <body>
            <div class="calendar-card">
                <div class="calendar-header">
                    <div class="calendar-month">August</div>
                    <div class="calendar-year">Birthday Month</div>
                </div>
                <div class="calendar-weekday-grid">
                    <div>Sun</div><div>Mon</div><div>Tue</div><div>Wed</div>
                    <div>Thu</div><div>Fri</div><div>Sat</div>
                </div>
                <div class="calendar-day-grid">
        """
    ]

    for week in month_days:
        for day in week:
            if day == 0:
                html_parts.append('<div class="calendar-day empty-day"></div>')
            elif day == BIRTHDAY_DAY:
                html_parts.append(
                    f'<div class="calendar-day birthday-day"><span>{day}</span><small>🎂</small></div>'
                )
            else:
                html_parts.append(f'<div class="calendar-day"><span>{day}</span></div>')

    html_parts.append(
        """
                </div>
                <div class="calendar-caption">This day belongs to AS 🎈</div>
            </div>
        </body>
        </html>
        """
    )
    return "".join(html_parts)


def typewriter_message(message, delay_ms=18):
    """Render the final letter with non-blocking browser-side animation.

    The original version used time.sleep() in Python. Streamlit reruns the full
    script whenever a widget changes, and all tab content is normally computed,
    so that implementation could block every later interaction for many seconds.
    """
    js_message = json.dumps(message)
    safe_delay = max(5, int(delay_ms))

    component = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            * {{ box-sizing: border-box; }}
            body {{
                margin: 0;
                padding: 2px;
                background: transparent;
                font-family: Arial, sans-serif;
            }}
            #typewriter-box {{
                background: #ffffff;
                border-radius: 24px;
                padding: 1.5rem;
                border: 1px solid rgba(37, 99, 235, 0.18);
                box-shadow: 0 12px 30px rgba(37, 99, 235, 0.12);
                color: #1e3a8a;
                font-size: 1.08rem;
                line-height: 1.8;
                font-weight: 500;
                text-align: left;
                white-space: pre-wrap;
                overflow-wrap: anywhere;
            }}
            .cursor {{
                display: inline-block;
                width: 2px;
                height: 1.1em;
                margin-left: 2px;
                background: #2563eb;
                vertical-align: -0.12em;
                animation: blink 0.75s step-end infinite;
            }}
            @keyframes blink {{ 50% {{ opacity: 0; }} }}
        </style>
    </head>
    <body>
        <div id="typewriter-box"><span id="typed"></span><span id="cursor" class="cursor"></span></div>
        <script>
            const message = {js_message};
            const typed = document.getElementById('typed');
            const cursor = document.getElementById('cursor');
            let i = 0;

            function typeNext() {{
                if (i < message.length) {{
                    typed.textContent += message.charAt(i);
                    i += 1;
                    window.setTimeout(typeNext, {safe_delay});
                }} else {{
                    cursor.style.display = 'none';
                }}
            }}
            typeNext();
        </script>
    </body>
    </html>
    """

    components.html(component, height=760, scrolling=True)


# =========================================================
# Computed Values
# =========================================================

next_birthday = get_next_birthday()
days_since_left_country = days_between(LEFT_COUNTRY_DATE)
home_image_path = find_home_image()


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
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 45%, #e0f2fe 100%);
        border-radius: 30px;
        padding: 2.2rem;
        border: 1px solid rgba(37, 99, 235, 0.25);
        box-shadow: 0 18px 55px rgba(37, 99, 235, 0.17);
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
        opacity: 0.14;
    }
    .hero-title {
        font-size: clamp(2.1rem, 5vw, 3.1rem);
        font-weight: 900;
        color: #1e3a8a;
        line-height: 1.08;
        margin-bottom: 0.6rem;
    }
    .hero-subtitle {
        font-size: 1.13rem;
        color: #1e40af;
        line-height: 1.65;
        max-width: 900px;
    }
    .cute-badge {
        display: inline-block;
        background: #dbeafe;
        color: #1e3a8a;
        padding: 0.36rem 0.78rem;
        border-radius: 999px;
        font-size: 0.9rem;
        font-weight: 800;
        margin: 0.25rem 0.25rem 0.25rem 0;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.84);
        border-radius: 26px;
        padding: 1.35rem;
        border: 1px solid rgba(37, 99, 235, 0.22);
        box-shadow: 0 14px 35px rgba(37, 99, 235, 0.12);
        height: 100%;
    }
    .section-title {
        font-size: 1.35rem;
        font-weight: 900;
        color: #1e3a8a;
        margin-bottom: 0.65rem;
    }
    .small-note {
        color: #475569;
        font-size: 0.96rem;
        line-height: 1.55;
    }
    .placeholder-photo {
        min-height: 390px;
        border-radius: 24px;
        background: linear-gradient(135deg, #dbeafe, #e0f2fe);
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        color: #1e3a8a;
        border: 2px dashed rgba(37, 99, 235, 0.38);
        text-align: center;
        padding: 1.5rem;
    }
    .placeholder-initials {
        font-size: 4rem;
        font-weight: 900;
        margin-bottom: 0.4rem;
    }
    .memory-card {
        background: linear-gradient(135deg, #ffffff, #eff6ff);
        border-radius: 24px;
        padding: 1.2rem 1.25rem;
        border: 1px solid rgba(37, 99, 235, 0.18);
        box-shadow: 0 12px 28px rgba(15, 23, 42, 0.08);
        margin-bottom: 1rem;
    }
    .memory-title {
        color: #1e3a8a;
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
        background: linear-gradient(135deg, #ffffff, #eff6ff);
        border-radius: 26px;
        padding: 1.4rem;
        border: 1px solid rgba(37, 99, 235, 0.18);
        box-shadow: 0 12px 28px rgba(37, 99, 235, 0.10);
        margin-bottom: 1rem;
    }
    .wish-text {
        font-size: 1.1rem;
        color: #1e3a8a;
        line-height: 1.75;
        font-weight: 500;
    }
    .quote-strip {
        background: #eff6ff;
        border-radius: 22px;
        padding: 1rem 1.2rem;
        color: #1e3a8a;
        font-weight: 800;
        text-align: center;
        border: 1px solid rgba(37, 99, 235, 0.16);
        margin-bottom: 1rem;
    }
    div.stButton > button {
        border-radius: 15px;
        border: 0;
        background: linear-gradient(135deg, #38bdf8, #2563eb);
        color: white;
        font-weight: 900;
        padding: 0.68rem 1.1rem;
        box-shadow: 0 8px 18px rgba(37, 99, 235, 0.28);
    }
    div.stButton > button:hover {
        border: 0;
        color: white;
        transform: translateY(-1px);
    }
    div[data-testid="stMetric"] {
        background: linear-gradient(135deg, #ffffff, #eff6ff);
        border: 1px solid rgba(37, 99, 235, 0.16);
        border-radius: 18px;
        padding: 1rem;
        box-shadow: 0 10px 24px rgba(37, 99, 235, 0.08);
    }
    div[data-testid="stImage"] img {
        border-radius: 24px;
        border: 1px solid rgba(37, 99, 235, 0.18);
        box-shadow: 0 16px 35px rgba(37, 99, 235, 0.13);
    }
    .floating-items {
        position: fixed;
        inset: 0;
        width: 100%;
        pointer-events: none;
        z-index: 999999;
        overflow: hidden;
    }
    .float-item {
        position: absolute;
        animation: floatItem 9s linear infinite;
        color: rgba(37, 99, 235, 0.42);
        font-size: 25px;
    }
    .float-item:nth-child(1) { left: 8%; animation-delay: 0s; }
    .float-item:nth-child(2) { left: 22%; animation-delay: 1.6s; }
    .float-item:nth-child(3) { left: 45%; animation-delay: 3s; }
    .float-item:nth-child(4) { left: 68%; animation-delay: 2.2s; }
    .float-item:nth-child(5) { left: 84%; animation-delay: 4s; }
    @keyframes floatItem {
        0% { transform: translateY(100vh) scale(0.75); opacity: 0; }
        20% { opacity: 1; }
        100% { transform: translateY(-10vh) scale(1.25); opacity: 0; }
    }
    @media (prefers-reduced-motion: reduce) {
        .float-item { animation: none; display: none; }
    }
    </style>

    <div class="floating-items">
        <div class="float-item">💙</div>
        <div class="float-item">🎈</div>
        <div class="float-item">✨</div>
        <div class="float-item">🎂</div>
        <div class="float-item">💌</div>
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# Personalized Messages
# =========================================================

memories = [
    {
        "title": "2nd March 2021",
        "body": (
            "That day became the beginning of a small but meaningful memory. "
            "Some moments stay quietly special."
        ),
    },
    {
        "title": "The Thoughtful Silence",
        "body": (
            "The way you listen and stay thoughtful makes you different in the best possible way. "
            "But, somehow you skip my channel."
        ),
    },
    {
        "title": "The First Memory",
        "body": (
            "Some little things make ordinary moments feel brighter. "
            "That first appearance of yours stays with me, a simple memory that never fades. "
            "And yes, I even remember those eyebrows, haha."
        ),
    },
    {
        "title": "The Friendship Memory",
        "body": (
            "Slowly something clicked between us. "
            "Somehow, in the quiet flow of time, we became friends."
        ),
    },
    {
        "title": "13 December 2022",
        "body": (
            "On 13 December 2022, you left the country. "
            "That was not just a journey to another place, it was the beginning of a new life chapter."
        ),
    },
    {
        "title": "The Long Gap",
        "body": (
            "After that, time moved forward in its own way. There were no more meetings, but you have "
            "a calm, warm, and rare kind of presence. Though I once carried a silent anger, it is all forgotten now."
        ),
    },
    {
        "title": "Appreciation",
        "body": (
            "Your journey deserves respect, because building a future far from home takes courage, effort, and patience."
        ),
    },
    {
        "title": "26 August",
        "body": (
            "August 26 is your birthday, and today is meant to remind you that you are appreciated, remembered, and warmly wished."
        ),
    },
]

birthday_wish = f"""
Happy Birthday, Shihab! 🎂

On this special day, I wish you a day full of peace, happiness, smiles, and small moments that make your heart feel light.

Life isn’t always easy, but you’ve carried yourself with strength, patience, and determination. Every step you take toward your future is proof of your courage, and I couldn’t be prouder to see you growing into the person you are meant to be.

May this year bring you peace in your heart, joy in your days, and confidence in your journey. May you find good people who inspire you, opportunities that challenge you, and achievements that remind you of your worth. I hope your hard work turns into meaningful results, your struggles become stepping stones, and your dreams feel closer with every sunrise.

Happy Birthday once again. I hope this makes you feel special, because you really are.
"""

final_letter = f"""
Dear {PERSON_NAME},

Some people remain part of our story even when life takes us far apart. I don’t know if we will ever meet again, and I do not wish for us to meet again, but I want you to know that you will always be remembered. The dates we shared and the moments we lived may fade one day.

You are living across oceans now, carrying the weight of new challenges, new routines, and new responsibilities. But I hope you never forget the dream that once lit your path — your dream of joining Microsoft. Please don’t give up on it. Even when the road feels long, even when the days feel heavy, remember that your hard work and persistence can take you there.

May your efforts turn into achievements.
May your struggles shape your strength.
May your dreams move closer each day.
And may you always find reasons to keep believing in yourself.

Though life moves on, your story still lingers in mine. This may be my last wish like this, because none of us knows where we will be next year, or what life will look like.

You are remembered with respect and gratitude,
Maherun Nessa Isty
"""


# =========================================================
# Hero Section
# =========================================================

st.markdown(
    f"""
    <div class="hero-box">
        <div class="hero-title">🎂 Happy Birthday, {PERSON_NAME}!</div>
        <div class="hero-subtitle">
            Today is all about celebrating you and the beautiful journey you are building.
        </div>
        <br>
        <span class="cute-badge">🎈 26th August 2026</span>
        <span class="cute-badge">💌 Birthday Wishes</span>
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
                <div class="small-note">A special photo for a special birthday moment.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")

        if home_image_path is not None:
            st.image(
                str(home_image_path),
                caption=f"Happy Birthday, {PERSON_NAME} 🎂",
                use_container_width=True,
            )
        else:
            st.markdown(
                f"""
                <div class="placeholder-photo">
                    <div class="placeholder-initials">AS</div>
                    <div><b>Photo will appear here</b></div>
                    <div style="margin-top:0.35rem;">
                        Add the file <b>assets/{HOME_IMAGE_NAME}</b> to the repository.
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with right_col:
        st.markdown(
            """
            <div class="glass-card">
                <div class="section-title">🗓️ Birthday Calendar</div>
                <div class="small-note">August is your birthday month, and 26th August is marked specially.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write("")
        components.html(
            create_august_calendar_html(next_birthday.year),
            height=620,
            scrolling=False,
        )

    st.divider()

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Birthday Date", "26 August")
    with c2:
        st.metric("Current Living", COUNTRY_NAME)
    with c3:
        st.metric("Days Living There", f"{days_since_left_country:,}")
    with c4:
        st.metric("Global Scholar Award", "Congratulations!!!")


# =========================================================
# Memory Album
# =========================================================

with tab_memory:
    st.markdown("## 📖 Memory Album")
    st.markdown(
        """
        <div class="quote-strip">
            Some memories are not measured by how often people meet, but by how deeply they stay remembered.
        </div>
        """,
        unsafe_allow_html=True,
    )

    for memory in memories:
        st.markdown(
            f"""
            <div class="memory-card">
                <div class="memory-title">💙 {memory['title']}</div>
                <div class="memory-body">{memory['body']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


# =========================================================
# Surprise Box
# =========================================================

with tab_surprise:
    st.markdown("## 🎁 Birthday Surprise Box")
    st.write("Each box reveals a small birthday message. This keeps the website interactive and cute.")

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("Open Box 1 🎁", key="box_1"):
            st.success("Unlocked: I wish you a peaceful heart and a happy smile today.")
    with c2:
        if st.button("Open Box 2 ✨", key="box_2"):
            st.success("Unlocked: I wish your hard work brings you beautiful success.")
    with c3:
        if st.button("Open Box 3 🎈", key="box_3"):
            st.success("Unlocked: I wish this birthday becomes the beginning of an amazing year for you.")

    st.divider()
    st.markdown("## 🎲 Random Birthday Line")

    birthday_lines = [
        "I hope your birthday feels soft, peaceful, and full of tiny happy moments.",
        "May your day be as bright as your smile and as sweet as your favorite dessert.",
        "I wish your heart feels lighter today, because birthdays should feel warm and special.",
        "May this chapter of your life become more beautiful, successful, and full of good surprises.",
        "I hope this birthday gives you a reason to smile even on a busy university day.",
        "May your dreams come closer, your worries become smaller, and your happiness grow bigger.",
        "I wish you good grades, good friends, peaceful nights, and a heart full of confidence.",
        "May August 26 bring you cake, smiles, blessings, and a little reminder that you are special.",
        "I hope your birthday feels like a warm hug from all the good memories around you.",
        "May this new year of your life be kinder, brighter, and more successful than the last one.",
        "I wish your coffee tastes better, your assignments feel easier, and your birthday feels extra cute today.",
        "May your birthday be full of sweet notifications, warm wishes, and one very happy heart.",
        "I hope today treats you gently and gives you a reason to smile without even trying.",
        "May your birthday feel like a soft little pause from everything stressful.",
        "I wish you a birthday full of cake-level sweetness and star-level brightness.",
    ]

    if "birthday_line" not in st.session_state:
        st.session_state.birthday_line = None

    if st.button("Generate a Birthday Line 💌", key="birthday_line_button"):
        st.session_state.birthday_line = random.choice(birthday_lines)

    if st.session_state.birthday_line:
        st.info(st.session_state.birthday_line)


# =========================================================
# Birthday Wish
# =========================================================

with tab_wish:
    st.markdown(f"## 💌 Birthday Wish for {PERSON_NAME}")
    st.markdown(
        f"""
        <div class="wish-card">
            <div class="wish-text">{multiline_to_html(birthday_wish)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================================================
# Final Message
# =========================================================

with tab_final:
    if "final_opened" not in st.session_state:
        st.session_state.final_opened = False

    if not st.session_state.final_opened:
        if st.button("Open the Capsule 💌", key="open_capsule"):
            st.session_state.final_opened = True
            st.balloons()
            st.rerun()
    else:
        typewriter_message(final_letter)

        if st.button("Close the Capsule", key="close_capsule"):
            st.session_state.final_opened = False
            st.rerun()
