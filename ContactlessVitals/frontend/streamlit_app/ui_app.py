import streamlit as st

# Hide the default sidebar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Set up the main landing page
st.set_page_config(page_title="Contactless Mobile Vital Signs", layout="wide")
st.title("Contactless Mobile Vital Signs")
st.write("Welcome to the Contactless Mobile Vital Signs app. Use the buttons below to navigate to the different pages.")

# Provide navigation buttons that switch pages
if st.button("Splash Screen"):
    st.switch_page("Splash")       # This should match the title or name of your splash page file (e.g. "Splash.py")
if st.button("Onboarding"):
    st.switch_page("Onboarding")   # Make sure your onboarding page is named accordingly
if st.button("Home"):
    st.switch_page("Home")
if st.button("Measurement"):
    st.switch_page("Measurement")
if st.button("History & Trends"):
    st.switch_page("History & Trends")
