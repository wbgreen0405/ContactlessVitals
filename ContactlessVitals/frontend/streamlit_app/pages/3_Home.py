import streamlit as st

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="Home", layout="wide")

st.markdown("""
<div class="min-h-screen bg-gray-100">
  <header class="p-4 flex justify-between items-center bg-white">
    <h1 class="text-xl font-bold">Welcome Back</h1>
    <img src="https://api.dicebear.com/7.x/notionists/svg?scale=200&seed=123" class="w-10 h-10 rounded-full"/>
  </header>
  <main class="p-4">
    <div class="bg-white p-6 rounded-xl shadow-sm">
      <div class="text-center">
        <h2 class="text-2xl font-bold">Wellness Score</h2>
        <div class="text-5xl font-bold my-4">85</div>
        <p class="text-gray-600">Good Condition</p>
      </div>
    </div>
  </main>
</div>
""", unsafe_allow_html=True)
