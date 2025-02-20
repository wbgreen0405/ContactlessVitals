import streamlit as st

st.set_page_config(page_title="How to Take Measurements", layout="wide")

# 1) Enforce a light background & pinned footer
st.markdown("""
<style>
/* Force a near-white background */
body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: #F9FAFB !important;
    margin: 0; padding: 0;
    font-family: sans-serif;
}
/* Remove default Streamlit top/bottom padding */
main .block-container {
    padding-top: 1rem !important;
    padding-bottom: 6rem !important; /* leave space for pinned footer */
}
/* Pinned bright-blue footer at bottom */
.footer-fixed {
    position: fixed;
    bottom: 0; left: 0; right: 0;
    background-color: #3B82F6;
    padding: 1rem;
    text-align: center;
    z-index: 9999;
    margin: 0;
}
/* Style the button in the pinned footer */
.footer-fixed .stButton button {
    width: 100% !important;
    background-color: #3B82F6 !important;
    color: #FFFFFF !important;
    font-size: 1rem !important;
    font-weight: 500 !important;
    border-radius: 0.5rem !important;
    border: none !important;
    padding: 0.75rem 1.5rem !important;
    margin: 0 !important;
    cursor: pointer;
}
.footer-fixed .stButton button:hover {
    background-color: #2563EB !important;
}
</style>
""", unsafe_allow_html=True)

# 2) Top Bar (arrow on left, skip on right)
col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
with col1:
    # Arrow button on the left
    if st.button("←"):
        st.info("Back arrow clicked (placeholder)")
with col2:
    st.write("")  # empty space in the middle
with col3:
    # "Skip" button on the right
    if st.button("Skip"):
        st.warning("Skipping tutorial... (placeholder)")

# 3) Heading & Subtitle (centered)
st.markdown(
    """
    <div style="text-align: center; margin-top: 1rem; margin-bottom: 1rem;">
      <h1 style="font-size: 1.875rem; font-weight: 700; color: #111827;">How to Take Measurements</h1>
      <p style="font-size: 1rem; color: #4B5563;">Follow these steps for accurate readings</p>
    </div>
    """,
    unsafe_allow_html=True
)

# 4) Carousel slides (simulate a card in the center)
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

# Center the card with a container & columns
card_col = st.columns([1, 2, 1])[1]
with card_col:
    st.markdown("""
    <div style="
      background-color: #FFFFFF;
      border: 1px solid #E5E7EB;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
      border-radius: 0.5rem;
      padding: 1rem;
      text-align: center;">
    """, unsafe_allow_html=True)

    st.image(current_slide["image"], width=200)
    st.markdown(f"""
    <h4 style="font-size:1.25rem; font-weight:700; color:#374151; margin-top:1rem;">
      {current_slide['title']}
    </h4>
    <p style="font-size:1rem; color:#4B5563; margin-top:0.5rem;">
      {current_slide['description']}
    </p>
    """, unsafe_allow_html=True)

    # Prev / Next in a row
    nav1, nav2, nav3 = st.columns(3)
    with nav1:
        if st.button("←", key="prev"):
            prev_slide()
    with nav2:
        st.write("")
    with nav3:
        if st.button("→", key="next"):
            next_slide()

    st.markdown("</div>", unsafe_allow_html=True)

# 5) Pinned Footer: "Got It, Let's Start"
st.markdown('<div class="footer-fixed">', unsafe_allow_html=True)
got_it = st.button("Got It, Let's Start", key="got_it_btn")
st.markdown('</div>', unsafe_allow_html=True)

if got_it:
    st.success("Tutorial complete! (placeholder)")
