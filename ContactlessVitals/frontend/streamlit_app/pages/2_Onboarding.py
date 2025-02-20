import streamlit as st

# Use wide mode so we have more horizontal space
st.set_page_config(layout="wide", page_title="Camera Access Required")

# Inject some global CSS to get the light gray background and remove extra padding
st.markdown("""
<style>
/* Light gray background for the whole page */
body {
    background-color: #F9FAFB;
    margin: 0;
    padding: 0;
    font-family: sans-serif;
}
/* Remove top/bottom padding in main block container */
main .block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
}
</style>
""", unsafe_allow_html=True)

# 1. Header Section (Title & Subtitle)
st.markdown(
    """
    <h1 style="
        text-align: center; 
        font-size: 1.875rem;  /* text-3xl */
        font-weight: 700;     /* font-bold */
        color: #111827;       /* near-black text */
        margin-bottom: 0.5rem;">
      Camera Access Required
    </h1>
    <p style="
        text-align: center; 
        font-size: 1rem;      /* text-base */
        color: #4B5563;       /* text-base-600 */
        margin-bottom: 2rem;">
      To measure your vital signs accurately, ContactlessVitals needs access to your device's camera.
    </p>
    """,
    unsafe_allow_html=True
)

# 2. Card: Enable Camera Access
st.markdown(
    """
    <div style="
        background-color: #FFFFFF; 
        border: 1px solid #E5E7EB; 
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border-radius: 0.5rem; 
        padding: 2rem; 
        max-width: 600px; 
        margin: 0 auto 2rem auto; 
        text-align: center;">
        
      <!-- Camera icon -->
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
          font-size: 1.25rem;   /* text-xl */
          font-weight: 700;     /* font-bold */
          color: #374151;       /* text-base-700 */
          margin-bottom: 1rem;">
        Enable Camera Access
      </h2>
      <p style="
          font-size: 1rem; 
          color: #4B5563;       /* text-base-600 */
          margin-bottom: 1.5rem;
          line-height: 1.5;">
        Your camera will only be used during vital measurements. No videos or images are stored.
      </p>

      <!-- "Allow Camera Access" button -->
      <form action="#" method="post">
        <button type="submit" style="
            background-color: #3B82F6; /* text-primary-500 */
            color: #fff;              /* text-primary-content */
            padding: 0.75rem 1.5rem;  /* px-5 py-3 */
            font-size: 1rem;
            font-weight: 500;         /* font-medium */
            border: none;
            border-radius: 0.5rem;    /* rounded-lg */
            cursor: pointer;
            transition: background-color 0.2s ease-in-out;">
          Allow Camera Access
        </button>
      </form>
    </div>
    """,
    unsafe_allow_html=True
)

# 3. Card: Privacy Guarantee
st.markdown(
    """
    <div style="
        background-color: #FFFFFF; 
        border: 1px solid #E5E7EB; 
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border-radius: 0.5rem; 
        padding: 2rem; 
        max-width: 600px; 
        margin: 0 auto; 
        text-align: center;">
        
      <h2 style="
          font-size: 1.25rem;   /* text-xl */
          font-weight: 700;     /* font-bold */
          color: #374151;       /* text-base-700 */
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

      <div style="margin-top: 1rem;">
        <a href="#" style="
            font-size: 0.875rem; /* text-sm */
            color: #3B82F6;      /* text-primary */
            text-decoration: underline;">
          Read Privacy Policy
        </a>
      </div>
    </div>
    """,
    unsafe_allow_html=True
)
