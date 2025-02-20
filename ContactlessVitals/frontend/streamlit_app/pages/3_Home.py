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
        st.markdown("---")
        # Centered heading for Step X
        st.markdown(
            f"""
            <h3 style="text-align: center; margin-bottom:0.5rem;">
                Step {i}: {step['title']}
            </h3>
            """,
            unsafe_allow_html=True
        )
        # Centered image (via inline HTML)
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="{step['image_url']}" style="width:200px; border-radius:4px;" />
            </div>
            """,
            unsafe_allow_html=True
        )
        # Centered description
        st.markdown(
            f"""
            <p style="text-align: center; color:#4B5563; margin-top:0.5rem;">
                {step["description"]}
            </p>
            """,
            unsafe_allow_html=True
        )
    st.markdown("---")
    
# 4) Pinned Footer with real Streamlit button, forcing the button to be blue
footer_html = """
<style>
.footer-fixed {
    position: fixed;
    bottom: 0; left: 0; right: 0;
    padding: 1rem; /* Keep the padding */
    text-align: center;
    z-index: 9999;
    margin: 0;
}
/* Force the button inside the pinned footer to be blue */
.footer-fixed button {
    display: block;
    margin: 0 auto;  /* Center the button */
    width: auto !important; /* Adjust width as needed */
    background-color: #3B82F6 !important; /* Force button background */
    color: #FFFFFF !important;
    font-size: 1rem !important;
    font-weight: 500 !important;
    border-radius: 0.5rem !important;
    border: none !important;
    padding: 0.75rem 1.5rem !important;
    cursor: pointer;
}
.footer-fixed button:hover {
    background-color: #2563EB !important;
}
</style>
<div class="footer-fixed">
    <button id="my-button" type="button" class="stButton">Got It, Let's Start</button>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)


# Inject JavaScript to handle the button click and Streamlit updates
st.markdown("""
<script>
    const button = document.getElementById('my-button');
    button.addEventListener('click', function() {
        // Send a message to Streamlit
        Streamlit.set({ 'button_clicked': true }); // Using Streamlit.set
    });
</script>
""", unsafe_allow_html=True)

# Important: Initialize the button_clicked state
if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False

if st.session_state.button_clicked:
    st.info("Tutorial complete! (placeholder)")
    st.session_state.button_clicked = False # Reset to prevent multiple triggers
