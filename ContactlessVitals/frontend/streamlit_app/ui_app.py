import streamlit as st
import streamlit.components.v1 as components

# -------------------------------------------------
# 1) Tailwind + FontAwesome + minimal global styles
# -------------------------------------------------
TAILWIND_HEADER = """
<head>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
      window.FontAwesomeConfig = { autoReplaceSvg: 'nest' };
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/js/all.min.js"
          crossorigin="anonymous" referrerpolicy="no-referrer"></script>
  <style>
      * {
          font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
      }
      ::-webkit-scrollbar {
          display: none;
      }
  </style>
</head>
"""

# -------------------------------------------------
# SPLASH SCREEN
# -------------------------------------------------
SPLASH_SCREEN_HTML = f"""
<html>
  {TAILWIND_HEADER}
  <body class="min-h-screen bg-gradient-to-br from-blue-200 to-teal-200 flex items-center justify-center">
    <div class="text-center">
      <div class="w-32 h-32 bg-white rounded-full flex items-center justify-center shadow-lg mx-auto">
          <i class="fa-solid fa-heart-pulse text-blue-500 text-5xl"></i>
      </div>
      <h1 class="text-4xl font-bold text-blue-900 mt-6">VitalScan</h1>
      <p class="text-lg text-teal-800 mt-2">Contactless Health Monitoring</p>
    </div>
  </body>
</html>
"""

# -------------------------------------------------
# ONBOARDING SCREEN
#  - "Skip" => ?screen=Home
#  - "Get Started" => ?screen=Measurement
# -------------------------------------------------
ONBOARDING_HTML = f"""
<html>
  {TAILWIND_HEADER}
  <body class="min-h-screen bg-white flex flex-col">
    <header class="p-4 flex justify-between items-center">
      <!-- 'Skip' link navigates to Home -->
      <a href="?screen=Home" class="text-sm text-gray-500">Skip</a>
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
          <p class="text-lg text-gray-600">
            Monitor your health vitals using just your smartphone camera. No additional devices needed.
          </p>
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
      <!-- 'Get Started' => Measurement -->
      <button onclick="window.location.search='?screen=Measurement'"
              class="w-full bg-gray-900 text-white py-4 rounded-xl font-semibold">
        Get Started
      </button>
    </footer>
  </body>
</html>
"""

# -------------------------------------------------
# HOME SCREEN
# -------------------------------------------------
HOME_HTML = f"""
<html>
  {TAILWIND_HEADER}
  <body class="min-h-screen bg-gray-100">
    <header class="p-4 flex justify-between items-center bg-white">
      <h1 class="text-xl font-bold">Welcome Back</h1>
      <img src="https://api.dicebear.com/7.x/notionists/svg?scale=200&seed=123"
           class="w-10 h-10 rounded-full"/>
    </header>
    <main class="p-4 space-y-6">
      <div class="bg-white p-6 rounded-xl shadow-sm">
          <div class="text-center">
              <h2 class="text-2xl font-bold">Wellness Score</h2>
              <div class="text-5xl font-bold my-4">85</div>
              <p class="text-gray-600">Good Condition</p>
          </div>
      </div>
      <!-- Additional content here... -->
    </main>
  </body>
</html>
"""

# -------------------------------------------------
# MEASUREMENT SCREEN
# -------------------------------------------------
MEASUREMENT_HTML = f"""
<html>
  {TAILWIND_HEADER}
  <body class="min-h-screen bg-gray-900">
    <header class="fixed top-0 left-0 right-0 p-4 flex justify-between items-center bg-gray-800">
      <a href="?screen=Home" class="text-white"><i class="fa-solid fa-arrow-left text-xl"></i></a>
      <h1 class="text-white text-xl">Measure Vitals</h1>
      <button class="text-white"><i class="fa-solid fa-gear text-xl"></i></button>
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
  </body>
</html>
"""

# -------------------------------------------------
# Dictionary of screens
# -------------------------------------------------
SCREENS = {
    "Splash": SPLASH_SCREEN_HTML,
    "Onboarding": ONBOARDING_HTML,
    "Home": HOME_HTML,
    "Measurement": MEASUREMENT_HTML,
}


def main():
    st.set_page_config(page_title="Contactless Mobile Vital Signs", layout="wide")

    # 1) Read the query param "screen"
    #    st.query_params is a property, so we access it like a dict, not as a function
    qparams = st.query_params
    screen_param = qparams.get("screen", ["Splash"])[0]

    # 2) Fallback to "Splash" if unknown
    if screen_param not in SCREENS:
        screen_param = "Splash"

    # 3) Render the chosen screen's HTML
    html_code = SCREENS[screen_param]
    components.html(html_code, height=900, scrolling=True)

    # (Optional) If you do not want a second nav, do NOT add any radio or st.sidebar here.
    # This ensures the only nav is from your HTML links or buttons.


if __name__ == "__main__":
    main()
