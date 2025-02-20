import streamlit as st

# We do NOT rely on user theme now—our config.toml forces light mode.
# We still set layout=wide and a page title:
st.set_page_config(
    page_title="How to Take Measurements",
    layout="wide"
)

# 1) Inject extra CSS to do the pinned footer, top bar layout, etc.
st.markdown("""
<style>
/* Since config.toml enforces light theme, 
   we can trust the background to be #F9FAFB or #FFFFFF. */

/* Remove extra Streamlit padding */
main .block-container {
    padding: 0 !important;
    margin: 0 !important;
}

/* Top bar container (arrow left, skip right) */
.top-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 1.5rem;
    background-color: #F9FAFB;
}
/* Arrow button (HTML) */
.arrow-btn {
    background: none;
    border: none;
    cursor: pointer;
    outline: none;
    padding: 0;
}
.arrow-btn:hover {
    opacity: 0.8;
}
/* We'll place the Streamlit skip button in the same row using columns. 
   Or we can do a plain HTML button if you prefer. */

/* Center heading area */
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

/* Carousel container (white card) */
.carousel-wrapper {
    max-width: 600px;
    margin: 2rem auto 5rem auto; /* extra bottom space for pinned footer */
    background-color: #FFFFFF;
    border-radius: 0.5rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    padding: 1rem;
    position: relative;
}

/* The pinned bright-blue footer at bottom */
.footer-bar {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #3B82F6; /* bright blue */
    padding: 1rem;
    text-align: center;
    z-index: 999;
    margin: 0;
}

/* Make st.button full-width inside the pinned bar if desired */
.footer-btn-container button {
    width: 100% !important;
    background-color: #3B82F6 !important;
    color: #FFFFFF !important;
    font-size: 1rem !important;
    font-weight: 500 !important;
    border-radius: 0.5rem !important;
    border: none !important;
    padding: 0.75rem 1.5rem !important;
    margin: 0 !important;
    cursor: pointer;
}
.footer-btn-container button:hover {
    background-color: #2563EB !important; /* darker blue on hover */
}
</style>
""", unsafe_allow_html=True)

#############################
# 2) TOP BAR: arrow on left, skip on right
#############################
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
    """,
    unsafe_allow_html=True
)

# Place "Skip" as a real Streamlit button on the top right
col1, col2 = st.columns([0.9, 0.1])
with col1:
    st.write("")
with col2:
    if st.button("Skip"):
        st.warning("Skipping tutorial... (placeholder)")

# Close the top-bar div
st.markdown("</div>", unsafe_allow_html=True)

#############################
# 3) Heading & subheading
#############################
st.markdown(
    """
    <div class="header-text">
      <h1>How to Take Measurements</h1>
      <p>Follow these steps for accurate readings</p>
    </div>
    """,
    unsafe_allow_html=True
)

#############################
# 4) Carousel (white card)
#############################
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

#############################
# 5) Pinned footer with "Got It, Let's Start"
#############################
st.markdown('<div class="footer-bar">', unsafe_allow_html=True)
# We create a container for the button. 
# We'll place the real st.button in a column so it's 100% wide.
colA, colB, colC = st.columns([0.15, 0.7, 0.15])
with colB:
    with st.container():
        st.markdown('<div class="footer-btn-container">', unsafe_allow_html=True)
        if st.button("Got It, Let's Start"):
            st.success("Tutorial complete! (placeholder)")
        st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
