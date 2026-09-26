import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Celebrity Fan Card",
    page_icon="⭐",
    layout="centered"
)

st.title("⭐ Celebrity Fan Card")
st.caption("UNOFFICIAL FAN CARD • Fan-made concept")

# Load CSV
df = pd.read_csv("fan_cards.csv")

# Celebrity selector
celebrity_options = df["celebrity"].drop_duplicates().tolist()

selected = st.selectbox(
    "Choose a celebrity",
    celebrity_options
)

# Custom celebrity
if selected == "Name Your Own Celebrity":
    celebrity_name = st.text_input(
        "Enter celebrity name",
        placeholder="e.g. Your favorite celebrity"
    )
else:
    celebrity_name = selected

st.subheader("Fan Details")

fan_name = st.text_input(
    "Fan name",
    placeholder="Enter fan name"
)

member_id = st.text_input(
    "Fan ID",
    placeholder="e.g. FC001"
)

status = st.selectbox(
    "Fan status",
    ["VIP Fan", "Premium Fan", "Regular Fan"]
)

join_date = st.text_input(
    "Member since",
    value="2026"
)

if st.button("Create Fan Card", type="primary"):

    if not fan_name:
        st.warning("Please enter the fan name.")
    elif not member_id:
        st.warning("Please enter a Fan ID.")
    elif not celebrity_name:
        st.warning("Please enter a celebrity name.")
    else:
        st.markdown("---")

        st.markdown(
            f"""
            <div style="
                border: 2px solid #333;
                border-radius: 18px;
                padding: 25px;
                max-width: 500px;
                margin: auto;
                text-align: center;
                background: linear-gradient(135deg, #f8f8f8, #ffffff);
                box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            ">
                <h2>⭐ FAN MEMBERSHIP CARD</h2>
                <h3>{celebrity_name}</h3>
                <hr>
                <p><b>Fan Name</b><br>{fan_name}</p>
                <p><b>Fan ID</b><br>{member_id}</p>
                <p><b>Status</b><br>{status}</p>
                <p><b>Member Since</b><br>{join_date}</p>
                <hr>
                <small>UNOFFICIAL FAN CARD • FAN-MADE CONCEPT</small>
            </div>
            """,
            unsafe_allow_html=True
        )
