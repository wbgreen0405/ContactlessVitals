import streamlit as st

# Hide the sidebar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="Contactless Mobile Vital Signs", layout="wide")

st.markdown("Use the links below to navigate to different pages:")

# Custom navigation using st.page_link with the correct parameter name ("page")
st.page_link("Splash", page="1_Splash", icon="🌅")
st.page_link("Onboarding", page="2_Onboarding", icon="📝")
st.page_link("Home", page="3_Home", icon="🏠")
st.page_link("Measurement", page="4_Measurement", icon="🎥")
st.page_link("History & Trends", page="5_History", icon="📈")
