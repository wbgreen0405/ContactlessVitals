import streamlit as st

# Use wide mode and set a page title
st.set_page_config(layout="wide", page_title="Camera Access Required")

# Inject CSS for styling the background, cards, headings, buttons, etc.
st.markdown("""
<style>
/* Overall page background (similar to bg-gray-50) */
body {
    background-color: #F9FAFB;
    margin: 0;
    padding: 0;
    font-family: sans-serif;
}

/* Container that centers content and controls width */
.container {
    max-width: 600px;
    margin: 0 auto;
    padding: 2rem 1rem;
    text-align: center;
}

/* Page title style (Camera Access Required) */
.container h1 {
    font-size: 1.875rem;  /* text-3xl */
    font-weight: 700;     /* font-bold */
    color: #111827;       /* near-black text */
    margin-bottom: 0.5rem;
}

/* Subtitle paragraph under the title */
.container .subtitle {
    font-size: 1rem;      /* text-base */
    color: #4B5563;       /* text-base-600 */
    margin-bottom: 2rem;
}

/* Card styles */
.card {
    background-color: #FFFFFF;
    border: 1px solid #E5E7EB; /* border-base-200 */
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    border-radius: 0.5rem;     /* rounded-lg */
    padding: 2rem;
    margin-bottom: 1.5rem;
    text-align: center;
}

/* Card heading (e.g. "Enable Camera Access") */
.card h2 {
    font-size: 1.25rem;   /* text-xl */
    font-weight: 700;     /* font-bold */
    color: #374151;       /* text-base-700 */
    margin-bottom: 1rem;
}

/* Regular paragraph inside cards */
.card p {
    font-size: 1rem;      /* text-base */
    color: #4B5563;       /* text-base-600 */
    margin-bottom: 1.5rem;
    line-height: 1.5;
}

/* Blue button (Allow Camera Access) */
.button-primary {
    display: inline-block;
    background-color: #3B82F6; /* text-primary-500 */
    color: #FFFFFF;           /* text-primary-content */
    padding: 0.75rem 1.5rem;  /* px-5 py-3 */
    font-size: 1rem;
    font-weight: 500;         /* font-medium */
    border: none;
    border-radius: 0.5rem;    /* rounded-lg */
    cursor: pointer;
    transition: background-color 0.2s ease-in-out;
}

/* Hover state for the primary button */
.button-primary:hover {
    background-color: #2563EB; /* hover:bg-primary-600 */
}

/* Privacy Guarantee list styling */
.privacy-list {
    text-align: left;
    list-style: disc inside;
    margin: 1rem auto 1.5rem auto;
    max-width: 400px;
    padding: 0;
    color: #1f2937; /* text-base-content */
    font-size: 1rem;
}

/* Each bullet item */
.privacy-list li {
    margin-bottom: 0.5rem;
}

/* "Read Privacy Policy" link-like button */
.button-link {
    display: inline-block;
    margin-top: 1rem;
    font-size: 0.875rem; /* text-sm */
    color: #3B82F6;      /* text-primary */
    text-decoration: underline;
    cursor: pointer;
}

/* SVG icon styling (camera icon, lock icon, etc.) */
.icon {
    width: 64px;
    height: 64px;
    color: #3B82F6;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)

# Page container
st.markdown("""
<div class="container">

  <!-- Page Title -->
  <h1>Camera Access Required</h1>
  <p class="subtitle">
    To measure your vital signs accurately, ContactlessVitals needs access to your device's camera.
  </p>

  <!-- Card 1: Enable Camera Access -->
  <div class="card">
    <!-- Camera icon -->
    <svg class="icon" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
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

    <h2>Enable Camera Access</h2>
    <p>Your camera will only be used during vital measurements. No videos or images are stored.</p>

    <!-- "Allow Camera Access" button -->
    <button class="button-primary">Allow Camera Access</button>
  </div>

  <!-- Card 2: Privacy Note -->
  <div class="card">
    <h2>Privacy Guarantee</h2>
    <ul class="privacy-list">
      <li>All measurements are processed locally on your device</li>
      <li>Your data is encrypted and never shared without consent</li>
      <li>You can delete your data at any time</li>
    </ul>
    <div class="button-link">Read Privacy Policy</div>
  </div>

</div>
""", unsafe_allow_html=True)
