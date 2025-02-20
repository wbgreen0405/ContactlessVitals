import streamlit as st

st.set_page_config(layout="wide", page_title="Camera Access Required")

# Inject CSS for background and reduced padding
st.markdown("""
<style>
/* Light gray page background */
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
</style>
""", unsafe_allow_html=True)

# 1. Page Title & Subtitle (centered)
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

# 2. Card: "Enable Camera Access"
#    We'll open a <div> with card styling, place text, then do st.button, then close the </div>.
st.markdown("""
<div style="
  background-color: #FFFFFF; 
  border: 1px solid #E5E7EB; 
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  border-radius: 0.5rem; 
  padding: 2rem; 
  max-width: 600px; 
  margin: 0 auto 2rem auto; /* center horizontally + bottom margin */
  text-align: center;">
  
  <!-- Icon -->
  <svg style="width:64px; height:64px; color:#3b82f6; margin-bottom:1rem;"
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
    margin-bottom: 1.5rem;
    line-height: 1.5;">
    Your camera will only be used during vital measurements. No videos or images are stored.
  </p>
""", unsafe_allow_html=True)

# Actual Streamlit button
if st.button("Allow Camera Access"):
    st.success("Camera access granted! (Placeholder)")

# Close the card's div
st.markdown("</div>", unsafe_allow_html=True)

# 3. Card: "Privacy Guarantee"
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
  <ul style="
    list-style-type: disc; 
    list-style-position: inside; 
    margin: 1rem auto 1.5rem auto; 
    max-width: 400px; 
    padding: 0; 
    text-align: left; 
    color: #4B5563;       /* text-base-600 */
    font-size: 1rem;">
    <li>All measurements are processed locally on your device</li>
    <li>Your data is encrypted and never shared without consent</li>
    <li>You can delete your data at any time</li>
  </ul>
""", unsafe_allow_html=True)

# Actual Streamlit button for "Read Privacy Policy"
if st.button("Read Privacy Policy"):
    st.info("Privacy policy details here (placeholder).")

# Close the card's div
st.markdown("</div>", unsafe_allow_html=True)
