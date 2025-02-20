import streamlit as st

# Configure the page (must be the first Streamlit call)
st.set_page_config(page_title="Contactless Mobile Vital Signs", layout="wide")

# Optionally, hide the default sidebar with CSS
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main landing page content
st.title("Contactless Mobile Vital Signs")
st.write("Welcome to the Contactless Mobile Vital Signs app. Use the buttons below to navigate to different pages.")

# Navigation buttons using st.switch_page()
if st.button("Splash Screen"):
    st.switch_page("Splash")          # This should match the page name in your pages folder
if st.button("Onboarding"):
    st.switch_page("Onboarding")
if st.button("Home"):
    st.switch_page("Home")
if st.button("Measurement"):
    st.switch_page("Measurement")
if st.button("History & Trends"):
    st.switch_page("History & Trends")
