import streamlit as st

st.set_page_config(page_title="Quick Start", layout="wide")

###########################
# 1) Top Bar: "Quick Start" (centered in its column), [X] on right
###########################
colA, colB = st.columns([9,1])
with colA:
    # Center "Quick Start" within colA via inline HTML
    st.markdown("<h2 style='margin:0; text-align:center; width:100%;'>Quick Start</h2>", unsafe_allow_html=True)

with colB:
    # "X" button on the right
    if st.button("✕", key="close_quickstart"):
        st.write("Closed quick start (placeholder)")

st.write("---")  # horizontal rule

###########################
# 2) "Before You Begin" Section (centered)
###########################
c1, c2, c3 = st.columns([1,2,1])
with c2:
    # Center the heading
    st.markdown("<h3 style='text-align:center;'>Before You Begin</h3>", unsafe_allow_html=True)
    # Center the bullet points via inline HTML
    st.markdown("""
    <ul style="list-style-type: disc; text-align:center; margin:0 auto; padding:0;">
      <li>Ensure good lighting on your face</li>
      <li>Keep your face relatively still</li>
      <li>Measurement takes about 30 seconds</li>
    </ul>
    """, unsafe_allow_html=True)

###########################
# 3) Large Circle in Center
###########################
col1, col2, col3 = st.columns([1,2,1])
with col2:
    # We'll use inline HTML + CSS to create a dark circle with text in the center
    st.markdown(
        """
        <div style="
            width:100%; 
            max-width:400px; 
            aspect-ratio:1 / 1; 
            background-color:#1F2937; 
            border-radius:50%; 
            margin:2rem auto; 
            display:flex; 
            align-items:center; 
            justify-content:center;
        ">
            <p style="color:#FFFFFF; text-align:center; margin:0;">
                Position your face within the circle
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

###########################
# 4) "Start Measurement" Button (blue)
###########################
colA2, colB2, colC2 = st.columns([1,2,1])
with colB2:
    # Minimal CSS to force the button blue
    st.markdown("""
    <style>
    .start-btn button {
        display: block;
        margin: 0 auto;
        background-color: #3B82F6 !important;
        color: #FFFFFF !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
        border-radius: 0.5rem !important;
        border: none !important;
        padding: 0.75rem 1.5rem !important;
        max-width: 300px;
        cursor: pointer;
    }
    .start-btn button:hover {
        background-color: #2563EB !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='start-btn'>", unsafe_allow_html=True)
    if st.button("Start Measurement", key="start_measure"):
        st.success("Measurement started (placeholder).")
    st.markdown("</div>", unsafe_allow_html=True)
