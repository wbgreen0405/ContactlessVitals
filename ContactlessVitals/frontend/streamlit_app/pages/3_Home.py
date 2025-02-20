import streamlit as st

# Set up page config
st.set_page_config(
    page_title="Tutorial Flow",
    layout="wide"
)

# (A) Inject extra CSS to remove default Streamlit padding
#     and ensure a light background
st.markdown("""
<style>
/* Force a near-white background. 
   If you used config.toml, that also enforces light mode. */
body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
    background-color: #F9FAFB !important;
}
/* Remove extra Streamlit top/bottom padding */
main .block-container {
    padding: 0 !important;
    margin: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# (B) The raw HTML snippet from your final code
#     This includes the pinned footer, the carousel, the "Skip" & arrow buttons, etc.
#     We place it directly in st.markdown(..., unsafe_allow_html=True).
html_snippet = """
<!-- BEGIN TUTORIAL-FLOW HTML -->
<div id="tutorial-flow" class="min-h-screen bg-gray-50 p-4">

  <!-- HEADER -->
  <div id="header" class="mb-8">
    <div class="flex items-center justify-between">
      <!-- Left Arrow Button -->
      <button ds-variant="ghost" ds-name="Button"
        class="flex justify-center items-center font-medium transition-colors duration-200 ease-in-out
               focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-opacity-50
               px-5 py-2.5 text-sm rounded-lg bg-transparent hover:bg-base-200
               text-base-content hover:text-base-content !p-2">
        <svg class="h-5 w-auto text-current h-6 w-6" aria-hidden="true"
             xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0
                 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0
                 110 2H5.414l4.293 4.293a1 1 0 010 1.414z"
                 clip-rule="evenodd"></path>
        </svg>
      </button>
      <!-- Skip Button -->
      <button ds-variant="ghost" ds-name="Button"
        class="flex justify-center items-center font-medium transition-colors duration-200 ease-in-out
               focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-opacity-50
               px-5 py-2.5 text-sm rounded-lg bg-transparent hover:bg-base-200
               text-base-content hover:text-base-content text-sm">
        Skip
      </button>
    </div>
  </div>

  <!-- CONTENT -->
  <div id="content" class="max-w-lg mx-auto space-y-8">
    <div class="text-center space-y-2">
      <h2 ds-name="H2" class="text-3xl font-bold leading-tight tracking-tight text-base-800">
        How to Take Measurements
      </h2>
      <p ds-name="Paragraph" class="text-base leading-relaxed text-base-600 text-gray-600">
        Follow these steps for accurate readings
      </p>
    </div>

    <!-- CAROUSEL -->
    <div ds-name="Carousel" id="default-carousel" class="relative w-full bg-base-100">
      <div class="relative h-56 overflow-hidden rounded-lg md:h-96">

        <!-- Slide 1 -->
        <div class="hidden duration-700 ease-in-out absolute inset-0 transition-all transform"
             data-carousel-item="active">
          <div class="absolute inset-0 flex items-center justify-center">
            <div class="space-y-4 text-center p-4">
              <img src="https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png"
                   alt="Position Camera" class="w-64 h-64 mx-auto">
              <h4 ds-name="H4" class="text-xl font-bold leading-tight tracking-tight text-base-700">
                Position Your Camera
              </h4>
              <p ds-name="Paragraph" class="text-base leading-relaxed text-base-600">
                Hold your phone 12 inches from your face in good lighting
              </p>
            </div>
          </div>
        </div>

        <!-- Slide 2 -->
        <div class="hidden duration-700 ease-in-out absolute inset-0 transition-all transform"
             data-carousel-item>
          <div class="absolute inset-0 flex items-center justify-center">
            <div class="space-y-4 text-center p-4">
              <img src="https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png"
                   alt="Stay Still" class="w-64 h-64 mx-auto">
              <h4 ds-name="H4" class="text-xl font-bold leading-tight tracking-tight text-base-700">
                Stay Still
              </h4>
              <p ds-name="Paragraph" class="text-base leading-relaxed text-base-600">
                Remain steady and breathe normally during measurement
              </p>
            </div>
          </div>
        </div>

        <!-- Slide 3 -->
        <div class="hidden duration-700 ease-in-out absolute inset-0 transition-all transform"
             data-carousel-item>
          <div class="absolute inset-0 flex items-center justify-center">
            <div class="space-y-4 text-center p-4">
              <img src="https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png"
                   alt="Wait" class="w-64 h-64 mx-auto">
              <h4 ds-name="H4" class="text-xl font-bold leading-tight tracking-tight text-base-700">
                Wait 30 Seconds
              </h4>
              <p ds-name="Paragraph" class="text-base leading-relaxed text-base-600">
                The scan will take about 30 seconds to complete
              </p>
            </div>
          </div>
        </div>

      </div>

      <!-- Prev Button -->
      <button type="button"
              class="absolute top-0 left-0 z-30 flex items-center justify-center
                     h-full px-4 cursor-pointer group focus:outline-none"
              data-carousel-prev>
        <span class="inline-flex items-center justify-center w-10 h-10
                     rounded-full bg-gray-200 group-hover:bg-gray-300
                     group-focus:ring-4 group-focus:ring-gray-400 group-focus:outline-none">
          <svg class="w-4 h-4 text-gray-800" aria-hidden="true"
               xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                  stroke-width="2" d="M5 1 1 5l4 4"/>
          </svg>
          <span class="sr-only">Previous</span>
        </span>
      </button>

      <!-- Next Button -->
      <button type="button"
              class="absolute top-0 right-0 z-30 flex items-center justify-center
                     h-full px-4 cursor-pointer group focus:outline-none"
              data-carousel-next>
        <span class="inline-flex items-center justify-center w-10 h-10
                     rounded-full bg-gray-200 group-hover:bg-gray-300
                     group-focus:ring-4 group-focus:ring-gray-400 group-focus:outline-none">
          <svg class="w-4 h-4 text-gray-800" aria-hidden="true"
               xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                  stroke-width="2" d="m1 9 4-4-4-4"/>
          </svg>
          <span class="sr-only">Next</span>
        </span>
      </button>

    </div>

    <script>
      document.addEventListener('DOMContentLoaded', function() {
        const carousel = document.getElementById('default-carousel');
        const items = carousel.querySelectorAll('[data-carousel-item]');
        const prevButton = carousel.querySelector('[data-carousel-prev]');
        const nextButton = carousel.querySelector('[data-carousel-next]');
        const indicators = carousel.querySelectorAll('[data-carousel-slide-to]');
        let currentIndex = 0;

        function showSlide(index) {
          items.forEach((item, i) => {
            item.classList.toggle('hidden', i !== index);
            item.classList.toggle('translate-x-0', i === index);
            item.classList.toggle('translate-x-full', i !== index);
          });
          indicators.forEach((indicator, i) => {
            indicator.setAttribute('aria-current', i === index ? 'true' : 'false');
          });
          currentIndex = index;
        }

        function nextSlide() {
          showSlide((currentIndex + 1) % items.length);
        }

        function prevSlide() {
          showSlide((currentIndex - 1 + items.length) % items.length);
        }

        nextButton.addEventListener('click', nextSlide);
        prevButton.addEventListener('click', prevSlide);

        indicators.forEach((indicator, index) => {
          indicator.addEventListener('click', () => showSlide(index));
        });

        // Auto-play
        const interval = 3000;
        let autoplayInterval = setInterval(nextSlide, interval);

        carousel.addEventListener('mouseenter', () => clearInterval(autoplayInterval));
        carousel.addEventListener('mouseleave', () => autoplayInterval = setInterval(nextSlide, interval));

        showSlide(0);
      });
    </script>

  </div>

  <!-- FOOTER -->
  <div id="footer" class="fixed bottom-0 left-0 right-0 p-4 bg-white border-t">
    <button ds-variant="primary" ds-name="Button"
      class="flex justify-center items-center font-medium transition-colors
             duration-200 ease-in-out focus:outline-none focus:ring-2
             focus:ring-offset-2 focus:ring-opacity-50 px-5 py-2.5 text-sm
             rounded-lg bg-primary-500 text-primary-content hover:bg-primary-600
             focus:ring-primary-300 w-full">
      Got It, Let's Start
    </button>
  </div>

</div>
<!-- END TUTORIAL-FLOW HTML -->
"""

# Place the snippet into the page
st.markdown(html_snippet, unsafe_allow_html=True)
