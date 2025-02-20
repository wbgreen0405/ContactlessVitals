import streamlit as st

# Hide the sidebar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="Onboarding", layout="wide")

st.markdown("""
<div class="min-h-screen bg-white flex flex-col">
  <header class="p-4 flex justify-between items-center">
    <!-- "Skip" button navigates to Home -->
    <button onclick="window.parent.location.href='/';" style="background:none;border:none;color:#6B7280;font-size:0.875rem;">Skip</button>
    <div class="flex space-x-2">
       <div class="w-2 h-2 rounded-full bg-gray-900"></div>
       <div class="w-2 h-2 rounded-full bg-gray-300"></div>
       <div class="w-2 h-2 rounded-full bg-gray-300"></div>
    </div>
  </header>
  <main class="px-6 pt-8 flex-grow">
    <div class="w-full h-72 bg-gray-100 rounded-2xl flex items-center justify-center mb-12">
        <i class="fa-solid fa-camera text-gray-500 text-6xl"></i>
    </div>
    <div class="space-y-6">
        <h1 class="text-3xl font-bold text-gray-900">Contactless Vital Signs</h1>
        <p class="text-lg text-gray-600">Monitor your health vitals using just your smartphone camera. No additional devices needed.</p>
    </div>
    <div class="mt-12 space-y-6">
        <div class="flex items-center gap-4">
            <div class="w-12 h-12 bg-gray-100 rounded-full flex items-center justify-center">
                <i class="fa-solid fa-camera text-gray-600"></i>
            </div>
            <div>
                <h3 class="font-semibold text-gray-900">Face Scan Technology</h3>
                <p class="text-sm text-gray-600">Quick 30-second face scan for all vitals</p>
            </div>
        </div>
        <div class="flex items-center gap-4">
            <div class="w-12 h-12 bg-gray-100 rounded-full flex items-center justify-center">
                <i class="fa-solid fa-chart-line text-gray-600"></i>
            </div>
            <div>
                <h3 class="font-semibold text-gray-900">Real-time Monitoring</h3>
                <p class="text-sm text-gray-600">Track BP, SPO2, Heart & Respiratory Rate</p>
            </div>
        </div>
        <div class="flex items-center gap-4">
            <div class="w-12 h-12 bg-gray-100 rounded-full flex items-center justify-center">
                <i class="fa-solid fa-clock-rotate-left text-gray-600"></i>
            </div>
            <div>
                <h3 class="font-semibold text-gray-900">History & Trends</h3>
                <p class="text-sm text-gray-600">View your progress over time</p>
            </div>
        </div>
    </div>
  </main>
  <footer class="p-6">
    <!-- "Get Started" button navigates to Measurement -->
    <button onclick="window.parent.location.href='?page=Measurement'" style="width:100%;background-color:#1F2937;color:white;padding:1rem;border:none;border-radius:0.75rem;font-weight:600;">
      Get Started
    </button>
  </footer>
</div>
""", unsafe_allow_html=True)

# (Alternatively, you can use st.button and st.switch_page in Python code.)
