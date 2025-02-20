import streamlit as st

st.set_page_config(page_title="How to Take Measurements", layout="wide")

# Inject CSS
st.markdown("""
<style>
/* Force a light background */
body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: #F9FAFB !important;
    margin: 0; padding: 0;
    font-family: sans-serif;
}
/* Remove default top/bottom padding, add space for pinned footer */
main .block-container {
    padding-top: 1rem !important;
    padding-bottom: 6rem !important; 
}
/* Top bar: arrow left, skip right */
.top-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 1.5rem;
    margin-bottom: 1rem;
}
/* Pinned footer at bottom, bright blue background */
.footer-fixed {
    position: fixed;
    bottom: 0; left: 0; right: 0;
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
    max-width: 300px; /* limit how wide it can grow */
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
/* Main card that holds all steps, centered horizontally */
.card {
    background-color: #FFFFFF;
    border: 1px solid #E5E7EB;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    border-radius: 0.5rem;
    padding: 2rem;
    max-width: 600px;
    margin: 0 auto;  /* center horizontally */
    text-align: center; /* center icons & text inside */
}
</style>
""", unsafe_allow_html=True)

#####################################
# Top Bar
#####################################
st.markdown("""
<div class="top-bar">
  <!-- Left arrow (pure HTML). If you need a Python callback, replace with st.button -->
  <button type="button" style="background:none; border:none; cursor:pointer;"
          onclick="alert('Back arrow clicked (placeholder)')">
    <svg style="width:24px; height:24px; color:#111827;" 
         xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
      <path fill-rule="evenodd" 
            d="M9.707 16.707a1 1 0 01-1.414 
               0l-6-6a1 1 0 010-1.414l6-6a1 
               1 0 011.414 1.414L5.414 
               9H17a1 1 0 110 2H5.414l4.293 
               4.293a1 1 0 010 1.414z" 
            clip-rule="evenodd"/>
    </svg>
  </button>
""", unsafe_allow_html=True)

# Right side: "Skip" as a real Streamlit button
col1, col2 = st.columns([0.8, 0.2])
with col1:
    st.write("")
with col2:
    if st.button("Skip"):
        st.warning("Skipping tutorial... (placeholder)")

# Close top bar div
st.markdown("</div>", unsafe_allow_html=True)

#####################################
# Heading & Subtitle (centered)
#####################################
st.markdown("""
<div style="text-align: center; margin-bottom: 1.5rem;">
  <h1 style="font-size: 1.875rem; font-weight: 700; color: #111827;">
    How to Take Measurements
  </h1>
  <p style="font-size: 1rem; color: #4B5563;">
    Follow these steps for accurate readings
  </p>
</div>
""", unsafe_allow_html=True)

#####################################
# Steps in a single centered card
#####################################
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

# Create the card
st.markdown('<div class="card">', unsafe_allow_html=True)
for step in steps:
    st.markdown(step["ico
