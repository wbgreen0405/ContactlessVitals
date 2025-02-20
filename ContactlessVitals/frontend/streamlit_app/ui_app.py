import streamlit as st

st.set_page_config(page_title="Main Navigation", layout="wide")

st.write("Choose a page below:")

# If your pages are named "1_Splash.py", "2_Onboarding.py", etc., do:

st.page_link(page="1_Splash", label="Splash", icon="🌅")
st.page_link(page="2_Onboarding", label="Onboarding", icon="📝")
st.page_link(page="3_Home", label="Home", icon="🏠")
st.page_link(page="4_Measurement", label="Measurement", icon="🎥")
st.page_link(page="5_History", label="History & Trends", icon="📈")

