import streamlit as st

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="Measurement", layout="wide")

st.markdown("""
<div class="min-h-screen bg-gray-900">
  <header class="fixed top-0 left-0 right-0 p-4 flex justify-between items-center bg-gray-800">
    <button onclick="window.parent.location.href='?page=Home'" style="background:none;border:none;color:white;">
      <i class="fa-solid fa-arrow-left text-xl"></i>
    </button>
    <h1 class="text-white text-xl">Measure Vitals</h1>
    <button style="background:none;border:none;color:white;">
      <i class="fa-solid fa-gear text-xl"></i>
    </button>
  </header>
  <div class="pt-16 h-[400px] mx-4 mt-6 rounded-2xl overflow-hidden relative">
    <div class="absolute inset-0 flex items-center justify-center">
      <!-- Placeholder for live video feed -->
      <div class="w-full h-full bg-black flex items-center justify-center">
        <span class="text-white text-2xl">Live Camera Feed</span>
      </div>
      <!-- Face scan overlay -->
      <div class="absolute inset-0 flex items-center justify-center">
        <div class="w-48 h-48 border-4 border-white rounded-full"></div>
      </div>
    </div>
    <div class="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-gray-900">
      <p class="text-white text-center mb-2">Position your face within the circle</p>
      <div class="w-full bg-gray-700 rounded-full h-2">
        <div class="bg-white w-3/4 h-2 rounded-full"></div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)
