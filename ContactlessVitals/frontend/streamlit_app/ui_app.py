import streamlit as st

# Optional: Hide default sidebar navigation via configuration
st.set_page_config(page_title="Contactless Mobile Vital Signs", layout="wide")

st.markdown("## Welcome to Contactless Mobile Vital Signs")
st.markdown("Use the links below to navigate to different pages:")

# Custom navigation using st.page_link:
st.page_link("Splash", page_name="1_Splash", icon="🌅")
st.page_link("Onboarding", page_name="2_Onboarding", icon="📝")
st.page_link("Home", page_name="3_Home", icon="🏠")
st.page_link("Measurement", page_name="4_Measurement", icon="🎥")
st.page_link("History & Trends", page_name="5_History", icon="📈")
