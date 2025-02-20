import streamlit as st

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="History & Trends", layout="wide")

st.markdown("""
<div class="min-h-screen bg-white">
  <header class="fixed top-0 w-full bg-white border-b border-neutral-200 z-50">
    <div class="flex items-center justify-between px-4 py-3">
      <h1 class="text-xl font-semibold">History & Trends</h1>
      <button style="background:none;border:none;padding:0.5rem;">
        <i class="fa-solid fa-gear text-neutral-600"></i>
      </button>
    </div>
  </header>
  <main class="pt-16 pb-20 px-4">
    <div id="date-filter" class="mb-6 flex items-center justify-between">
      <select class="bg-white border border-neutral-200 rounded-lg px-4 py-2">
        <option>Last 7 Days</option>
        <option>Last 30 Days</option>
        <option>Last 3 Months</option>
      </select>
      <button class="bg-neutral-100 px-4 py-2 rounded-lg">
        <i class="fa-regular fa-calendar mr-2"></i>Custom Range
      </button>
    </div>
    <div id="vitals-cards" class="space-y-6">
      <!-- Blood Pressure Card -->
      <div class="bg-white rounded-xl p-4 shadow-sm">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-lg font-semibold">Blood Pressure</h2>
          <i class="fa-solid fa-heart-pulse text-neutral-600"></i>
        </div>
        <div class="h-[200px] bg-neutral-100 rounded-lg mb-4 flex items-center justify-center">
          <span class="text-neutral-500">Graph Placeholder</span>
        </div>
        <div class="flex justify-between text-sm text-neutral-600">
          <span>Average: 120/80</span>
          <span>Highest: 135/88</span>
          <span>Lowest: 110/70</span>
        </div>
      </div>
      <!-- Additional cards for Heart Rate and Oxygen Saturation -->
      <div class="bg-white rounded-xl p-4 shadow-sm">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-lg font-semibold">Heart Rate</h2>
          <i class="fa-solid fa-heartbeat text-neutral-600"></i>
        </div>
        <div class="h-[200px] bg-neutral-100 rounded-lg mb-4 flex items-center justify-center">
          <span class="text-neutral-500">Graph Placeholder</span>
        </div>
        <div class="flex justify-between text-sm text-neutral-600">
          <span>Average: 72 bpm</span>
          <span>Highest: 85 bpm</span>
          <span>Lowest: 65 bpm</span>
        </div>
      </div>
      <div class="bg-white rounded-xl p-4 shadow-sm">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-lg font-semibold">Oxygen Saturation</h2>
          <i class="fa-solid fa-lungs text-neutral-600"></i>
        </div>
        <div class="h-[200px] bg-neutral-100 rounded-lg mb-4 flex items-center justify-center">
          <span class="text-neutral-500">Graph Placeholder</span>
        </div>
        <div class="flex justify-between text-sm text-neutral-600">
          <span>Average: 98%</span>
          <span>Highest: 99%</span>
          <span>Lowest: 96%</span>
        </div>
      </div>
    </div>
  </main>
  <nav id="bottom-nav" class="fixed bottom-0 w-full bg-white border-t border-neutral-200">
    <div class="flex justify-around py-3">
      <button class="flex flex-col items-center">
        <i class="fa-solid fa-house text-neutral-400"></i>
        <span class="text-xs mt-1">Home</span>
      </button>
      <button class="flex flex-col items-center">
        <i class="fa-solid fa-camera text-neutral-400"></i>
        <span class="text-xs mt-1">Measure</span>
      </button>
      <button class="flex flex-col items-center">
        <i class="fa-solid fa-chart-line text-neutral-900"></i>
        <span class="text-xs mt-1">History</span>
      </button>
      <button class="flex flex-col items-center">
        <i class="fa-solid fa-book-medical text-neutral-400"></i>
        <span class="text-xs mt-1">Learn</span>
      </button>
      <button class="flex flex-col items-center">
        <i class="fa-regular fa-user text-neutral-400"></i>
        <span class="text-xs mt-1">Profile</span>
      </button>
    </div>
  </nav>
</div>
""", unsafe_allow_html=True)
