import streamlit as st

# Force wide layout
st.set_page_config(page_title="How to Take Measurements", layout="wide")

# Inject custom CSS
st.markdown("""
<style>
/* Entire page background = light/white */
body, [data-testid="stAppViewContainer"], [data-testid="stApp"], .block-container {
    background-color: #F9FAFB !important;
    margin: 0;
    padding: 0;
    font-family: sans-serif;
}

/* Remove extra top/bottom padding, leave space for pinned footer */
main .block-container {
    padding-top: 1rem !important;
    padding-bottom: 6rem !important; /* space above pinned footer */
}

/* A top bar for arrow (left) + skip (right), no columns */
.top-bar {
    position: relative;
    width: 100%;
    height: 60px;         /* fixed height for the top bar */
    background-color: #F9FAFB;
    margin-bottom: 1rem;
}
/* Arrow button pinned to the left */
.arrow-btn {
    position: absolute;
    top: 50%;
    left: 1rem;
    transform: translateY(-50%);
    background: none;
    border: none;
    cursor: pointer;
}
/* Skip button pinned to the right */
.skip-btn {
    position: absolute;
    top: 50%;
    right: 1rem;
    transform: translateY(-50%);
    background: none;
    border: none;
    cursor: pointer;
    color: #111827;
    font-size: 1rem;
}

/* Centered container for heading & steps */
.center-container {
    max-width: 600px;
    margin: 0 auto;          /* center horizontally */
    text-align: center;      /* center the text/icons inside */
    padding-top: 1rem; 
}

/* Heading & subtitle styling */
.center-container h1 {
    font-size: 1.875rem;  /* ~ text-3xl */
    font-weight: 700;     /* bold */
    color: #111827;
    margin-bottom: 0.5rem;
}
.center-container p.subtitle {
    font-size: 1rem;      /* text-base */
    color: #4B5563;
    margin-bottom: 2rem;
}

/* A card-like container for the steps */
.card {
    background-color: #FFFFFF;
    border: 1px solid #E5E7EB;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    border-radius: 0.5rem;
    padding: 2rem;
    margin-bottom: 2rem;
}

/* Step items stacked in the card */
.step-icon {
    width: 64px;
    height: 64px;
    color: #3B82F6;
    margin: 0 auto 0.75rem auto; /* center icon & add spacing below */
}
.step-title {
    font-size: 1.25rem; /* ~ text-xl */
    font-weight: 700;
    color: #374151;
    margin-bottom: 0.25rem;
}
.step-desc {
    font-size: 1rem;
    color: #4B5563;
    margin-bottom: 1.75rem;
}

/* Pinned footer at bottom, bright blue */
.footer-fixed {
    position: fixed;
    bottom: 0; left: 0; right: 0;
    background-color: #3B82F6;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
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
</style>
""", unsafe_allow_html=True)

##########################
# Top Bar
##########################
st.markdown("""
<div class="top-bar">
  <!-- Arrow button (pure HTML) -->
  <button class="arrow-btn" onclick="alert('Back arrow clicked (placeholder)')">
    <svg style="width:24px; height:24px;" fill="currentColor" viewBox="0 0 20 20">
      <path fill-rule="evenodd" 
            d="M9.707 16.707a1 1 0 01-1.414 
               0l-6-6a1 1 0 010-1.414l6-6a1 
               1 0 011.414 1.414L5.414 
               9H17a1 1 0 110 2H5.414l4.293 
               4.293a1 1 0 010 1.414z"
            clip-rule="evenodd"/>
    </svg>
  </button>

  <!-- Skip button (pure HTML) -->
  <button class="skip-btn" onclick="alert('Skip clicked (placeholder)')">
    Skip
  </button>
</div>
""", unsafe_allow_html=True)

##########################
# Centered Container
##########################
st.markdown("""
<div class="center-container">

  <h1>How to Take Measurements</h1>
  <p class="subtitle">Follow these steps for accurate readings</p>

  <div class="card">

    <!-- Step 1 -->
    <svg class="step-icon" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
      <path fill-rule="evenodd"
            d="M4 5a2 2 0 00-2 2v8a2 
               2 0 002 2h12a2 2 0 
               002-2V7a2 2 0 
               00-2-2h-1.586a1 1 0 
               01-.707-.293l-1.121-1.121A2 
               2 0 0011.172 3H8.828a2 2 0 
               00-1.414.586L6.293 4.707A1 
               1 0 015.586 5H4zm6 9a3 3 0 
               100-6 3 3 0 000 6z"
            clip-rule="evenodd"/>
    </svg>
    <div class="step-title">Position Your Camera</div>
    <div class="step-desc">Hold your phone 12 inches from your face in good lighting</div>

    <!-- Step 2 -->
    <svg class="step-icon" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
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
    </svg>
    <div class="step-title">Stay Still</div>
    <div class="step-desc">Remain steady and breathe normally during measurement</div>

    <!-- Step 3 -->
    <svg class="step-icon" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
      <path fill-rule="evenodd"
            d="M10 2a8 8 0 
               100 16 8 8 0 000-16zm1 
               8a1 1 0 01-1 
               1H6a1 1 0 110-2h3V5a1 
               1 0 112 0v3z"
            clip-rule="evenodd"/>
    </svg>
    <div class="step-title">Wait 30 Seconds</div>
    <div class="step-desc">The scan will take about 30 seconds to complete</div>

  </div> <!-- end card -->

</div> <!-- end center-container -->
""", unsafe_allow_html=True)

##########################
# Pinned Footer
##########################
st.markdown("""
<div class="footer-fixed">
""", unsafe_allow_html=True)

# A real Streamlit button so you can handle clicks in Python
if st.button("Got It, Let's Start"):
    st.success("Tutorial complete! (placeholder)")

st.markdown("</div>", unsafe_allow_html=True)
