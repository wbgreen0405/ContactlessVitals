import streamlit as st

st.set_page_config(page_title="How to Take Measurements", layout="wide")

# 1) Inject CSS for a light background, pinned footer, and centered wide button
st.markdown("""
<style>
/* Force a near-white background */
body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: #F9FAFB !important;
    margin: 0;
    padding: 0;
    font-family: sans-serif;
}
/* Remove default Streamlit top/bottom padding, add bottom space for pinned footer */
main .block-container {
    padding-top: 1rem !important;
    padding-bottom: 6rem !important; /* space for pinned footer */
}
/* Pinned bright-blue footer at bottom */
.footer-fixed {
    position: fixed;
    bottom: 0; left: 0; right: 0;
    background-color: #3B82F6; /* bright blue */
    padding: 1rem;
    text-align: center;  /* center the button horizontally */
    z-index: 9999;
    margin: 0;
}
/* Style the button in the pinned footer */
.footer-fixed .stButton button {
    width: 100% !important;       /* Make button wide */
    max-width: 300px;            /* Optionally limit how wide it can get */
    margin: 0 auto !important;   /* Center the button horizontally */
    background-color: #3B82F6 !important;
    color: #FFFFFF !important;
    font-size: 1rem !important;  /* text-base */
    font-weight: 500 !important; /* font-medium */
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

# 2) Top Bar: arrow on left, skip on right
col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
with col1:
    # Arrow button on the left
    if st.button("←"):
        st.info("Back arrow clicked (placeholder)")
with col2:
    st.write("")  # empty center
with col3:
    # "Skip" on the right
    if st.button("Skip"):
        st.warning("Skipping tutorial... (placeholder)")

# 3) Heading & Subtitle (centered)
st.markdown("""
<div style="text-align: center; margin-top: 1rem; margin-bottom: 1.5rem;">
  <h1 style="font-size: 1.875rem; font-weight: 700; color: #111827;">How to Take Measurements</h1>
  <p style="font-size: 1rem; color: #4B5563;">Follow these steps for accurate readings</p>
</div>
""", unsafe_allow_html=True)

# 4) Steps in a single card, each with an icon, title, and description (all centered)
steps = [
    {
        "icon": """<svg style="width:64px; height:64px; color:#3B82F6; display:block; margin:0 auto;"
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
        "icon": """<svg style="width:64px; height:64px; color:#3B82F6; display:block; margin:0 auto;"
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
        "icon": """<svg style="width:64px; height:64px; color:#3B82F6; display:block; margin:0 auto;"
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

# Center the card
card_col = st.columns([1, 2, 1])[1]
with card_col:
    st.markdown("""
    <div style="
      background-color: #FFFFFF;
      border: 1px solid #E5E7EB;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
      border-radius: 0.5rem;
      padding: 2rem;
      text-align: center;">
    """, unsafe_allow_html=True)

    # Display each step stacked, with centered icon, title, and text
    for step in steps:
        st.markdown(step["icon"], unsafe_allow_html=True)
        st.markdown(f"""
        <h4 style="font-size:1.25rem; font-weight:700; color:#374151; margin-top:0.75rem;">
          {step['title']}
        </h4>
        <p style="font-size:1rem; color:#4B5563; margin-top:0.25rem; margin-bottom:1.75rem;">
          {step['description']}
        </p>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# 5) Pinned Footer: "Got It, Let's Start" (centered, wide, bright blue)
st.markdown('<div class="footer-fixed">', unsafe_allow_html=True)
if st.button("Got It, Let's Start"):
    st.success("Tutorial complete! (placeholder)")
st.markdown('</div>', unsafe_allow_html=True)
