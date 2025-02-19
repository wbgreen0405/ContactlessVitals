import streamlit as st
import streamlit.components.v1 as components

# -------------------------------------------------
# 1) Tailwind + FontAwesome header snippet (common to all pages)
# -------------------------------------------------
TAILWIND_HEADER = """
<head>
  <script src="https://cdn.jsdelivr.net/npm/apexcharts"></script>
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
      window.FontAwesomeConfig = { autoReplaceSvg: 'nest' };
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/js/all.min.js"
          crossorigin="anonymous"
          referrerpolicy="no-referrer"></script>
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
# 2) SPLASH SCREEN (Light blue and teal color scheme)
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
# 3) ONBOARDING SCREEN
#    "Skip" navigates to Home; "Get Started" navigates to Measurement.
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
      <!-- 'Get Started' button navigates to Measurement page -->
      <button onclick="window.location.search='?screen=Measurement'" class="w-full bg-gray-900 text-white py-4 rounded-xl font-semibold">
        Get Started
      </button>
    </footer>
  </body>
</html>
"""

# -------------------------------------------------
# 4) HOME SCREEN (placeholder)
# -------------------------------------------------
HOME_HTML = f"""
<html>
  {TAILWIND_HEADER}
  <body class="min-h-screen bg-gray-100">
    <header class="p-4 flex justify-between items-center bg-white">
      <h1 class="text-xl font-bold">Welcome Back</h1>
      <img src="https://api.dicebear.com/7.x/notionists/svg?scale=200&seed=123" class="w-10 h-10 rounded-full"/>
    </header>
    <main class="p-4 space-y-6">
      <div class="bg-white p-6 rounded-xl shadow-sm">
          <div class="text-center">
              <h2 class="text-2xl font-bold">Wellness Score</h2>
              <div class="text-5xl font-bold my-4">85</div>
              <p class="text-gray-600">Good Condition</p>
          </div>
      </div>
      <!-- Additional content can go here -->
    </main>
  </body>
</html>
"""

# -------------------------------------------------
# 5) MEASUREMENT SCREEN (placeholder for live feed)
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
# 6) RESULTS SCREEN (placeholder)
# -------------------------------------------------
RESULTS_HTML = f"""
<html>
  {TAILWIND_HEADER}
  <body class="min-h-screen bg-white">
    <header class="p-4 bg-white border-b">
      <div class="flex items-center">
          <a href="?screen=Measurement" class="mr-4"><i class="fa-solid fa-arrow-left text-gray-600 text-xl"></i></a>
          <h1 class="text-xl font-bold text-gray-800">Scan Results</h1>
      </div>
    </header>
    <main class="p-6">
      <div class="grid grid-cols-2 gap-4">
          <!-- Blood Pressure Card -->
          <div class="bg-white p-6 rounded-xl shadow-sm">
              <div class="flex justify-between items-center mb-4">
                  <div class="flex items-center gap-2">
                      <i class="fa-solid fa-droplet text-gray-600 text-xl"></i>
                      <h2 class="text-lg font-semibold text-gray-800">Blood Pressure</h2>
                  </div>
                  <span class="px-3 py-1 bg-gray-100 text-gray-600 text-sm rounded-full">Normal</span>
              </div>
              <div class="flex items-baseline">
                  <span class="text-3xl font-bold text-gray-800">120/80</span>
                  <span class="ml-2 text-gray-500">mmHg</span>
              </div>
          </div>
          <!-- Heart Rate Card -->
          <div class="bg-white p-6 rounded-xl shadow-sm">
              <div class="flex justify-between items-center mb-4">
                  <div class="flex items-center gap-2">
                      <i class="fa-solid fa-heart text-gray-600 text-xl"></i>
                      <h2 class="text-lg font-semibold text-gray-800">Heart Rate</h2>
                  </div>
                  <span class="px-3 py-1 bg-gray-800 text-white text-sm rounded-full">High</span>
              </div>
              <div class="flex items-baseline">
                  <span class="text-3xl font-bold text-gray-800">92 BPM</span>
              </div>
          </div>
          <!-- Blood Oxygen Card -->
          <div class="bg-white p-6 rounded-xl shadow-sm">
              <div class="flex justify-between items-center mb-4">
                  <div class="flex items-center gap-2">
                      <i class="fa-solid fa-lungs text-gray-600 text-xl"></i>
                      <h2 class="text-lg font-semibold text-gray-800">Blood Oxygen</h2>
                  </div>
                  <span class="px-3 py-1 bg-gray-100 text-gray-600 text-sm rounded-full">Normal</span>
              </div>
              <div class="flex items-baseline">
                  <span class="text-3xl font-bold text-gray-800">98%</span>
              </div>
          </div>
          <!-- Respiratory Rate Card -->
          <div class="bg-white p-6 rounded-xl shadow-sm">
              <div class="flex justify-between items-center mb-4">
                  <div class="flex items-center gap-2">
                      <i class="fa-solid fa-wave-square text-gray-600 text-xl"></i>
                      <h2 class="text-lg font-semibold text-gray-800">Respiratory Rate</h2>
                  </div>
                  <span class="px-3 py-1 bg-gray-100 text-gray-600 text-sm rounded-full">Normal</span>
              </div>
              <div class="flex items-baseline">
                  <span class="text-3xl font-bold text-gray-800">16 breaths/min</span>
              </div>
          </div>
      </div>
    </main>
  </body>
</html>
"""

