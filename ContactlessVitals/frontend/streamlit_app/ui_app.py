import streamlit as st

# Configure the main app page (only call this once, here in ui_app.py)
st.set_page_config(page_title="Contactless Mobile Vital Signs", layout="wide")

# Hide the sidebar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("## Navigation")
st.markdown("Click on the links below to navigate:")

# Use st.page_link (the parameter is "page", not "page_name")
st.page_link("Splash", page="1_Splash", icon="🌅")
st.page_link("Onboarding", page="2_Onboarding", icon="📝")
st.page_link("Home", page="3_Home", icon="🏠")
st.page_link("Measurement", page="4_Measurement", icon="🎥")
st.page_link("History & Trends", page="5_History", icon="📈")
