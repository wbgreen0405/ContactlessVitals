import streamlit as st

st.set_page_config(page_title="How to Measure Your Vitals", layout="wide")

# 1) Title & subtitle at the top (centered using columns)
colA, colB, colC = st.columns([1,2,1])
with colB:
    st.title("How to Measure Your Vitals")
    st.write("Follow these steps for accurate measurements")

# 2) Steps data
steps = [
    {
        "title": "Position Your Face",
        "description": "Center your face in the camera frame at arm's length distance",
        "image_url": "https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png"
    },
    {
        "title": "Ensure Good Lighting",
        "description": "Find a well-lit area, avoid backlighting",
        "image_url": "https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png"
    },
    {
        "title": "Stay Still",
        "description": "Hold your device steady for 30 seconds during measurement",
        "image_url": "https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png"
    },
]

# 3) Center the steps in the middle column
col1, col2, col3 = st.columns([1,2,1])
with col2:
    for i, step in enumerate(steps, start=1):
        # Each step "card"
        st.markdown(f"### Step {i}: {step['title']}")
        st.image(step["image_url"], width=200)
        st.write(step["description"])
        st.markdown("---")

# 4) Pinned footer using HTML for absolute positioning
#    We'll place a Streamlit button inside it.
st.markdown("""
<style>
.pinned-footer {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #3B82F6;
    padding: 1rem;
    text-align: center;
    z-index: 9999;
    margin: 0;
}
.pinned-footer .center-btn {
    display: block;
    margin: 0 auto;
    max-width: 300px;
}
</style>

<div class="pinned-footer" id="footer-area">
</div>
""", unsafe_allow_html=True)

# 5) Insert a real Streamlit button inside that pinned footer.
#    We'll "trick" Streamlit into placing the button's HTML inside #footer-area
footer_ph = st.empty()  # placeholder to hold the button
with footer_ph.container():
    # The container's HTML will appear after the pinned-footer <div> in the DOM,
    # but we can style it to appear over it. Alternatively, we can
    # place the button in normal flow and rely on the pinned bar behind it.
    button_clicked = st.button("Got It, Let's Start", key="got_it_btn")

# If the user clicks, show a small message in normal flow (not pushing pinned bar up).
if button_clicked:
    st.write("Tutorial complete! (placeholder)")
