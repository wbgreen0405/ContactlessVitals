import streamlit as st

st.set_page_config(page_title="How to Measure Your Vitals", layout="wide")

# Inject custom CSS
st.markdown("""
<style>
/* Make the entire page white, remove extra spacing */
body, [data-testid="stAppViewContainer"], [data-testid="stApp"], .block-container {
    background-color: #FFFFFF !important;
    margin: 0; 
    padding: 0;
    font-family: sans-serif;
}

/* Reduce default top/bottom padding, leave space for pinned footer */
main .block-container {
    padding-top: 2rem !important;
    padding-bottom: 6rem !important; /* space for pinned footer */
}

/* Centered container for heading & steps */
.center-container {
    max-width: 700px; /* narrower container */
    margin: 0 auto;   /* center horizontally */
    text-align: center;
}

/* Heading & subheading */
.center-container h1 {
    font-size: 1.875rem; /* ~ text-3xl */
    font-weight: 700;
    color: #111827;
    margin-bottom: 0.5rem;
}
.center-container p.subtitle {
    font-size: 1rem; /* text-base */
    color: #4B5563;
    margin-bottom: 2rem;
}

/* Steps wrapper (stack them vertically, center them) */
.steps-wrapper {
    display: flex;
    flex-direction: column;
    gap: 1.5rem; /* spacing between cards */
    align-items: center; /* center each card horizontally */
    width: 100%;
}

/* Each step card is narrower and centered */
.step-card {
    width: 100%;
    max-width: 600px; /* narrower card width */
    background-color: #FFFFFF;
    border: 1px solid #E5E7EB;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    border-radius: 0.5rem;
    padding: 1.5rem;
    position: relative;
    text-align: left; /* text inside left-aligned, if desired */
    display: flex;
    align-items: center;
    justify-content: space-between;
}

/* Step number in top-left corner */
.step-badge {
    position: absolute;
    top: 1rem;
    left: 1rem;
    background-color: #E5E7EB;
    color: #111827;
    width: 1.5rem;
    height: 1.5rem;
    border-radius: 9999px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.75rem;
    font-weight: 600;
}

/* Step text area */
.step-text {
    flex: 1; 
    margin-right: 1rem;
}

/* Step title */
.step-title {
    font-size: 1.125rem; /* ~ text-lg */
    font-weight: 700;
    color: #111827;
    margin-bottom: 0.25rem;
}

/* Step description */
.step-desc {
    font-size: 1rem;
    color: #4B5563;
}

/* Step image on the right */
.step-image {
    width: 80px;
    height: 80px;
    object-fit: cover;
    border-radius: 0.25rem;
}

/* Pinned footer (blue bar) */
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

#####################################
# Main Container
#####################################
st.markdown('<div class="center-container">', unsafe_allow_html=True)

# Heading & subheading
st.markdown("""
<h1>How to Measure Your Vitals</h1>
<p class="subtitle">Follow these simple steps for accurate measurements</p>
""", unsafe_allow_html=True)

# Steps container
st.markdown('<div class="steps-wrapper">', unsafe_allow_html=True)

# Example steps data
steps = [
    {
        "num": "1",
        "title": "Position Your Face",
        "desc": "Center your face in the camera frame at arm's length distance",
        "img": "https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png"
    },
    {
        "num": "2",
        "title": "Ensure Good Lighting",
        "desc": "Find a well-lit area, avoid backlighting",
        "img": "https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png"
    },
    {
        "num": "3",
        "title": "Stay Still",
        "desc": "Hold your device steady for 30 seconds during measurement",
        "img": "https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png"
    }
]

# Render each step as a narrower card, centered
for step in steps:
    st.markdown(f"""
    <div class="step-card">
      <div class="step-badge">{step['num']}</div>
      <div class="step-text">
        <div class="step-title">{step['title']}</div>
        <div class="step-desc">{step['desc']}</div>
      </div>
      <img src="{step['img']}" alt="Step image" class="step-image" />
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # close steps-wrapper
st.markdown('</div>', unsafe_allow_html=True)  # close center-container

#####################################
# Pinned Footer
#####################################
st.markdown('<div class="footer-fixed">', unsafe_allow_html=True)
if st.button("Got It, Let's Start"):
    st.success("Tutorial complete! (placeholder)")
st.markdown("</div>", unsafe_allow_html=True)
