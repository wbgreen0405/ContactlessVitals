import streamlit as st

st.set_page_config(page_title="How to Take Measurements", layout="wide")

# Inject custom CSS
st.markdown("""
<style>
/* Full white page background */
body, [data-testid="stAppViewContainer"], [data-testid="stApp"], .block-container {
    background-color: #FFFFFF !important;  /* pure white */
    margin: 0; 
    padding: 0;
    font-family: sans-serif;
}

/* Remove default top/bottom padding, leave space for pinned footer */
main .block-container {
    padding-top: 1rem !important;
    padding-bottom: 6rem !important; 
}

/* A top bar row for arrow (left) + skip (right). We'll use columns for the button placements. */
.top-bar-row {
    margin-bottom: 1rem;
}

/* Pinned bright-blue footer at the bottom */
.footer-fixed {
    position: fixed;
    bottom: 0; 
    left: 0; 
    right: 0;
    background-color: #3B82F6; /* bright blue */
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

/* A centered container for the heading and steps */
.centered-container {
    max-width: 600px;  /* limit total width */
    margin: 0 auto;    /* center horizontally */
    text-align: center;/* center text/icons inside */
}

/* The white card that holds the steps */
.card {
    background-color: #FFFFFF;
    border: 1px solid #E5E7EB;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    border-radius: 0.5rem;
    padding: 2rem;
    margin-top: 1rem;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

#####################################
# 1) Top Bar with real Streamlit buttons
#####################################
# We'll create a row with 3 columns: arrow in col1, empty col2, skip in col3
st.markdown('<div class="top-bar-row">', unsafe_allow_html=True)
col1, col2, col3 = st.columns([0.1, 0.8, 0.1])

with col1:
    # Arrow on the far left
    if st.button("←"):
        st.info("Back arrow clicked (placeholder)")

with col2:
    st.write("")  # empty middle space

with col3:
    # Skip on the far right
    if st.button("Skip"):
        st.warning("Skipping tutorial... (placeholder)")

st.markdown('</div>', unsafe_allow_html=True)

#####################################
# 2) Centered Container for Heading + Steps
#####################################
st.markdown('<div class="centered-container">', unsafe_allow_html=True)

# Heading & Subtitle
st.markdown("""
<h1 style="font-size: 1.875rem; font-weight: 700; color: #111827; margin-bottom: 0.5rem;">
  How to Take Measurements
</h1>
<p style="font-size: 1rem; color: #4B5563; margin-bottom: 1.5rem;">
  Follow these steps for accurate readings
</p>
""", unsafe_allow_html=True)

# Steps in a single white card
st.markdown('<div class="card">', unsafe_allow_html=True)

steps = [
    {
        "icon": """<svg style="width:64px; height:64px; color:#3B82F6; margin:0 auto;"
                         xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                     <path fill-rule="evenodd"
                           d="M4 5a2 2 0 00-2 2v8a2 2 0 
                              002 2h12a2 2 0 002-2V7a2 2 0 
                              00-2-2h-1.586a1 1 0 
                              01-.707-.293l-1.121-1.121A2 
                              2 0 0011.172 3H8.828a2 2 0 
                              00-1.414.586L6.293 4.707A1 
                              1 0 015.586 5H4zm6 9a3 3 0 
                              100-6 3 3 0 000 6z"
                           clip-rule="evenodd"/>
                   </svg>""",
        "title": "Position Your Camera",
        "description": "Hold your phone 12 inches from your face in good lighting"
    },
    {
        "icon": """<svg style="width:64px; height:64px; color:#3B82F6; margin:0 auto;"
                         xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                     <path fill-rule="evenodd"
                           d="M10 2a6 6 0 00-4.472 10.09 
                              8 8 0 018.944 0A6 6 0 
                              0010 2zm-2 7a2 2 0 114 
                              0 2 2 0 01-4 
                              0zM2 13.5a7.5 7.5 
                              0 0115 0v.45c0 
                              .786-.43 1.516-1.124 
                              1.913A13.07 13.07 0 
                              0110 17a13.07 13.07 
                              0 01-5.876-1.138A2.25 
                              2.25 0 013 13.95v-.45z"
                           clip-rule="evenodd"/>
                   </svg>""",
        "title": "Stay Still",
        "description": "Remain steady and breathe normally during measurement"
    },
    {
        "icon": """<svg style="width:64px; height:64px; color:#3B82F6; margin:0 auto;"
                         xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                     <path fill-rule="evenodd"
                           d="M10 2a8 8 0 
                              100 16 8 8 0 000-16zm1 
                              8a1 1 0 01-1 
                              1H6a1 1 0 110-2h3V5a1 
                              1 0 112 0v3z"
                           clip-rule="evenodd"/>
                   </svg>""",
        "title": "Wait 30 Seconds",
        "description": "The scan will take about 30 seconds to complete"
    }
]

for step in steps:
    # Icon
    st.markdown(step["icon"], unsafe_allow_html=True)
    # Title + Description
    st.markdown(f"""
    <h4 style="font-size:1.25rem; font-weight:700; color:#374151; margin-top:0.75rem;">
      {step['title']}
    </h4>
    <p style="font-size:1rem; color:#4B5563; margin-top:0.25rem; margin-bottom:1.75rem;">
      {step['description']}
    </p>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)  # close .card
st.markdown("</div>", unsafe_allow_html=True)  # close .centered-container

#####################################
# 4) Pinned Footer
#####################################
st.markdown('<div class="footer-fixed">', unsafe_allow_html=True)
if st.button("Got It, Let's Start"):
    st.success("Tutorial complete! (placeholder)")
st.markdown('</div>', unsafe_allow_html=True)
