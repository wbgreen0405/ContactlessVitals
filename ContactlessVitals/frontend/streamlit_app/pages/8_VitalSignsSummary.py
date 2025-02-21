import streamlit as st

st.set_page_config(page_title="Vital Signs Summary", layout="wide")

# Top row: Title on left, "Share Results" on right
col1, col2 = st.columns([6,1])
with col1:
    st.markdown("<h2 style='margin:0;'>Vital Signs Summary</h2>", unsafe_allow_html=True)
with col2:
    if st.button("Share Results"):
        st.write("Sharing results... (placeholder)")

st.write("---")

# 4 cards side by side: BP, Heart Rate, SpO2, Respiratory Rate
colA, colB = st.columns([2,2])

with colA:
    st.markdown("""
    <div style="
        border:1px solid #E5E7EB; 
        border-radius:0.5rem; 
        padding:1rem; 
        margin-bottom:1rem;
    ">
      <h4 style="margin:0;">Blood Pressure <span style="float:right;color:green;">Normal</span></h4>
      <p style="margin:0;">Your blood pressure is within healthy range</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
        border:1px solid #E5E7EB; 
        border-radius:0.5rem; 
        padding:1rem; 
    ">
      <h4 style="margin:0;">SpO<span style="font-size:0.8rem;">2</span> <span style="float:right;color:green;">Normal</span></h4>
      <p style="margin:0;">Your oxygen saturation is optimal</p>
    </div>
    """, unsafe_allow_html=True)

with colB:
    st.markdown("""
    <div style="
        border:1px solid #E5E7EB; 
        border-radius:0.5rem; 
        padding:1rem; 
        margin-bottom:1rem;
    ">
      <h4 style="margin:0;">Heart Rate <span style="float:right;color:green;">Normal</span></h4>
      <p style="margin:0;">Your heart rate indicates good cardiovascular health</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
        border:1px solid #E5E7EB; 
        border-radius:0.5rem; 
        padding:1rem; 
    ">
      <h4 style="margin:0;">Respiratory Rate <span style="float:right;color:green;">Normal</span></h4>
      <p style="margin:0;">Your breathing rate is within normal range</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# Bottom button: "Take New Reading"
colX, colY, colZ = st.columns([2,1,2])
with colY:
    # Minimal styling to make it blue
    st.markdown("""
    <style>
    .new-reading-btn button {
        background-color: #3B82F6 !important;
        color: #FFFFFF !important;
        font-weight: 500 !important;
        border-radius: 0.5rem !important;
        border: none !important;
        padding: 0.75rem 1.5rem !important;
    }
    .new-reading-btn button:hover {
        background-color: #2563EB !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("<div class='new-reading-btn' style='text-align:center;'>", unsafe_allow_html=True)
    if st.button("Take New Reading"):
        st.write("Taking new reading... (placeholder)")
    st.markdown("</div>", unsafe_allow_html=True)
