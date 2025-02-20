import streamlit as st

st.set_page_config(layout="wide", page_title="How to Take Measurements")

# 1) Inject CSS to style background, remove extra padding, etc.
st.markdown("""
<style>
/* Light gray background, like Tailwind's bg-gray-50 */
body {
    background-color: #F9FAFB;
    margin: 0;
    padding: 0;
    font-family: sans-serif;
}
/* Remove some Streamlit padding */
main .block-container {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
}
/* Make the bottom bar 'fixed' at the bottom */
.footer-bar {
    position: fixed; 
    bottom: 0; 
    left: 0; 
    right: 0; 
    background-color: #FFFFFF; 
    border-top: 1px solid #E5E7EB; 
    padding: 1rem;
}
/* A container for the top bar (arrow + skip) */
.top-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
}
.icon-button {
    background: none;
    border: none;
    cursor: pointer;
}
.icon-button:hover {
    opacity: 0.7;
}
</style>
""", unsafe_allow_html=True)

# 2) Header with "Back Arrow" + "Skip" 
#    We'll do a small HTML snippet for the arrow icon
#    Then a real Streamlit button for "Skip".
st.markdown(
    """
    <div class="top-bar">
      <!-- Back arrow (pure HTML). 
           If you want to handle a click in Python, replace with st.button. -->
      <button class="icon-button" type="button">
        <svg style="width:24px; height:24px; color:#111827;" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 
            0l-6-6a1 1 0 010-1.414l6-6a1 
            1 0 011.414 1.414L5.414 
            9H17a1 1 0 110 2H5.414l4.293 
            4.293a1 1 0 010 1.414z" 
            clip-rule="evenodd">
          </path>
        </svg>
      </button>
    </div>
    """,
    unsafe_allow_html=True
)

# "Skip" as a real Streamlit button (right-aligned). 
# We'll float it or just place it in the same row using columns:
col1, col2 = st.columns([0.85, 0.15])
with col1:
    st.write("")  # filler
with col2:
    if st.button("Skip"):
        st.warning("Skipping tutorial... (placeholder)")

# 3) Main content: Title + Subtitle
st.markdown("""
<div style="max-width: 600px; margin: 2rem auto; text-align: center;">
  <h2 style="
    font-size: 1.875rem; /* text-3xl */
    font-weight: 700;    /* font-bold */
    color: #111827;      /* near-black text */
    margin-bottom: 0.5rem;">
    How to Take Measurements
  </h2>
  <p style="
    font-size: 1rem;     /* text-base */
    color: #4B5563;      /* text-base-600 */
    margin-bottom: 2rem;">
    Follow these steps for accurate readings
  </p>
</div>
""", unsafe_allow_html=True)

# 4) Carousel HTML + JavaScript
#    We place it inside a container. The slides each have an image + heading + text.
#    The JS might be partially restricted in Streamlit, but we'll include it for completeness.
carousel_html = """
<div id="default-carousel" style="max-width:600px; margin: 0 auto; background-color: #FFFFFF; border-radius: 0.5rem; padding: 1rem; position: relative;">
  <div style="position: relative; height: 300px; overflow: hidden;">
    <!-- Slide 1 -->
    <div class="hidden duration-700 ease-in-out absolute inset-0 transition-all transform" data-carousel-item="active">
      <div style="position:absolute; inset:0; display:flex; justify-content:center; align-items:center;">
        <div style="text-align:center; padding:1rem;">
          <img src="https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png" alt="Position Camera" style="width:160px; height:160px; margin:auto;" />
          <h4 style="font-size:1.25rem; font-weight:700; color:#374151; margin-top:1rem;">Position Your Camera</h4>
          <p style="font-size:1rem; color:#4B5563; margin-top:0.5rem;">
            Hold your phone 12 inches from your face in good lighting
          </p>
        </div>
      </div>
    </div>
    <!-- Slide 2 -->
    <div class="hidden duration-700 ease-in-out absolute inset-0 transition-all transform" data-carousel-item>
      <div style="position:absolute; inset:0; display:flex; justify-content:center; align-items:center;">
        <div style="text-align:center; padding:1rem;">
          <img src="https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png" alt="Stay Still" style="width:160px; height:160px; margin:auto;" />
          <h4 style="font-size:1.25rem; font-weight:700; color:#374151; margin-top:1rem;">Stay Still</h4>
          <p style="font-size:1rem; color:#4B5563; margin-top:0.5rem;">
            Remain steady and breathe normally during measurement
          </p>
        </div>
      </div>
    </div>
    <!-- Slide 3 -->
    <div class="hidden duration-700 ease-in-out absolute inset-0 transition-all transform" data-carousel-item>
      <div style="position:absolute; inset:0; display:flex; justify-content:center; align-items:center;">
        <div style="text-align:center; padding:1rem;">
          <img src="https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png" alt="Wait" style="width:160px; height:160px; margin:auto;" />
          <h4 style="font-size:1.25rem; font-weight:700; color:#374151; margin-top:1rem;">Wait 30 Seconds</h4>
          <p style="font-size:1rem; color:#4B5563; margin-top:0.5rem;">
            The scan will take about 30 seconds to complete
          </p>
        </div>
      </div>
    </div>
  </div>

  <!-- Carousel prev/next controls -->
  <button type="button" style="position:absolute; top:50%; left:0; transform:translateY(-50%); background:#EEE; border:none; border-radius:50%; width:32px; height:32px; cursor:pointer;" data-carousel-prev>
    <span style="display:inline-block; transform:translateX(2px);">
      <svg style="width:16px; height:16px; color:#333;" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 1 1 5l4 4"/>
      </svg>
    </span>
  </button>
  <button type="button" style="position:absolute; top:50%; right:0; transform:translateY(-50%); background:#EEE; border:none; border-radius:50%; width:32px; height:32px; cursor:pointer;" data-carousel-next>
    <span style="display:inline-block; transform:translateX(-2px);">
      <svg style="width:16px; height:16px; color:#333;" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 6 10">
        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 9 4-4-4-4"/>
      </svg>
    </span>
  </button>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const carousel = document.getElementById('default-carousel');
  if(!carousel) return;

  const items = carousel.querySelectorAll('[data-carousel-item]');
  const prevButton = carousel.querySelector('[data-carousel-prev]');
  const nextButton = carousel.querySelector('[data-carousel-next]');
  let currentIndex = 0;

  function showSlide(index) {
    items.forEach((item, i) => {
      const active = (i === index);
      item.classList.toggle('hidden', !active);
      item.classList.toggle('translate-x-0', active);
      item.classList.toggle('translate-x-full', !active);
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

  showSlide(0);
});
</script>
"""
st.markdown(carousel_html, unsafe_allow_html=True)

# 5) Fixed footer bar with "Got It, Let's Start" button
st.markdown(
    """
    <div class="footer-bar">
    </div>
    """,
    unsafe_allow_html=True
)

# Use absolute positioning trick to place the button in that bar
# We'll put the st.button call here, so it physically appears after the bar,
# but visually the button will appear on top of it (since it's 'fixed').
if st.button("Got It, Let's Start"):
    st.success("Tutorial complete! (Placeholder)")

