import streamlit as st

st.set_page_config(page_title="Main Navigation", layout="wide")

st.write("Choose a page below:")

# 8 total pages now (including History)
st.page_link(page="1_Splash.py", label="Splash", icon="🌅")
st.page_link(page="2_Onboarding.py", label="Onboarding", icon="📝")
st.page_link(page="3_Home.py", label="Home", icon="🏠")
st.page_link(page="4_Measurement.py", label="Measurement", icon="🎥")
st.page_link(page="5_History.py", label="History", icon="🕰")  # Updated icon
st.page_link(page="6_MeasurementResults.py", label="Measurement Results", icon="🔍")
st.page_link(page="7_BloodPressureInsights.py", label="Blood Pressure Insights", icon="💡")
st.page_link(page="8_VitalSignsSummary.py", label="Vital Signs Summary", icon="📊")



