import streamlit as st

# Must be first
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

# HTML content
splash_html = """
<html>
<head>
  <!-- Use CSS link for Font Awesome -->
  <link rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
        integrity="sha512-..."
        crossorigin="anonymous"
        referrerpolicy="no-referrer" />
  <style>
    body {
      margin:0; padding:0;
      font-family: sans-serif;
    }
    .splash-container {
      min-height:100vh;
      background: linear-gradient(to bottom right, #ccefff, #ccffe0);
      display:flex;
      align-items:center;
      justify-content:center;
      cursor:pointer;
    }
    .white-circle {
      width:8rem; height:8rem;
      background-color:white;
      border-radius:50%;
      display:flex;
      align-items:center;
      justify-content:center;
      margin:0 auto;
      box-shadow:0 0 10px rgba(0,0,0,0.2);
    }
    .title {
      font-size:2.5rem; 
      color:#1f2937; 
      margin-top:1rem;
    }
    .subtitle {
      font-size:1.25rem; 
      color:#1f2937;
    }
    .prompt {
      margin-top:1rem; 
      font-size:0.875rem; 
      color:#6b7280;
    }
  </style>
</head>
<body>
  <div class="splash-container" onclick="window.location.href='/2_Onboarding'">
    <div style="text-align:center;">
      <div class="white-circle">
        <!-- Using fa-solid fa-heart to test. 
             If you want fa-heart-pulse, change to fa-heart-pulse. -->
        <i class="fa-solid fa-heart" style="font-size:3rem; color:#3b82f6;"></i>
      </div>
      <h1 class="title">VitalScan</h1>
      <p class="subtitle">Contactless Health Monitoring</p>
      <p class="prompt">Please wait... (click anywhere to continue)</p>
    </div>
  </div>
</body>
</html>
"""

st.write(splash_html, unsafe_allow_html=True)
