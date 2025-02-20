import streamlit as st

st.set_page_config(page_title="How to Measure Your Vitals", layout="wide")

# Inject custom CSS for layout, cards, pinned footer, etc.
st.markdown("""
<style>
/* White background for the entire page */
body, [data-testid="stAppViewContainer"], [data-testid="stApp"], .block-container {
    background-color: #FFFFFF !important;
    margin: 0;
    padding: 0;
    font-family: sans-serif;
}

/* Remove extra top/bottom padding, add space for pinned footer */
main .block-container {
    padding-top: 2rem !important;
    padding-bottom: 6rem !important; /* space above pinned footer */
}

/* Centered container for heading & steps */
.center-container {
    max-width: 700px;
    margin: 0 auto;
    text-align: center;
}

/* Heading style */
.center-container h1 {
    font-size: 1.875rem;  /* ~ text-3xl */
    font-weight: 700;
    color: #111827;
    margin-bottom: 0.5rem;
}
.center-container p.subtitle {
    font-size: 1rem;      /* text-base */
    color: #4B5563;
    margin-bottom: 2rem;
}

/* Container that holds the 3 steps (stacked) */
.steps-wrapper {
    display: flex;
    flex-direction: column;
    gap: 1.5rem; /* spacing between cards */
}

/* Each step card */
.step-card {
    background-color: #FFFFFF;
    border: 1px solid #E5E7EB;
    box-shadow: 0 2px 4px rgba(0,0,0,0.08);
    border-radius: 0.5rem;
    padding: 2rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: relative;
}

/* Step number badge in top-left corner */
.step-badge {
    position: absolute;
    top: 1rem;
    left: 1rem;
    background-color: #E5E7EB;
    color: #111827;
    width: 2rem;
    height: 2rem;
    border-radius: 9999px; /* circle */
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.875rem;
    font-weight: 600;
}

/* Step text container (title + description) */
.step-text {
    flex: 1;
    text-align: left;
    margin-right: 1.5rem; /* space between text and image */
}

/* Step title */
.step-title {
    font-size: 1.125rem; /* ~ text-lg */
    font-weight: 700;
    color: #111827;
    margin-bottom: 0.5rem;
}
/* Step description */
.step-desc {
    font-size: 1rem;
    color: #4B5563;
    line-height: 1.4;
}

/* Step image on the right side (bigger than 80px) */
.step-image {
    width: 140px;
    height: 100px;
    object-fit: cover;
    border-radius: 0.25rem;
    background-color: #F9FAFB;
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

##########################
# Main Container
##########################
st.markdown('<div class="center-container">', unsafe_allow_html=True)

# Page heading
st.markdown("""
<h1>How to Measure Your Vitals</h1>
<p class="subtitle">Follow these simple steps for accurate measurements</p>
""", unsafe_allow_html=True)

# Steps container
st.markdown('<div class="steps-wrapper">', unsafe_allow_html=True)

# Step data
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

# Render each step as a "card"
for step in steps:
    st.markdown(f"""
    <div class="step-card">
      <div class="step-badge">{step['step_num']}</div>
      <div class="step-text">
        <div class="step-title">{step['title']}</div>
        <div class="step-desc">{step['description']}</div>
      </div>
      <img src="{step['image_url']}" alt="Step image" class="step-image" />
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # close steps-wrapper
st.markdown('</div>', unsafe_allow_html=True)  # close center-container

##########################
# Pinned Footer
##########################
st.markdown('<div class="footer-fixed">', unsafe_allow_html=True)
if st.button("Got It, Let’s Start"):
    st.success("Tutorial complete! (placeholder)")
st.markdown("</div>", unsafe_allow_html=True)

