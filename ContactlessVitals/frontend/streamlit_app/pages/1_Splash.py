import streamlit as st

st.set_page_config(layout="wide")

# Inject custom CSS to remove Streamlit’s default top spacing and remove all margin/padding
st.markdown("""
<style>
/* Remove default padding/margins on html and body */
html, body {
    margin: 0 !important;
    padding: 0 !important;
    height: 100% !important;
}

/* Streamlit main app container adjustments */
[data-testid="stAppViewContainer"], [data-testid="stApp"] {
    padding: 0 !important;
    margin: 0 !important;
    height: 100% !important;
    background: none !important;
}

/* Optionally remove the top/bottom white bar if your theme has them */
.block-container, .main .block-container {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    margin: 0 !important;
}

/* Our custom container with the gradient background */
.container {
    min-height: 100vh;
    margin: 0;
    padding: 0;
    background: linear-gradient(to bottom, #eff6ff, #ffffff);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

/* Remove extra margin from the header */
.header {
    text-align: center;
    margin-top: 0 !important;
    padding-top: 0 !important;
    padding-bottom: 0 !important;
}

/* Additional styling */
.header h1 {
    font-size: 2.5rem;
    font-weight: 800;
    margin-bottom: 0.5rem;
}
.header p {
    font-size: 1.25rem;
    font-weight: 300;
    margin-bottom: 1.5rem;
}
.header img {
    width: 100%;
    max-width: 400px;
    height: auto;
    border-radius: 0.5rem;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}
.card {
    max-width: 600px;
    margin: 2rem auto;
    background: rgba(255,255,255,0.8);
    backdrop-filter: blur(10px);
    border: 1px solid #e5e7eb;
    border-radius: 0.5rem;
    padding: 24px;
}
.icon-section {
    display: flex;
    justify-content: center;
    gap: 32px;
    margin-top: 16px;
}
.icon-section div {
    text-align: center;
}
.buttons {
    max-width: 600px;
    margin: 2rem auto;
    text-align: center;
}
.buttons button {
    width: 100%;
    padding: 12px 0;
    margin-bottom: 16px;
    border: none;
    border-radius: 0.5rem;
    font-size: 1rem;
    cursor: pointer;
}
.primary {
    background-color: #3b82f6;
    color: white;
}
.link {
    background: transparent;
    color: #3b82f6;
}
</style>
""", unsafe_allow_html=True)

# Build the layout
st.markdown('<div class="container">', unsafe_allow_html=True)

st.markdown(
    """
    <div class="header">
      <h1>ContactlessVitals</h1>
      <p>Monitor your vital signs instantly using just your smartphone camera</p>
      <img src="https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png" alt="Contactless monitoring animation">
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="card">
      <div class="icon-section">
        <div>
          <svg aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" style="color:#ef4444; width:32px; height:32px; margin-bottom:8px;">
            <path fill-rule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clip-rule="evenodd"></path>
          </svg>
          <p>Heart Rate</p>
        </div>
        <div>
          <svg aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" style="color:#3b82f6; width:32px; height:32px; margin-bottom:8px;">
            <path stroke-linecap="round" stroke-linejoin="round" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path>
          </svg>
          <p>Blood Pressure</p>
        </div>
        <div>
          <svg aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" style="color:#f59e0b; width:32px; height:32px; margin-bottom:8px;">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>
          </svg>
          <p>SpO</p>
        </div>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="buttons">
      <button class="primary">Get Started</button>
      <button class="link">Already have an account? Sign in</button>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('</div>', unsafe_allow_html=True)
