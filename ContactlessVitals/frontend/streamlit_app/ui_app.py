import streamlit as st

st.set_page_config(page_title="Main Navigation", layout="wide")

st.write("Choose a page below:")

# If your pages are named "1_Splash.py", "2_Onboarding.py", etc., do:

st.page_link(page="1_Splash.py", label="Splash", icon="🌅")
st.page_link(page="2_Onboarding.py", label="Onboarding", icon="📝")
st.page_link(page="3_Home.py", label="Home", icon="🏠")
st.page_link(page="4_Measurement.py", label="Measurement", icon="🎥")


