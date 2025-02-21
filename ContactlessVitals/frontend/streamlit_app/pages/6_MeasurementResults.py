import streamlit as st

st.set_page_config(page_title="Measurement Results", layout="wide")

# Top row: Page Title (left), "Share Results" (right)
col1, col2 = st.columns([6,1])
with col1:
    st.markdown("<h2 style='margin:0;'>Measurement Results</h2>", unsafe_allow_html=True)
    st.write("Taken on March 12, 2024 at 2:30 PM")  # or dynamic date/time
with col2:
    # "Share Results" button top right
    if st.button("Share Results"):
        st.write("Sharing results... (placeholder)")

st.write("---")

# 4 cards side by side: Blood Pressure, Pulse Rate, SpO2, Respiratory Rate
colA, colB = st.columns(2)
with colA:
    # Left column: Blood Pressure & Pulse Rate
    st.markdown("""
    <div style="
        border:1px solid #E5E7EB; 
        border-radius:0.5rem; 
        padding:1rem; 
        margin-bottom:1rem;
    ">
      <h4 style="margin:0;">Blood Pressure <span style="float:right;color:green;">Normal</span></h4>
      <p style="font-size:1.25rem;margin:0;">120/80 <span style="font-size:0.75rem;">mmHg</span></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
        border:1px solid #E5E7EB; 
        border-radius:0.5rem; 
        padding:1rem; 
    ">
      <h4 style="margin:0;">Pulse Rate <span style="float:right;color:green;">Normal</span></h4>
      <p style="font-size:1.25rem;margin:0;">72 <span style="font-size:0.75rem;">BPM</span></p>
    </div>
    """, unsafe_allow_html=True)

with colB:
    # Right column: SpO2 & Respiratory Rate
    st.markdown("""
    <div style="
        border:1px solid #E5E7EB; 
        border-radius:0.5rem; 
        padding:1rem; 
        margin-bottom:1rem;
    ">
      <h4 style="margin:0;">SpO<span style="font-size:0.8rem;">2</span> <span style="float:right;color:green;">Normal</span></h4>
      <p style="font-size:1.25rem;margin:0;">98% <span style="font-size:0.75rem;">Oxygen Saturation</span></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
        border:1px solid #E5E7EB; 
        border-radius:0.5rem; 
        padding:1rem; 
    ">
      <h4 style="margin:0;">Respiratory Rate <span style="float:right;color:green;">Normal</span></h4>
      <p style="font-size:1.25rem;margin:0;">16 <span style="font-size:0.75rem;">Breaths per minute</span></p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# Bottom row: "Return Home" and "Retake Measurement"
colX, colY, colZ = st.columns([1,1,1])
with colX:
    if st.button("Return Home"):
        st.write("Returning home... (placeholder)")

with colZ:
    if st.button("Retake Measurement"):
        st.write("Retaking measurement... (placeholder)")
