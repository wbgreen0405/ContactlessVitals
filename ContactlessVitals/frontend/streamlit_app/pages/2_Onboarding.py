import streamlit as st

# Use wide mode so we have more horizontal space
st.set_page_config(layout="wide", page_title="Camera Access Required")

# Optional: remove some default Streamlit padding via CSS
st.markdown("""
<style>
/* Remove top and bottom padding */
main .block-container {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
}
/* Make the background a light gray (similar to bg-gray-50) */
body {
    background-color: #F9FAFB;
}
</style>
""", unsafe_allow_html=True)

# 1. Header Section
st.title("Camera Access Required")
st.write("To measure your vital signs accurately, ContactlessVitals needs access to your device's camera.")

# 2. Camera Permission Card
with st.container():
    st.markdown("---")  # horizontal rule for separation

    st.subheader("Enable Camera Access")
    st.write("Your camera will only be used during vital measurements. No videos or images are stored.")

    # Show a camera icon. You can replace with an st.image if you prefer a local file or different icon
    st.markdown(
        """
        <div style="text-align:center; margin: 1rem 0;">
          <svg style="width:64px; height:64px; color:#3b82f6;" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" 
                  d="M4 5a2 2 0 00-2 2v8a2 2 0 
                     002 2h12a2 2 0 002-2V7a2 2 0 
                     00-2-2h-1.586a1 1 0 
                     01-.707-.293l-1.121-1.121A2 
                     2 0 0011.172 3H8.828a2 2 0 
                     00-1.414.586L6.293 4.707A1 
                     1 0 015.586 5H4zm6 9a3 3 0 
                     100-6 3 3 0 000 6z" 
                  clip-rule="evenodd">
            </path>
          </svg>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Button to allow camera access
    if st.button("Allow Camera Access"):
        st.success("Camera access granted! (Example behavior)")

# 3. Privacy Note Card
with st.container():
    st.markdown("---")  # another horizontal rule

    st.subheader("Privacy Guarantee")

    # You can replicate the bullet points with st.write or st.markdown
    st.markdown("""
    - All measurements are processed locally on your device  
    - Your data is encrypted and never shared without consent  
    - You can delete your data at any time
    """)

    # "Read Privacy Policy" link-like button
    if st.button("Read Privacy Policy"):
        # In a real app, you might open a link or show more info
        st.info("Privacy policy details here (placeholder).")