# -------------------------------------------------
# 7) HISTORY & TRENDS SCREEN (placeholder)
# -------------------------------------------------
HISTORY_HTML = f"""
<html>
  {TAILWIND_HEADER}
  <body class="min-h-screen bg-white">
    <header class="p-4 border-b">
      <div class="flex justify-between items-center">
          <h1 class="text-xl font-bold">History & Trends</h1>
          <i class="fa-solid fa-calendar text-gray-600 text-xl"></i>
      </div>
    </header>
    <div class="p-6">
      <div class="bg-white p-4 rounded-xl shadow-sm mb-6">
        <h2 class="font-bold text-gray-800 mb-2">Heart Rate Trends</h2>
        <!-- Placeholder for a bar chart -->
        <div class="h-48 bg-gray-100 rounded-lg flex items-end p-4">
          <div class="w-8 h-32 bg-gray-800 rounded-t-sm mx-1"></div>
          <div class="w-8 h-24 bg-gray-800 rounded-t-sm mx-1"></div>
          <div class="w-8 h-40 bg-gray-800 rounded-t-sm mx-1"></div>
          <div class="w-8 h-28 bg-gray-800 rounded-t-sm mx-1"></div>
          <div class="w-8 h-36 bg-gray-800 rounded-t-sm mx-1"></div>
          <div class="w-8 h-20 bg-gray-800 rounded-t-sm mx-1"></div>
          <div class="w-8 h-28 bg-gray-800 rounded-t-sm mx-1"></div>
        </div>
      </div>
      <div class="bg-white p-4 rounded-xl shadow-sm">
        <h2 class="font-bold text-gray-800 mb-2">Blood Pressure Trends</h2>
        <!-- Placeholder for a line graph -->
        <div class="h-48 bg-gray-100 rounded-lg"></div>
      </div>
    </div>
  </body>
</html>
"""

# -------------------------------------------------
# 8) SETTINGS & PROFILE SCREEN (placeholder)
# -------------------------------------------------
SETTINGS_HTML = f"""
<html>
  {TAILWIND_HEADER}
  <body class="min-h-screen bg-gray-50">
    <header class="p-4 border-b flex justify-between items-center">
      <h1 class="text-xl font-bold">Settings & Profile</h1>
      <img src="https://api.dicebear.com/7.x/notionists/svg?scale=200&seed=123"
           class="w-10 h-10 rounded-full"/>
    </header>
    <main class="p-6">
      <h2 class="text-2xl font-bold mb-4">Customization Options</h2>
      <p class="text-gray-600">Customize which vital signs to view, change theme colors, and update personal information.</p>
      <div class="mt-6">
          <label class="block text-gray-700 font-semibold mb-2">Preferred Theme</label>
          <select class="border rounded p-2 w-full">
            <option>Light</option>
            <option>Dark</option>
          </select>
      </div>
    </main>
  </body>
</html>
"""

# -------------------------------------------------
# Dictionary for all screens
# -------------------------------------------------
SCREENS = {
    "Splash": SPLASH_SCREEN_HTML,
    "Onboarding": ONBOARDING_HTML,
    "Home": HOME_HTML,
    "Measurement": MEASUREMENT_HTML,
    "Results": RESULTS_HTML,
    "History": HISTORY_HTML,
    "Settings": SETTINGS_HTML,
}

def main():
    st.set_page_config(page_title="Contactless Mobile Vital Signs", layout="wide")
    st.title("Contactless Mobile Vital Signs")

    # Read current screen from query parameters (default to "Splash")
    query_params = st.query_params
    current_screen = query_params.get("screen", ["Splash"])[0]
    if current_screen not in SCREENS:
        current_screen = "Splash"

    # Save current screen in session state (for sidebar navigation)
    if "screen" not in st.session_state:
        st.session_state["screen"] = current_screen

    # Render the selected screen's HTML
    html_content = SCREENS[current_screen]
    components.html(html_content, height=1000, scrolling=True)

    # Sidebar navigation (for testing and debugging)
    st.sidebar.markdown("### Navigation")
    nav_choice = st.sidebar.radio("Go to Screen", list(SCREENS.keys()), index=list(SCREENS.keys()).index(current_screen))
    if nav_choice != st.session_state["screen"]:
        st.session_state["screen"] = nav_choice
        st.set_query_params(screen=nav_choice)
        st.experimental_rerun()

if __name__ == "__main__":
    main()
