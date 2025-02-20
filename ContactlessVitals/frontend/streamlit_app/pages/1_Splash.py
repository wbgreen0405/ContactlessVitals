import streamlit as st
import time

# Hide the sidebar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)

# Configure the page (only once, here in the splash page)
st.set_page_config(page_title="Splash", layout="wide")

# Render the splash screen HTML
st.markdown(
    """
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
    """,
    unsafe_allow_html=True
)

# Wait 3 seconds, then switch to the Onboarding page
time.sleep(3)
st.switch_page("Onboarding")
