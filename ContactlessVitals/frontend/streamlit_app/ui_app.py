import streamlit as st

# Configure the main app page (only call set_page_config once, here!)
st.set_page_config(
    page_title="Contactless Mobile Vital Signs",
    layout="wide"
)

st.title("Contactless Mobile Vital Signs")
st.write("Welcome to the Contactless Mobile Vital Signs app. Use the buttons below to navigate.")

# Navigation buttons using st.switch_page() to jump to pages in /pages/
if st.button("Splash Screen"):
    st.switch_page("1_Splash")        # Must match the name of the .py file in pages/ (minus the .py)
if st.button("Onboarding"):
    st.switch_page("2_Onboarding")
if st.button("Home"):
    st.switch_page("3_Home")
if st.button("Measurement"):
    st.switch_page("4_Measurement")
if st.button("History & Trends"):
    st.switch_page("5_History")

