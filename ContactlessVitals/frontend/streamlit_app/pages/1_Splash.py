import streamlit as st

# Must be the first Streamlit command
st.set_page_config(page_title="Splash", layout="wide")

# Optionally hide the sidebar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)

# Define your splash page HTML.
# The outer <body> has an onclick event that sends the user to the Onboarding page.
splash_html = """
<html>
  <head>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/js/all.min.js"
            crossorigin="anonymous"
            referrerpolicy="no-referrer"></script>
    <style>
      * { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; }
    </style>
  </head>
  <body onclick="window.location.href='?page=2_Onboarding'" style="cursor:pointer;" class="min-h-screen bg-gradient-to-br from-blue-200 to-teal-200 flex items-center justify-center">
    <div class="text-center">
      <div class="w-32 h-32 bg-white rounded-full flex items-center justify-center shadow-lg mx-auto">
          <i class="fa-solid fa-heart-pulse text-blue-500 text-5xl"></i>
      </div>
      <h1 class="text-4xl font-bold text-blue-900 mt-6">VitalScan</h1>
      <p class="text-lg text-teal-800 mt-2">Contactless Health Monitoring</p>
      <p class="mt-4 text-sm text-gray-600">Please wait... (click anywhere to continue)</p>
    </div>
  </body>
</html>
"""

# Render the splash screen.
st.components.v1.html(splash_html, height=900, scrolling=False)
