import streamlit as st
import time  # Import the time module here

# Configure the page (must be first)
st.set_page_config(page_title="Splash", layout="wide")

# Hide the sidebar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)

# Render the splash screen HTML
st.markdown("""
<div class="min-h-screen bg-gradient-to-br from-blue-200 to-teal-200 flex items-center justify-center">
  <div class="text-center">
    <div class="w-32 h-32 bg-white rounded-full flex items-center justify-center shadow-lg mx-auto">
      <i class="fa-solid fa-heart-pulse text-blue-500 text-5xl"></i>
    </div>
    <h1 class="text-4xl font-bold text-blue-900 mt-6">VitalScan</h1>
    <p class="text-lg text-teal-800 mt-2">Contactless Health Monitoring</p>
    <p class="mt-4 text-sm text-gray-600">Please wait...</p>
  </div>
</div>
""", unsafe_allow_html=True)

# Wait for 3 seconds, then provide a link to navigate to the Onboarding page.
time.sleep(3)
st.page_link("Go to Onboarding", page_name="2_Onboarding", icon="➡️")
