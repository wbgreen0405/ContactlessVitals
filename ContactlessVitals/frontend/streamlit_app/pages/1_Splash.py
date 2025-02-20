# pages/1_Splash.py
import streamlit as st

# Must be the first Streamlit command:
st.set_page_config(page_title="Splash", layout="wide")

# Hide the default sidebar (optional)
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

# The next page (e.g. 2_Onboarding.py)
onboarding_page_path = "/2_Onboarding"  # Adjust if needed

splash_html = f"""
<html>
<head>
  <!-- If you haven't already included Font Awesome globally, do so here: -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/js/all.min.js"
          crossorigin="anonymous" referrerpolicy="no-referrer"></script>
</head>
<body style="margin:0; padding:0;">
  <div onclick="window.location.href='{onboarding_page_path}'"
       style="
         min-height:100vh; 
         background: linear-gradient(to bottom right, #ccefff, #ccffe0);
         display:flex; 
         align-items:center; 
         justify-content:center; 
         cursor:pointer;">
    <div style="text-align:center;">
      <div style="
        width:8rem; 
        height:8rem; 
        background-color:white; 
        border-radius:50%; 
        display:flex; 
        align-items:center; 
        justify-content:center; 
        margin:0 auto; 
        box-shadow:0 0 10px rgba(0,0,0,0.2);
      ">
        <!-- The heart icon -->
        <i class="fa-solid fa-heart-pulse" style="font-size:3rem; color:#3b82f6;"></i>
      </div>
      <h1 style="font-size:2.5rem; color:#1f2937; margin-top:1rem;">VitalScan</h1>
      <p style="font-size:1.25rem; color:#1f2937;">Contactless Health Monitoring</p>
      <p style="margin-top:1rem; font-size:0.875rem; color:#6b7280;">
        Please wait... (click anywhere to continue)
      </p>
    </div>
  </div>
</body>
</html>
"""

st.write(splash_html, unsafe_allow_html=True)
