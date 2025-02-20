import streamlit as st

st.set_page_config(page_title="How to Take Measurements", layout="wide")

# Inject custom CSS
st.markdown("""
<style>
/* Entire page: pure white background */
body, [data-testid="stAppViewContainer"], [data-testid="stApp"], .block-container {
    background-color: #FFFFFF !important;
    margin: 0; 
    padding: 0;
    font-family: sans-serif;
}
/* Remove default Streamlit padding, leave space for pinned footer */
main .block-container {
    padding-top: 1rem !important;
    padding-bottom: 6rem !important; /* space above pinned footer */
}

/* Top bar row with arrow (left) and skip (right) */
.top-bar {
    margin-bottom: 1rem;
}

/* Pinned footer at bottom (blue bar) */
.footer-fixed {
    position: fixed;
    bottom: 0; left: 0; right: 0;
    background-color: #3B82F6;
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

/* Centered container for the big image and text */
.center-container {
    max-width: 600px;
    margin: 0 auto;       /* center horizontally */
    text-align: center;   /* center the content inside */
    padding-top: 1rem;
}

/* White card with a big image in the center */
.card {
    background-color: #FFFFFF;
    border: 1px solid #E5E7EB;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    border-radius: 0.5rem;
    padding: 2rem;
    margin-top: 1rem;
    text-align: center;
}

/* Large image in the card */
.big-image {
    display: block;
    margin: 0 auto;
    width: 256px;
    height: 256px;
    object-fit: cover;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

##########################
# 1) Top Bar with real Streamlit buttons
##########################
# Create 3 columns: arrow on the left, empty in the middle, skip on the right
col1, col2, col3 = st.columns([0.1, 0.8, 0.1])

with col1:
    if st.button("←"):
        st.info("Back arrow clicked (placeholder)")

with col2:
    st.write("")  # empty center

with col3:
    if st.button("Skip"):
        st.warning("Skipping tutorial... (placeholder)")

##########################
# 2) Centered Container with a White Card
##########################
st.markdown('<div class="center-container">', unsafe_allow_html=True)

# Heading & Subtitle
st.markdown("""
<h1 style="font-size: 1.875rem; font-weight: 700; color:#111827; margin-bottom: 0.5rem;">
  How to Take Measurements
</h1>
<p style="font-size: 1rem; color:#4B5563; margin-bottom: 2rem;">
  Follow these steps for accurate readings
</p>
""", unsafe_allow_html=True)

# White card with a big image, title, and description
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("""
<img src="https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png"
     class="big-image"
     alt="Big camera image" />

<h2 style="font-size:1.5rem; font-weight:700; color:#111827; margin-bottom:0.5rem;">
  Position Your Camera
</h2>
<p style="font-size:1rem; color:#4B5563; margin-bottom:0;">
  Hold your phone 12 inches from your face in good lighting
</p>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # close card
st.markdown('</div>', unsafe_allow_html=True)  # close center-container

##########################
# 3) Pinned Footer
##########################
st.markdown('<div class="footer-fixed">', unsafe_allow_html=True)
if st.button("Got It, Let’s Start"):
    st.success("Tutorial complete! (placeholder)")
st.markdown("</div>", unsafe_allow_html=True)
