# pages/1_Splash.py
import streamlit as st

# Must be the first Streamlit command:
st.set_page_config(page_title="Splash", layout="wide")

# Hide the sidebar (optional)
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

# Example: we link to page "2_Onboarding" in the same `pages/` folder.
# The name "2_Onboarding" must match the file name "2_Onboarding.py" (minus .py).
onboarding_page_path = "/2_Onboarding"  

# Or if you want to navigate to the main script (no 'pages/'):
# onboarding_page_path = "/"

# The HTML below:
#  - a big clickable area
#  - the heart icon
#  - "Please wait... (click anywhere to continue)"
splash_html = f"""
<div onclick="window.location.href='{onboarding_page_path}'"
     style="min-height:100vh; background: linear-gradient(to bottom right, #ccefff, #ccffe0);
            display:flex; align-items:center; justify-content:center; cursor:pointer;">
  <div style="text-align:center;">
    <div style="width:8rem; height:8rem; background-color:white; border-radius:50%;
                display:flex; align-items:center; justify-content:center; margin:0 auto;
                box-shadow:0 0 10px rgba(0,0,0,0.2);">
      <i class="fa-solid fa-heart-pulse" style="font-size:3rem; color:#3b82f6;"></i>
    </div>
    <h1 style="font-size:2.5rem; color:#1f2937; margin-top:1rem;">VitalScan</h1>
    <p style="font-size:1.25rem; color:#1f2937;">Contactless Health Monitoring</p>
    <p style="margin-top:1rem; font-size:0.875rem; color:#6b7280;">
      Please wait... (click anywhere to continue)
    </p>
  </div>
</div>
"""

st.markdown(splash_html, unsafe_allow_html=True)

