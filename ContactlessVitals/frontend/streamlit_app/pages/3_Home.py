import streamlit as st

st.set_page_config(page_title="How to Measure Your Vitals", layout="wide")

# Inject custom CSS
st.markdown("""
<style>
/* Set a light background and remove extra padding */
body, [data-testid="stAppViewContainer"], [data-testid="stApp"], .block-container {
    background-color: #F9FAFB !important;
    margin: 0;
    padding: 0;
    font-family: sans-serif;
}
main .block-container {
    padding-top: 2rem !important;
    padding-bottom: 6rem !important;
}

/* Center container for the heading and subheading */
.center-container {
    max-width: 700px;
    margin: 0 auto;
    text-align: center;
}

/* Pinned footer styling */
.footer-fixed {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #3B82F6; /* Blue background */
    padding: 1rem;
    text-align: center;
    z-index: 9999;
    margin: 0;
}
.footer-fixed .stButton button {
    display: block;
    margin: 0 auto;
    width: 100% !important;
    max-width: 300px;
    background-color: #3B82F6 !important;
    color: #FFFFFF !important;
    font-size: 1rem !important;
    font-weight: 500 !important;
    border-radius: 0.5rem !important;
    border: none !important;
    padding: 0.75rem 1.5rem !important;
    cursor: pointer;
}
.footer-fixed .stButton button:hover {
    background-color: #2563EB !important;
}
</style>
""", unsafe_allow_html=True)

# Centered heading and subtitle
st.markdown('<div class="center-container">', unsafe_allow_html=True)
st.markdown("""
<h1>How to Measure Your Vitals</h1>
<p>Follow these simple steps for accurate measurements</p>
""", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Pinned footer with a blue, centered button
st.markdown('<div class="footer-fixed">', unsafe_allow_html=True)
if st.button("Got It, Let's Go"):
    st.success("Tutorial complete! (placeholder)")
st.markdown("</div>", unsafe_allow_html=True)
