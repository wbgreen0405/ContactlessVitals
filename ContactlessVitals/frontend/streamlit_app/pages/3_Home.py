import streamlit as st

st.set_page_config(page_title="How to Measure Your Vitals", layout="wide")

# 1) Inline CSS for centering + pinned footer
st.markdown("""
<style>
/* Light background for the entire page */
body, [data-testid="stAppViewContainer"], [data-testid="stApp"], .block-container {
    background-color: #F9FAFB !important; /* or transparent if you prefer */
    margin: 0; 
    padding: 0;
    font-family: sans-serif;
}

/* Remove default Streamlit padding, leave space for pinned footer */
main .block-container {
    padding-top: 2rem !important;
    padding-bottom: 6rem !important; /* space above pinned footer */
}

/* A container that centers content horizontally */
.center-container {
    max-width: 700px;
    margin: 0 auto; 
    text-align: center; 
}

/* Steps wrapper: stack them vertically, center each step */
.steps-wrapper {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    align-items: center; /* center each step horizontally */
    margin-top: 2rem;
}

/* Each step card: minimal border, stacked content, centered text */
.step-card {
    border: 1px solid #E5E7EB;
    border-radius: 0.5rem;
    padding: 2rem;
    width: 100%;
    max-width: 600px;
    display: flex;
    flex-direction: column;
    align-items: center; 
    text-align: center; 
    background-color: #FFFFFF; /* or transparent if you don't want a white box */
    box-shadow: none;
    position: relative;
}

/* Step number badge */
.step-badge {
    background-color: #E5E7EB;
    color: #111827;
    width: 2rem;
    height: 2rem;
    border-radius: 9999px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.875rem;
    font-weight: 600;
    margin-bottom: 1rem;
}

/* Step image */
.step-image {
    width: 140px;
    height: 100px;
    object-fit: cover;
    border-radius: 0.25rem;
    background-color: #F9FAFB;
    margin-bottom: 1rem;
}

/* Step title & description */
.step-title {
    font-size: 1.125rem; /* ~ text-lg */
    font-weight: 700;
    color: #111827;
    margin-bottom: 0.5rem;
}
.step-desc {
    font-size: 1rem;
    color: #4B5563;
    line-height: 1.4;
}

/* Pinned footer at the bottom (blue bar) */
.footer-fixed {
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
/* Center the pinned footer button, make it wide */
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

# 2) Main Heading
st.markdown("""
<div class="center-container">
  <h1 style="margin-bottom:0.5rem;">How to Measure Your Vitals</h1>
  <p style="color:#4B5563; margin-bottom:2rem;">Follow these simple steps for accurate measurements</p>
</div>
""", unsafe_allow_html=True)

# 3) Steps
steps = [
    {
        "step_num": "1",
        "title": "Position Your Face",
        "description": "Center your face in the camera frame at arm's length distance",
        "image_url": "https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png"
    },
    {
        "step_num": "2",
        "title": "Ensure Good Lighting",
        "description": "Find a well-lit area, avoid backlighting",
        "image_url": "https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png"
    },
    {
        "step_num": "3",
        "title": "Stay Still",
        "description": "Hold your device steady for 30 seconds during measurement",
        "image_url": "https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png"
    },
]

st.markdown('<div class="center-container"><div class="steps-wrapper">', unsafe_allow_html=True)

for step in steps:
    st.markdown(f"""
    <div class="step-card">
      <div class="step-badge">{step['step_num']}</div>
      <img src="{step['image_url']}" alt="Step image" class="step-image" />
      <div class="step-title">{step['title']}</div>
      <div class="step-desc">{step['description']}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)  # close steps-wrapper & center-container

# 4) Pinned Footer with a wide, centered button
st.markdown('<div class="footer-fixed">', unsafe_allow_html=True)
button_clicked = st.button("Got It, Let's Start")
st.markdown("</div>", unsafe_allow_html=True)

# 5) If clicked, show a small note below the button area (but won't push the pinned bar up)
if button_clicked:
    st.write("You clicked the button! (Placeholder behavior)")

