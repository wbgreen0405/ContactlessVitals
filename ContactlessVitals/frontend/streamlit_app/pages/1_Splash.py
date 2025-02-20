import streamlit as st

# 1) Must be first Streamlit command
st.set_page_config(page_title="ContactlessVitals", layout="wide")

# 2) Add Tailwind + FontAwesome + optional global styles
tailwind_header = """
<head>
  <!-- Tailwind CSS via CDN -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- FontAwesome (optional) -->
  <script>
      window.FontAwesomeConfig = {
          autoReplaceSvg: 'nest'
      };
  </script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/js/all.min.js"
          crossorigin="anonymous" referrerpolicy="no-referrer"></script>

  <!-- Minimal global override or custom styles -->
  <style>
    /* Example: Hide default Streamlit scrollbar */
    ::-webkit-scrollbar {
      display: none;
    }
    /* You can also hide Streamlit’s default sidebar if desired: */
    [data-testid="stSidebar"] {
      display: none;
    }
  </style>
</head>
"""

# 3) Your HTML snippet (with the classes you provided)
welcome_html = f"""
{tailwind_header}
<body class="h-full text-base-content">
  <div id="welcome-screen"
       class="min-h-screen bg-gradient-to-b from-blue-50 to-white p-6 flex flex-col justify-between">

    <!-- Top section with title, subtitle, and image -->
    <div class="text-center space-y-6 mt-12">
      <h1 ds-name="H1"
          class="text-4xl font-extrabold leading-tight tracking-tight text-base-900">
        ContactlessVitals
      </h1>
      <p ds-name="Lead"
         class="text-xl font-light leading-relaxed text-base-700">
        Monitor your vital signs instantly using just your smartphone camera
      </p>
      <div class="w-full max-w-md mx-auto">
        <img src="https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png"
             alt="Contactless monitoring animation"
             class="w-full h-64 object-cover rounded-xl shadow-lg" />
      </div>
    </div>

    <!-- Bottom section: Card with icons + Buttons -->
    <div class="space-y-6 text-center mt-12">
      <div ds-name="Card"
           class="rounded-lg text-base-content flex flex-col bg-base border border-base-200 p-0 shadow max-w-md mx-auto bg-white/80 backdrop-blur">
        <div class="flex h-full flex-col justify-start gap-4 p-6">
          <div class="flex items-center justify-center space-x-4">
            <!-- Heart Rate Icon -->
            <div class="flex flex-col items-center">
              <svg class="h-8 w-8 text-red-500 mb-2"
                   aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                   fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd"
                      d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z"
                      clip-rule="evenodd"></path>
              </svg>
              <p ds-name="Paragraph"
                 class="text-base leading-relaxed text-base-600">
                Heart Rate
              </p>
            </div>
            <!-- Blood Pressure Icon -->
            <div class="flex flex-col items-center">
              <svg class="h-8 w-8 text-blue-500 mb-2"
                   aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                   fill="currentColor" viewBox="0 0 20 20">
                <path stroke-linecap="round" stroke-linejoin="round"
                      d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path>
              </svg>
              <p ds-name="Paragraph"
                 class="text-base leading-relaxed text-base-600">
                Blood Pressure
              </p>
            </div>
            <!-- SpO Icon -->
            <div class="flex flex-col items-center">
              <svg class="h-8 w-8 text-yellow-500 mb-2"
                   aria-hidden="true" xmlns="http://www.w3.org/2000/svg"
                   fill="currentColor" viewBox="0 0 20 20">
                <path stroke-linecap="round" stroke-linejoin="round"
                      d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>
              </svg>
              <p ds-name="Paragraph"
                 class="text-base leading-relaxed text-base-600">
                SpO
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- Buttons -->
      <div class="space-y-4 max-w-md mx-auto">
        <!-- "Get Started" button -->
        <button ds-variant="primary"
                ds-size="xl"
                ds-name="Button"
                class="flex justify-center items-center font-medium transition-colors duration-200 ease-in-out
                       focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-opacity-50
                       rounded-lg bg-primary-500 text-primary-content
                       hover:bg-primary-600 focus:ring-primary-300
                       px-6 py-3.5 text-base w-full">
          Get Started
        </button>
        <!-- "Already have an account?" link -->
        <button ds-variant="link"
                ds-name="Button"
                class="flex justify-center items-center font-medium transition-colors duration-200 ease-in-out
                       focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-opacity-50
                       px-5 py-2.5 text-sm rounded-lg bg-transparent text-primary
                       hover:underline hover:text-primary-focus">
          Already have an account? Sign in
        </button>
      </div>
    </div>
  </div>
</body>
"""

# 4) Actually display it in Streamlit
st.markdown(welcome_html, unsafe_allow_html=True)
