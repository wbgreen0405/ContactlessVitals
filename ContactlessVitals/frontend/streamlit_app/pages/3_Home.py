import streamlit as st

st.set_page_config(page_title="Centered Steps", layout="wide")

# Inline CSS that centers everything
st.markdown("""
<style>
/* Force a near-white background */
body, [data-testid="stAppViewContainer"], [data-testid="stApp"], .block-container {
    background-color: #F9FAFB !important;
    margin: 0; 
    padding: 0;
    font-family: sans-serif;
}

/* Remove default top/bottom padding, 
   leave space for pinned footer at bottom */
main .block-container {
    padding-top: 2rem !important;
    padding-bottom: 6rem !important;
}

/* A single container that centers everything horizontally */
.center-page {
    display: flex;
    flex-direction: column;
    align-items: center;  /* horizontally center all content */
    justify-content: flex-start;
    width: 100%;
    margin: 0 auto;
    text-align: center;   /* center text inline */
    max-width: 700px;     /* limit how wide content can get */
}

/* Each step card: minimal border, stacked content, centered text */
.step-card {
    width: 100%;
    max-width: 600px;
    border: 1px solid #E5E7EB;
    border-radius: 0.5rem;
    background-color: #FFFFFF;
    margin-bottom: 1.5rem;
    padding: 2rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
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
    margin: 0 auto 1rem auto;
}

/* Step image */
.step-image {
    width: 140px;
    height: 100px;
    object-fit: cover;
    border-radius: 0.25rem;
    background-color: #F9FAFB;
    margin: 0 auto 1rem auto;
}

/* Step title & desc */
.step-title {
    font-size: 1.125rem;
    font-weight: 700;
    color: #111827;
    margin-bottom: 0.5rem;
}
.step-desc {
    font-size: 1rem;
    color: #4B5563;
    line-height: 1.4;
}

/* Pinned footer (blue bar) at bottom */
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

# 1) Container to hold everything
st.markdown('<div class="center-page">', unsafe_allow_html=True)

# 2) Heading & subtitle
st.markdown("""
<h1 style="margin-bottom:0.5rem;">How to Measure Your Vitals</h1>
<p style="color:#4B5563; margin-bottom:2rem;">
  Follow these simple steps for accurate measurements
</p>
""", unsafe_allow_html=True)

# 3) Steps data
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

# 4) Render steps
for step in steps:
    st.markdown(f"""
    <div class="step-card">
      <div class="step-badge">{step['step_num']}</div>
      <img src="{step['image_url']}" alt="Step image" class="step-image" />
      <div class="step-title">{step['title']}</div>
      <div class="step-desc">{step['description']}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # close .center-page

# 5) Pinned footer
st.markdown('<div class="footer-fixed">', unsafe_allow_html=True)
button_clicked = st.button("Got It, Let's Start")
st.markdown("</div>", unsafe_allow_html=True)

if button_clicked:
    st.write("Button was clicked. (Placeholder)")

