import streamlit as st

st.set_page_config(page_title="ContactlessVitals", layout="wide")

# Minimal CSS to style the page, cards, and buttons
st.markdown("""
<style>
body, [data-testid="stAppViewContainer"], [data-testid="stApp"], .block-container {
    background-color: #F9FAFB !important; /* Light background */
    margin: 0; 
    padding: 0;
    font-family: sans-serif;
}
/* A centered container for the entire page */
.landing-container {
    max-width: 600px;
    margin: 0 auto;
    text-align: center;
    padding: 2rem;
}
/* The top brand/logo */
.brand-logo {
    width: 80px;
    margin: 0 auto 1rem auto;
    display: block;
}
/* Big heading */
h1.title {
    font-size: 1.75rem;
    font-weight: 700;
    margin-bottom: 0.75rem;
}
/* Subheading text */
p.subtitle {
    font-size: 1rem;
    color: #4B5563;
    margin-bottom: 2rem;
}
/* 4 "cards" in a grid */
.features-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin-bottom: 2rem;
}
/* Each card style */
.feature-card {
    background-color: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 0.5rem;
    padding: 1rem;
    text-align: center;
    font-size: 0.9rem;
    font-weight: 500;
    color: #111827;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
}
/* Blue button style */
.blue-btn button {
    display: block;
    margin: 0 auto;
    background-color: #3B82F6 !important;
    color: #FFFFFF !important;
    font-size: 1rem !important;
    font-weight: 500 !important;
    border-radius: 0.5rem !important;
    border: none !important;
    padding: 0.75rem 1.5rem !important;
    max-width: 300px;
    cursor: pointer;
}
.blue-btn button:hover {
    background-color: #2563EB !important;
}
/* Sign in link style */
.signin-link {
    display: block;
    margin-top: 1rem;
    color: #3B82F6;
    text-decoration: none;
    font-size: 0.95rem;
}
.signin-link:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# Main container
st.markdown('<div class="landing-container">', unsafe_allow_html=True)

# 1) Logo + brand
st.markdown("""
<img src="https://via.placeholder.com/80?text=CV" alt="Logo" class="brand-logo" />
<h1 class="title">ContactlessVitals</h1>
""", unsafe_allow_html=True)

# 2) Subheading / instructions
st.markdown("""
<p class="subtitle">
Monitor your vital signs instantly using just your phone's camera. 
No additional devices needed.
</p>
""", unsafe_allow_html=True)

# 3) Four "cards" for vitals
st.markdown('<div class="features-grid">', unsafe_allow_html=True)
st.markdown("""
<div class="feature-card">❤️<br/>Blood Pressure</div>
<div class="feature-card">🔃<br/>Pulse Rate</div>
<div class="feature-card">🩸<br/>SpO₂ Levels</div>
<div class="feature-card">🌬<br/>Respiratory Rate</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 4) "Get Started" button + "Sign In" link
st.markdown('<div class="blue-btn">', unsafe_allow_html=True)
start_clicked = st.button("Get Started")
st.markdown('</div>', unsafe_allow_html=True)

if start_clicked:
    st.success("Starting measurement... (placeholder)")

# Sign In link
st.markdown('<a href="#" class="signin-link">Sign In</a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # close landing-container
