import streamlit as st
import pandas as pd

st.set_page_config(page_title="Celebrity Fan Card", page_icon="⭐")
st.title("⭐ Celebrity Fan Card")
st.caption("UNOFFICIAL FAN CARD • Fan-made concept")

df = pd.read_csv("fan_cards.csv")
if "celebrity_photo_url" not in df.columns:
    df["celebrity_photo_url"] = ""

selected = st.selectbox("Choose a celebrity", df["celebrity"].drop_duplicates().tolist())
row = df[df["celebrity"] == selected].iloc[0]

if selected == "Name Your Own Celebrity":
    celebrity_name = st.text_input("Enter celebrity name")
else:
    celebrity_name = selected

st.subheader("Celebrity Photo")
photo_url = str(row.get("celebrity_photo_url", "")).strip()
if photo_url:
    st.image(photo_url, caption=celebrity_name, width=220)

celeb_photo = st.file_uploader("Upload celebrity photo", type=["jpg","jpeg","png","webp"], key="celeb")

st.subheader("Fan Details")
fan_name = st.text_input("Fan name")
member_id = st.text_input("Fan ID", placeholder="FC001")
status = st.selectbox("Fan status", ["VIP Fan", "Premium Fan", "Regular Fan"])
join_date = st.text_input("Member since", "2026")
fan_photo = st.file_uploader("Upload fan photo", type=["jpg","jpeg","png","webp"], key="fan")

if st.button("Create Fan Card", type="primary"):
    if not fan_name or not member_id or not celebrity_name:
        st.warning("Please complete the fan name, Fan ID, and celebrity name.")
    elif not celeb_photo and not photo_url:
        st.warning("Please upload a celebrity photo.")
    elif not fan_photo:
        st.warning("Please upload a fan photo.")
    else:
        st.markdown("---")
        st.subheader("Your Fan Card")
        c1, c2 = st.columns(2)
        with c1:
            st.image(celeb_photo if celeb_photo else photo_url,
                     caption=celebrity_name, use_container_width=True)
        with c2:
            st.image(fan_photo, caption=fan_name, use_container_width=True)

        st.markdown(f'''
        <div style="border:2px solid #444;border-radius:18px;padding:22px;
        text-align:center;background:#fff;box-shadow:0 8px 25px rgba(0,0,0,.15);">
        <h2>⭐ FAN MEMBERSHIP CARD</h2>
        <h3>{celebrity_name}</h3><hr>
        <p><b>Fan Name</b><br>{fan_name}</p>
        <p><b>Fan ID</b><br>{member_id}</p>
        <p><b>Status</b><br>{status}</p>
        <p><b>Member Since</b><br>{join_date}</p><hr>
        <small>UNOFFICIAL FAN CARD • FAN-MADE CONCEPT</small>
        </div>
        ''', unsafe_allow_html=True)
