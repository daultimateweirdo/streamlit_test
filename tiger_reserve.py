import pandas as pd
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Tiger Explorer Adventure", page_icon="🐯", layout="wide"
)

# Custom Tiger-Themed CSS (Jungle Dark Green & Tiger Amber/Orange)
st.markdown(
    """
    <style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #101c14 0%, #1b2e20 100%);
        color: #f4f1ea;
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #0b140e;
        border-right: 2px solid #ff7b00;
    }
    /* Headings */
    h1, h2, h3 {
        color: #ff9e00 !important;
        font-family: 'Trebuchet MS', sans-serif;
    }
    /* Custom Tiger Card */
    .tiger-card {
        background-color: rgba(255, 123, 0, 0.12);
        border-left: 5px solid #ff7b00;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    /* Buttons */
    div.stButton > button {
        background-color: #ff7b00;
        color: #101c14;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        transition: all 0.2s ease-in-out;
    }
    div.stButton > button:hover {
        background-color: #ffaa00;
        color: #000000;
        transform: scale(1.02);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize Session State to store saved expeditions
if "expeditions" not in st.session_state:
    st.session_state.expeditions = []

# App Header
st.title("🐯 Tiger Explorer Adventure")
st.caption(
    "Step into the wild jungle to test your wildlife knowledge and plan your"
    " next tiger tracking expedition."
)
st.divider()

# Sidebar Navigation
st.sidebar.title("🐾 Jungle Navigation")
st.sidebar.markdown("Choose your path through the reserve:")
choice = st.sidebar.radio(
    "Go to:",
    ["🏕️ Basecamp (Home)", "🧠 Tiger Quiz", "🗺️ Expedition Planner"],
    label_visibility="collapsed",
)

st.sidebar.divider()
st.sidebar.info(
    "🐅 **Did you know?** Every tiger's stripe pattern is completely unique—just"
    " like human fingerprints!"
)

# --- 1. HOME SECTION ---
if choice == "🏕️ Basecamp (Home)":
    st.header("🌿 Welcome to the Tiger Reserve!")

    st.markdown(
        """
        <div class="tiger-card">
            <h4>Embark on an unforgettable wildlife adventure!</h4>
            <p>Use the navigation menu on the left to explore the reserve:</p>
            <ul>
                <li><b>🧠 Tiger Quiz:</b> Challenge yourself with trivia about the world's largest big cats.</li>
                <li><b>🗺️ Expedition Planner:</b> Organize and save your own jungle safari mission.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Quick Wildlife Stats using Columns & Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            label="Wild Tiger Population",
            value="~5,574",
            delta="Recovering Globally",
        )
    with col2:
        st.metric(
            label="Top Sprint Speed", value="65 km/h", delta="40 mph bursts"
        )
    with col3:
        st.metric(label="Roar Audibility", value="3 km", delta="Nearly 2 miles")

# --- 2. TIGER QUIZ SECTION ---
elif choice == "🧠 Tiger Quiz":
    st.header("🐾 Test Your Tiger Knowledge")
    st.write("Select your answers below and submit to earn your ranger badge!")

    with st.container(border=True):
        q1 = st.radio(
            "Q1: Which is the largest living tiger subspecies?",
            ["Bengal Tiger", "Siberian (Amur) Tiger", "Sumatran Tiger"],
            index=None,
        )
        st.divider()
        q2 = st.radio(
            "Q2: What happens if you shave a tiger's fur?",
            [
                "Its skin is plain pink",
                "Its skin still has the exact same stripes",
                "Its skin is covered in spots",
            ],
            index=None,
        )
        st.divider()
        q3 = st.radio(
            "Q3: How do tigers feel about water compared to most domestic cats?",
            [
                "They avoid it completely",
                "They are strong swimmers and love cooling off in water",
                "They only drink from waterfalls",
            ],
            index=None,
        )

    if st.button("🐾 Submit Quiz"):
        if None in (q1, q2, q3):
            st.warning(
                "⚠️ Please answer all three questions before submitting!"
            )
        else:
            score = 0
            if q1 == "Siberian (Amur) Tiger":
                score += 1
            if q2 == "Its skin still has the exact same stripes":
                score += 1
            if (
                q3
                == "They are strong swimmers and love cooling off in water"
            ):
                score += 1

            if score == 3:
                st.balloons()
                st.success(
                    f"🏆 Perfect Score: {score}/3! You are a Master Tiger"
                    " Tracker!"
                )
            else:
                st.info(
                    f"🐾 Your score is {score}/3. Review the tracker log below!"
                )

            results = pd.DataFrame({
                "Question": [
                    "Q1: Largest Subspecies",
                    "Q2: Shaved Fur",
                    "Q3: Water Behavior",
                ],
                "Your Answer": [q1, q2, q3],
                "Correct Answer": [
                    "Siberian (Amur) Tiger",
                    "Its skin still has the exact same stripes",
                    "They are strong swimmers and love cooling off in water",
                ],
            })
            st.dataframe(results, use_container_width=True, hide_index=True)

# --- 3. EXPEDITION PLANNER SECTION ---
elif choice == "🗺️ Expedition Planner":
    st.header("🚙 Plan Your Tiger Tracking Expedition")

    col_form, col_quote = st.columns([2, 1])

    with col_form:
        with st.container(border=True):
            team_name = st.text_input(
                "Name your ranger team / jeep:", "Striped Vanguard"
            )

            c1, c2 = st.columns(2)
            with c1:
                launch_date = st.date_input("Select expedition date:")
            with c2:
                launch_time = st.time_input("Select safari start time:")

            vehicle_type = st.selectbox(
                "Choose your safari transport:",
                [
                    "Open-Top 4x4 Jeep",
                    "Camouflaged Watchtower",
                    "River Patrol Boat",
                    "Foot Tracking Patrol",
                ],
            )

            if st.button("🐅 Log Expedition"):
                new_trip = {
                    "Team": team_name,
                    "Date": str(launch_date),
                    "Time": str(launch_time),
                    "Transport": vehicle_type,
                }
                st.session_state.expeditions.append(new_trip)
                st.success(
                    f"Expedition '{team_name}' scheduled for {launch_date} at"
                    f" {launch_time} via {vehicle_type}!"
                )

    with col_quote:
        with st.container(border=True):
            st.subheader("🔥 Jungle Wisdom")
            category = st.selectbox(
                "Choose a theme:", ["Conservation", "Courage", "The Wild"]
            )
            quotes = {
                "Conservation": (
                    "When a man wants to murder a tiger he calls it sport; when"
                    " a tiger wants to murder him he calls it ferocity."
                ),
                "Courage": (
                    "The tiger does not lose sleep over the opinion of sheep."
                ),
                "The Wild": (
                    "In the deep jungle, every rustle of leaves tells a story"
                    " of survival."
                ),
            }
            st.markdown(f"> *“{quotes[category]}”*")

    # Display saved expeditions from session state
    if st.session_state.expeditions:
        st.divider()
        st.subheader("📋 Scheduled Expeditions Log")
        st.dataframe(
            pd.DataFrame(st.session_state.expeditions),
            use_container_width=True,
            hide_index=True,
        )
