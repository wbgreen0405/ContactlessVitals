import streamlit as st

onboarding_html = """
<div style="min-height:100vh; background-color:white; display:flex; flex-direction:column;">
  <header style="padding:1rem; display:flex; justify-content:space-between; align-items:center;">
    <!-- "Skip" goes to Home -->
    <a href="?page=3_Home" style="text-decoration:none; color:#6B7280; font-size:0.875rem;">Skip</a>
    <div style="display:flex; gap:0.5rem;">
      <div style="width:0.5rem; height:0.5rem; border-radius:50%; background-color:#111827;"></div>
      <div style="width:0.5rem; height:0.5rem; border-radius:50%; background-color:#d1d5db;"></div>
      <div style="width:0.5rem; height:0.5rem; border-radius:50%; background-color:#d1d5db;"></div>
    </div>
  </header>
  <main style="padding:1rem; flex-grow:1;">
    <div style="width:100%; height:18rem; background-color:#f3f4f6; border-radius:1rem;
                display:flex; align-items:center; justify-content:center; margin-bottom:3rem;">
      <i class="fa-solid fa-camera" style="color:#6b7280; font-size:3rem;"></i>
    </div>
    <h1 style="font-size:1.875rem; font-weight:bold; color:#111827;">Contactless Vital Signs</h1>
    <p style="font-size:1.125rem; color:#4b5563;">
      Monitor your health vitals using just your smartphone camera. No additional devices needed.
    </p>
  </main>
  <footer style="padding:1rem;">
    <!-- "Get Started" navigates to Measurement -->
    <a href="?page=4_Measurement" style="display:block; text-align:center; width:100%; background-color:#111827; color:white; padding:1rem; border:none; border-radius:0.75rem; font-weight:600; text-decoration:none;">
      Get Started
    </a>
  </footer>
</div>
"""

st.write(onboarding_html, unsafe_allow_html=True)

