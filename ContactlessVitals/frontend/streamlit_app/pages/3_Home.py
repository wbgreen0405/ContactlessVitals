import streamlit as st

st.set_page_config(page_title="How to Measure Your Vitals", layout="wide")

# 1) Title & Subtitle (centered using columns)
colA, colB, colC = st.columns([1, 2, 1])
with colB:
    st.title("How to Measure Your Vitals")
    st.write("Follow these simple steps for accurate measurements")

# 2) Steps Data
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

# 3) Steps (centered in the middle column)
colX, colY, colZ = st.columns([1, 2, 1])
with colY:
    for i, step in enumerate(steps, start=1):
        # Horizontal rule between steps
        st.markdown("---")

        # Step title
        st.markdown(f"### Step {i}: {step['title']}")

        # Centered image (via inline HTML)
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="{step['image_url']}" style="width:200px; border-radius:4px;" />
            </div>
            """,
            unsafe_allow_html=True
        )

        # Description
        st.write(step["description"])

    st.markdown("---")

# 4) Pinned Footer with minimal HTML + real Streamlit button
footer_html = """
<style>
.footer-bar {
    position: fixed;
    bottom: 0; left: 0; right: 0;
    background-color: #3B82F6;
    padding: 1rem;
    text-align: center;
    margin: 0;
    z-index: 9999;
}
.footer-btn {
    display: block;
    margin: 0 auto;
    max-width: 300px;
    font-weight: 500;
}
</style>
<div class="footer-bar" id="pinned-footer"></div>
"""
st.markdown(footer_html, unsafe_allow_html=True)

# We'll create a placeholder for the button, so it doesn't push up the pinned bar
button_ph = st.empty()
with button_ph.container():
    button_clicked = st.button("Got It, Let's Start", key="pinned-btn")

if button_clicked:
    st.info("Tutorial complete! (placeholder)")
