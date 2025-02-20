import streamlit as st

# Must be the first Streamlit command
st.set_page_config(page_title="Splash", layout="wide")

# Optionally hide Streamlit’s sidebar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True
)

splash_html = """
<html>
<head>
  <link rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
        integrity="sha512-..."
        crossorigin="anonymous"
        referrerpolicy="no-referrer" />
  <style>
    body {
      margin: 0; padding: 0;
      font-family: sans-serif;
      background: linear-gradient(to bottom right, #ccefff, #ccffe0);
    }
    .splash-container {
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    /* Anchor covers the entire area, no underline, same tab */
    .full-link {
      text-decoration: none;
      color: inherit;
      display: block;
      text-align: center;
      padding: 2rem;
    }
    .full-link:hover {
      text-decoration: none; /* ensure no underline on hover */
    }
    .white-circle {
      width: 8rem; height: 8rem;
      background-color: white;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto;
      box-shadow: 0 0 10px rgba(0,0,0,0.2);
    }
    .icon-heart {
      font-size: 3rem;
      color: #3b82f6; /* a nice blue color */
    }
    .title {
      font-size: 2.5rem;
      color: #1f2937;
      margin-top: 1rem;
    }
    .subtitle {
      font-size: 1.25rem;
      color: #1f2937;
    }
    .prompt {
      margin-top: 1rem;
      font-size: 0.875rem;
      color: #6b7280;
    }
  </style>
</head>
<body>
  <div class="splash-container">
    <!-- Anchor link that navigates in the same tab -->
    <!-- Use target="_self" to ensure same tab. Adjust href to your actual page. -->
    <a class="full-link" href="?page=Onboarding" target="_self">
      <div class="white-circle">
        <i class="fa-solid fa-heart icon-heart"></i>
      </div>
      <h1 class="title">VitalScan</h1>
      <p class="subtitle">Contactless Health Monitoring</p>
      <p class="prompt">Please wait... (click anywhere to continue)</p>
    </a>
  </div>
</body>
</html>
"""

st.write(splash_html, unsafe_allow_html=True)
