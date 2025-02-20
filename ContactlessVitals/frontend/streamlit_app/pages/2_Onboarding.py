import streamlit as st

st.set_page_config(layout="wide", page_title="Camera Access Required")

# Inject CSS for background, padding, and button styling
st.markdown("""
<style>
/* Light gray background, similar to Tailwind bg-gray-50 */
body {
    background-color: #F9FAFB;
    margin: 0;
    padding: 0;
    font-family: sans-serif;
}
/* Remove some default Streamlit padding */
main .block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
}
/* Center and style the Streamlit buttons */
.stButton > button {
    display: block;                
    margin: 1rem auto;            /* center horizontally */
    background-color: #3B82F6 !important;  /* Tailwind primary-500 */
    color: #ffffff !important;    
    border-radius: 0.5rem !important;      /* rounded-lg */
    border: none !important;
    padding: 0.75rem 1.5rem !important;    /* ~py-3 px-5 */
    font-weight: 500 !important;           /* font-medium */
    font-size: 1rem !important;            /* text-base */
    cursor: pointer;
    transition: background-color 0.2s ease-in-out;
}
.stButton > button:hover {
    background-color: #2563EB !important;  /* Tailwind primary-600 */
}
</style>
""", unsafe_allow_html=True)

# 1) Page Title & Subtitle (centered)
st.markdown("""
<div style="text-align: center; margin-bottom: 2rem;">
  <h1 style="
      font-size: 1.875rem; /* text-3xl */
      font-weight: 700;    /* font-bold */
      color: #111827;      /* near-black text */
      margin-bottom: 0.5rem;">
    Camera Access Required
  </h1>
  <p style="
      font-size: 1rem;  /* text-base */
      color: #4B5563;   /* text-base-600 */
      margin: 0 auto;">
    To measure your vital signs accurately, ContactlessVitals needs access to your device's camera.
  </p>
</div>
""", unsafe_allow_html=True)

# --------------------
# CARD 1: Enable Camera Access
# --------------------
# Open the card container (but don't close it yet)
st.markdown("""
<div style="
  background-color: #FFFFFF; 
  border: 1px solid #E5E7EB; 
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  border-radius: 0.5rem; 
  padding: 2rem; 
  max-width: 600px; 
  margin: 0 auto 2rem auto; /* center + bottom margin */
  text-align: center;">
  
  <!-- Camera icon, centered -->
  <div style="text-align: center; margin-bottom: 1rem;">
    <svg style="width:64px; height:64px; color:#3b82f6;"
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
    </svg>
  </div>

  <h2 style="
    font-size: 1.25rem; /* text-xl */
    font-weight: 700;   /* font-bold */
    color: #374151;     /* text-base-700 */
    margin-bottom: 1rem;">
    Enable Camera Access
  </h2>
  <p style="
    font-size: 1rem; 
    color: #4B5563;   /* text-base-600 */
    margin-bottom: 1rem;
    line-height: 1.5;">
    Your camera will only be used during vital measurements. No videos or images are stored.
  </p>
""", unsafe_allow_html=True)

# Place the Streamlit button *before* closing the card
if st.button("Allow Camera Access"):
    st.success("Camera access granted! (Placeholder)")

# Now close the card's div
st.markdown("</div>", unsafe_allow_html=True)

# --------------------
# CARD 2: Privacy Guarantee
# --------------------
# Open the card container
st.markdown("""
<div style="
  background-color: #FFFFFF; 
  border: 1px solid #E5E7EB; 
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  border-radius: 0.5rem; 
  padding: 2rem; 
  max-width: 600px; 
  margin: 0 auto; /* center horizontally */
  text-align: center;">
  
  <h2 style="
    font-size: 1.25rem; /* text-xl */
    font-weight: 700;   /* font-bold */
    color: #374151;     /* text-base-700 */
    margin-bottom: 1rem;">
    Privacy Guarantee
  </h2>

  <!-- Bullet points: remove max-width so it aligns nicely, or keep a narrower column if you prefer -->
  <ul style="
    list-style-type: disc; 
    list-style-position: inside; 
    margin: 0 auto 1.5rem auto; 
    padding: 0; 
    text-align: left; 
    color: #4B5563;       /* text-base-600 */
    font-size: 1rem;">
    <li style="margin-bottom: 0.5rem;">All measurements are processed locally on your device</li>
    <li style="margin-bottom: 0.5rem;">Your data is encrypted and never shared without consent</li>
    <li style="margin-bottom: 0.5rem;">You can delete your data at any time</li>
  </ul>
""", unsafe_allow_html=True)

# Place the Streamlit button for "Read Privacy Policy" here
if st.button("Read Privacy Policy"):
    st.info("Privacy policy details here (placeholder).")

# Close the card's div
st.markdown("</div>", unsafe_allow_html=True)
