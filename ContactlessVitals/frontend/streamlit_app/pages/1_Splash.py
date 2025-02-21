import streamlit as st

st.set_page_config(page_title="ContactlessVitals", layout="centered")

# Minimal CSS for a "mobile-like" single column layout
st.markdown("""
<style>
body, [data-testid="stAppViewContainer"], [data-testid="stApp"], .block-container {
    background-color: #F9FAFB !important;
    margin: 0; 
    padding: 0;
    font-family: sans-serif;
    text-align: center;
}

/* Container for everything */
.landing-container {
    max-width: 400px;
    margin: 0 auto;
    padding: 2rem 1rem;
}

/* Logo + Title */
.logo {
    width: 50px;
    margin: 0 auto 1rem auto;
    display: block;
}
.app-name {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

/* Hero image */
.hero-img {
    width: 100%;
    max-width: 250px;
    border-radius: 1rem;
    margin: 0 auto 1.5rem auto;
    display: block;
}

/* Main heading + subheading */
.main-heading {
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}
.subheading {
    font-size: 0.9rem;
    color: #4B5563;
    margin-bottom: 1.5rem;
}

/* 4 "cards" in a 2x2 grid for vitals */
.vitals-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 0.75rem;
    margin-bottom: 1.5rem;
}
.vital-card {
    background-color: #FFFFFF;
    border: 1px solid #E5E7EB;
    border-radius: 0.5rem;
    padding: 0.75rem;
    font-size: 0.85rem;
    font-weight: 600;
    color: #111827;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
}

/* The blue "Get Started" button style */
.blue-btn button {
    background-color: #6366F1 !important; /* or #3B82F6 if you prefer */
    color: #FFFFFF !important;
    font-size: 1rem !important;
    font-weight: 500 !important;
    border-radius: 0.5rem !important;
    border: none !important;
    padding: 0.75rem 1.5rem !important;
    cursor: pointer;
    max-width: 250px;
    margin: 0 auto;
    display: block;
}
.blue-btn button:hover {
    background-color: #4F46E5 !important; /* or #2563EB if using #3B82F6 above */
}

/* Sign in link */
.signin-link {
    display: block;
    margin-top: 1rem;
    color: #6366F1;
    text-decoration: none;
    font-size: 0.9rem;
}
.signin-link:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# Main container
st.markdown('<div class="landing-container">', unsafe_allow_html=True)

# 1) Logo + name
st.markdown("""
<img src="https://via.placeholder.com/50?text=CV" alt="Logo" class="logo" />
<div class="app-name">ContactlessVitals</div>
""", unsafe_allow_html=True)

# 2) Hero image
st.markdown("""
<img src="https://storage.googleapis.com/uxpilot-auth.appspot.com/21f77f5a4e-c5c01269354811e51d0c.png" 
     alt="african american person using phone for health monitoring, digital art style, medical app interface" 
     class="hero-img" />
""", unsafe_allow_html=True)

# 3) Headings
st.markdown("""
<div class="main-heading">Monitor Your Vitals</div>
<p class="subheading">
Personalized vital sign monitoring using your phone's camera. 
Calibrated for all skin tones.
</p>
""", unsafe_allow_html=True)

# 4) 4 "cards" for vitals
st.markdown('<div class="vitals-grid">', unsafe_allow_html=True)
st.markdown("""
<div class="vital-card">❤️<br/>Blood Pressure</div>
<div class="vital-card">🔃<br/>Pulse Rate</div>
<div class="vital-card">🩸<br/>SpO₂ Levels</div>
<div class="vital-card">🌬<br/>Respiratory Rate</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 5) "Get Started" button + "Sign In" link
st.markdown('<div class="blue-btn">', unsafe_allow_html=True)
start_clicked = st.button("Get Started")
st.markdown('</div>', unsafe_allow_html=True)

if start_clicked:
    st.success("Starting measurement... (placeholder)")

# Sign In link
st.markdown('<a href="#" class="signin-link">Sign In</a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # close landing-container
