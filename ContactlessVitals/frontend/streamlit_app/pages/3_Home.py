import streamlit as st

# Set page config; force wide mode.
st.set_page_config(page_title="How to Take Measurements", layout="wide")

# --- Custom CSS for light theme and pinned footer ---
st.markdown("""
<style>
/* Force light background */
body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: #F9FAFB !important;
    margin: 0;
    padding: 0;
    font-family: sans-serif;
}

/* Pinned footer styling */
.footer-fixed {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #3B82F6;  /* Bright blue */
    padding: 1rem;
    text-align: center;
    z-index: 9999;
}

/* Ensure Streamlit's container has no extra padding */
main .block-container {
    padding-top: 1rem !important;
    padding-bottom: 5rem !important;  /* leave space for footer */
}
</style>
""", unsafe_allow_html=True)

# --- Top Bar: Back Arrow & Skip Button ---
col_arrow, col_skip = st.columns([0.1, 0.9])
with col_arrow:
    # Back arrow (simulate with a simple arrow button)
    if st.button("←", key="back"):
        st.info("Back arrow pressed (placeholder)")
with col_skip:
    # Align Skip to the right using empty space
    if st.button("Skip", key="skip"):
        st.warning("Skipping tutorial... (placeholder)")

# --- Main Heading ---
st.markdown("""
<div style="text-align: center; margin-top: 1rem; margin-bottom: 1rem;">
  <h1 style="font-size: 1.875rem; font-weight: 700; color: #111827;">How to Take Measurements</h1>
  <p style="font-size: 1rem; color: #4B5563;">Follow these steps for accurate readings</p>
</div>
""", unsafe_allow_html=True)

# --- Carousel Simulation Using Streamlit ---
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

slides = [
    {
        "image": "https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png",
        "title": "Position Your Camera",
        "description": "Hold your phone 12 inches from your face in good lighting"
    },
    {
        "image": "https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png",
        "title": "Stay Still",
        "description": "Remain steady and breathe normally during measurement"
    },
    {
        "image": "https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png",
        "title": "Wait 30 Seconds",
        "description": "The scan will take about 30 seconds to complete"
    }
]

def prev_slide():
    st.session_state.slide_index = (st.session_state.slide_index - 1) % len(slides)

def next_slide():
    st.session_state.slide_index = (st.session_state.slide_index + 1) % len(slides)

current_slide = slides[st.session_state.slide_index]

with st.container():
    # Create a card-like container for the slide
    st.markdown("""
    <div style="
      max-width: 600px;
      margin: 0 auto;
      background-color: #FFFFFF;
      border: 1px solid #E5E7EB;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
      border-radius: 0.5rem;
      padding: 1rem;
      text-align: center;">
    """, unsafe_allow_html=True)
    
    st.image(current_slide["image"], width=256)
    st.markdown(f"<h4 style='font-size:1.25rem; font-weight:700; color:#374151; margin-top:1rem;'>{current_slide['title']}</h4>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:1rem; color:#4B5563; margin-top:0.5rem;'>{current_slide['description']}</p>", unsafe_allow_html=True)
    
    # Navigation arrows: use two columns to place Prev/Next buttons side-by-side
    nav_col1, nav_col2 = st.columns(2)
    with nav_col1:
        if st.button("←", key="prev_slide"):
            prev_slide()
    with nav_col2:
        if st.button("→", key="next_slide"):
            next_slide()
    
    st.markdown("</div>", unsafe_allow_html=True)

# --- Pinned Footer: "Got It, Let's Start" Button ---
# We add a fixed footer using our custom CSS from above.
st.markdown('<div class="footer-fixed"></div>', unsafe_allow_html=True)
# Place the actual Streamlit button for "Got It, Let's Start"
# We use st.empty() to overlay it in our layout.
footer_col = st.columns(1)[0]
if st.button("Got It, Let's Start", key="got_it"):
    st.success("Tutorial complete! (placeholder)")
