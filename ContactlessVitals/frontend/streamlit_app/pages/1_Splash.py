import streamlit as st

# This must be the very first command in your page.
st.set_page_config(page_title="Splash", layout="wide")

# Hide the sidebar.
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True
)

# Tailwind CSS, FontAwesome, and minimal custom styles.
tailwind_header = """
<head>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
      window.FontAwesomeConfig = { autoReplaceSvg: 'nest' };
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/js/all.min.js"
          crossorigin="anonymous" referrerpolicy="no-referrer"></script>
  <style>
    * { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; }
    ::-webkit-scrollbar { display: none; }
    a { text-decoration: none; }
    a:hover { text-decoration: none; }
    /* Optionally, limit the content width */
    #welcome-screen { max-width: 800px; margin: 0 auto; }
  </style>
</head>
"""

# The complete HTML for the welcome (splash) screen.
# Note: Change the href in the anchor tag to match your multipage URL.
welcome_html = f"""
{tailwind_header}
<body class="h-full text-base-content">
  <div id="welcome-screen" class="min-h-screen bg-gradient-to-b from-blue-50 to-white p-6 flex flex-col justify-between">
    <!-- Top section with title, subtitle, and image -->
    <div class="text-center space-y-6 mt-12">
      <h1 class="text-4xl font-extrabold leading-tight tracking-tight text-base-900">
        ContactlessVitals
      </h1>
      <p class="text-xl font-light leading-relaxed text-base-700">
        Monitor your vital signs instantly using just your smartphone camera
      </p>
      <div class="w-full max-w-md mx-auto">
        <img src="https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png"
             alt="Contactless monitoring animation"
             class="w-full h-64 object-cover rounded-xl shadow-lg" />
      </div>
    </div>
    <!-- Bottom section: Icons and the clickable heart button -->
    <div class="space-y-6 text-center mt-12">
      <div class="flex justify-center items-center space-x-6">
        <!-- Heart Rate Icon -->
        <div class="flex flex-col items-center">
          <svg class="h-8 w-8 text-red-500 mb-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
               fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clip-rule="evenodd"></path>
          </svg>
          <p class="text-base text-gray-600">Heart Rate</p>
        </div>
        <!-- Blood Pressure Icon -->
        <div class="flex flex-col items-center">
          <svg class="h-8 w-8 text-blue-500 mb-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
               fill="currentColor" viewBox="0 0 20 20">
            <path stroke-linecap="round" stroke-linejoin="round"
                  d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z">
            </path>
          </svg>
          <p class="text-base text-gray-600">Blood Pressure</p>
        </div>
        <!-- SpO Icon -->
        <div class="flex flex-col items-center">
          <svg class="h-8 w-8 text-yellow-500 mb-1" aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
               fill="currentColor" viewBox="0 0 20 20">
            <path stroke-linecap="round" stroke-linejoin="round"
                  d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z">
            </path>
          </svg>
          <p class="text-base text-gray-600">SpO</p>
        </div>
      </div>
      <!-- The clickable heart icon acting as a navigation button -->
      <a href="?page=2_Onboarding" target="_self" style="display:inline-block; margin-top: 2rem;">
        <div class="w-20 h-20 bg-white rounded-full flex items-center justify-center shadow-lg mx-auto">
          <i class="fa-solid fa-heart-pulse text-blue-500 text-4xl"></i>
        </div>
      </a>
      <p class="mt-2 text-sm text-gray-600">Tap the heart to get started</p>
    </div>
  </div>
</body>
"""

st.markdown(welcome_html, unsafe_allow_html=True)
