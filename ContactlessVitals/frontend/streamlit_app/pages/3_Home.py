import streamlit as st

st.set_page_config(layout="wide", page_title="How to Take Measurements")

# Inject CSS to style the page background, top bar, and pinned footer
st.markdown("""
<style>
/* Overall page background - near-white */
body {
    background-color: #F9FAFB;
    margin: 0;
    padding: 0;
    font-family: sans-serif;
}
/* Remove default Streamlit padding */
main .block-container {
    padding: 0 !important;
}

/* A top bar container for arrow (left) + skip (right) */
.top-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 1.5rem;
    background: transparent;  /* or #F9FAFB if you want a small bar color */
}
/* Left arrow button styling (HTML) */
.arrow-btn {
    background: none;
    border: none;
    cursor: pointer;
    padding: 0;
}
.arrow-btn:hover {
    opacity: 0.8;
}
/* We'll place the skip button in the top bar using a column approach. 
   But we can also do an absolute or flex approach. */

/* Centered heading container */
.header-text {
    text-align: center;
    margin-top: 1rem;
    margin-bottom: 1rem;
}
.header-text h1 {
    font-size: 1.875rem; /* text-3xl */
    font-weight: 700;    /* font-bold */
    color: #111827;      /* near-black text */
    margin-bottom: 0.5rem;
}
.header-text p {
    font-size: 1rem;     /* text-base */
    color: #4B5563;      /* text-base-600 */
    margin: 0 auto;
}

/* Carousel container styling */
.carousel-wrapper {
    max-width: 600px;
    margin: 2rem auto 4rem auto; /* 4rem bottom to leave space for the footer button */
    background-color: #FFFFFF;
    border-radius: 0.5rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    padding: 1rem;
    position: relative;
}

/* The "Got It, Let's Start" pinned footer */
.footer-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #3B82F6;  /* Tailwind primary-500 */
    padding: 1rem;
    text-align: center;
    z-index: 999; /* ensure it stays on top */
}
.footer-btn {
    display: inline-block;
    background-color: #3B82F6;
    color: #fff;
    border: none;
    border-radius: 0.5rem;
    padding: 0.75rem 1.5rem;
    font-size: 1rem;
    font-weight: 500;
    cursor: pointer;
    transition: background-color 0.2s ease-in-out;
}
.footer-btn:hover {
    background-color: #2563EB; /* Tailwind primary-600 */
}
</style>
""", unsafe_allow_html=True)

##############################
# 1) Top bar: Arrow on the left, "Skip" on the right
##############################

# We create a row with HTML for the arrow, and a Streamlit button for skip
st.markdown(
    """
    <div class="top-bar">
      <!-- Left arrow (HTML) -->
      <button class="arrow-btn" type="button">
        <svg style="width:24px; height:24px; color:#111827;" 
             xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
          <path fill-rule="evenodd" 
                d="M9.707 16.707a1 1 0 
                   01-1.414 0l-6-6a1 1 0 
                   010-1.414l6-6a1 1 0 
                   011.414 1.414L5.414 
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

# Right side: "Skip" as a real Streamlit button
# We'll float it to the right by placing it in the same top row with negative margin, or just do st.columns
col1, col2 = st.columns([0.85, 0.15])
with col1:
    st.write("")
with col2:
    if st.button("Skip"):
        st.warning("Skipping tutorial... (placeholder)")

##############################
# 2) Main heading & subtitle
##############################
st.markdown(
    """
    <div class="header-text">
      <h1>How to Take Measurements</h1>
      <p>Follow these steps for accurate readings</p>
    </div>
    """,
    unsafe_allow_html=True
)

##############################
# 3) Carousel
##############################
carousel_html = """
<div id="default-carousel" class="carousel-wrapper">
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

##############################
# 4) Fixed bottom bar: "Got It, Let's Start"
##############################
# We place an empty <div> for the bar, then the real Streamlit button that we style.
# Alternatively, we can do a plain HTML button. But let's do a real Streamlit button.
footer_bar_html = """
<div class="footer-bar">
</div>
"""
st.markdown(footer_bar_html, unsafe_allow_html=True)

# Place the actual Streamlit button
center_col = st.columns([1,2,1])[1]  # center column
with center_col:
    got_it = st.button("Got It, Let's Start")
    if got_it:
        st.success("Tutorial complete! (placeholder)")
