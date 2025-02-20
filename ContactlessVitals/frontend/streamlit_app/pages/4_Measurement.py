import streamlit as st

st.set_page_config(page_title="ContactlessVitals", layout="wide")

########################################
# 1) Top Bar
########################################
colA, colB, colC = st.columns([1,5,2])
with colA:
    # Replace with your actual logo URL or st.image for a local file
    st.image("https://via.placeholder.com/120x40?text=ContactlessVitals", width=120)

with colC:
    # Right-aligned (HTML or st.write). Minimal approach: inline HTML
    st.write("""<p style="text-align:right; font-size:1rem; margin:0;">
                <strong>ContactlessVitals</strong>
                </p>""", unsafe_allow_html=True)

st.write("---")  # A horizontal rule under the top bar

########################################
# 2) Centered Welcome + Subheading
########################################
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("<h2 style='text-align:center; margin-bottom:0.5rem;'>Welcome to ContactlessVitals</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; margin-bottom:1.5rem;'>Measure your vital signs instantly using your camera</p>", unsafe_allow_html=True)

########################################
# 3) "Start Measurement" Button (centered)
########################################
colA2, colB2, colC2 = st.columns([1,2,1])
with colB2:
    # Force the button to be a certain color (blue) with inline CSS
    st.markdown("""
    <style>
    .center-btn button {
        display: block;
        margin: 0 auto;
        background-color: #3B82F6 !important;
        color: #FFFFFF !important;
        font-size: 1rem !important;
        font-weight: 500 !important;
        border-radius: 0.5rem !important;
        border: none !important;
        padding: 0.75rem 1.5rem !important;
        cursor: pointer;
        max-width: 300px;
    }
    .center-btn button:hover {
        background-color: #2563EB !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Put the button in a container with that class
    with st.container():
        st.markdown('<div class="center-btn">', unsafe_allow_html=True)
        measure_btn = st.button("Start Measurement")
        st.markdown('</div>', unsafe_allow_html=True)

    if measure_btn:
        st.success("Starting measurement... (placeholder)")

st.write("")  # Some vertical space

########################################
# 4) Two Cards Side by Side
########################################
colCard1, colCard2, colCard3 = st.columns([1,2,1])
with colCard2:
    # We'll do two columns for the two cards
    c1, c2 = st.columns(2)

    # Icons for BP, Pulse, SpO2
    bp_icon    = "https://img.icons8.com/ios-filled/20/000000/heart-with-pulse.png"
    pulse_icon = "https://img.icons8.com/ios-filled/20/000000/pulse.png"
    spo2_icon  = "https://img.icons8.com/ios-filled/20/000000/oxygen-saturation.png"

    # Card 1: Last Reading
    with c1:
        st.markdown(f"""
        <div style="
            border:1px solid #E5E7EB; 
            border-radius:0.5rem; 
            padding:1rem; 
            text-align:center; 
            background-color:#F8F8F8;">
            <h4 style="margin-bottom:0.5rem;">Last Reading</h4>
            <p style="margin:0;">
              <img src="{bp_icon}" style="vertical-align:middle;" /> BP: 120/80
            </p>
            <p style="margin:0;">
              <img src="{pulse_icon}" style="vertical-align:middle;" /> Pulse: 72 bpm
            </p>
            <p style="margin:0;">
              <img src="{spo2_icon}" style="vertical-align:middle;" /> SpO2: 98%
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Card 2: Weekly Avg
    with c2:
        st.markdown(f"""
        <div style="
            border:1px solid #E5E7EB; 
            border-radius:0.5rem; 
            padding:1rem; 
            text-align:center; 
            background-color:#F8F8F8;">
            <h4 style="margin-bottom:0.5rem;">Weekly Avg</h4>
            <p style="margin:0;">
              <img src="{bp_icon}" style="vertical-align:middle;" /> BP: 117/76
            </p>
            <p style="margin:0;">
              <img src="{pulse_icon}" style="vertical-align:middle;" /> Pulse: 70 bpm
            </p>
            <p style="margin:0;">
              <img src="{spo2_icon}" style="vertical-align:middle;" /> SpO2: 97%
            </p>
        </div>
        """, unsafe_allow_html=True)

########################################
# 5) Bottom Nav with Streamlit Buttons + Icons
########################################
# We'll create a pinned footer bar using columns.
st.markdown("""
<style>
.bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: #FFFFFF;
    border-top: 1px solid #E5E7EB;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 9999;
}
</style>
<div class="bottom-nav" id="nav-bar"></div>
""", unsafe_allow_html=True)

# Create a placeholder to place columns for the nav buttons
nav_placeholder = st.empty()
with nav_placeholder.container():
    nav_col1, nav_col2, nav_col3 = st.columns(3)
    # Home
    with nav_col1:
        st.markdown("""<div style="text-align:center;">
        <img src="https://img.icons8.com/ios-filled/24/000000/home.png" /><br/>
        </div>""", unsafe_allow_html=True)
        if st.button("Home"):
            st.write("Home clicked")

    # History
    with nav_col2:
        st.markdown("""<div style="text-align:center;">
        <img src="https://img.icons8.com/ios-filled/24/000000/area-chart.png" /><br/>
        </div>""", unsafe_allow_html=True)
        if st.button("History"):
            st.write("History clicked")

    # Settings
    with nav_col3:
        st.markdown("""<div style="text-align:center;">
        <img src="https://img.icons8.com/ios-filled/24/000000/settings.png" /><br/>
        </div>""", unsafe_allow_html=True)
        if st.button("Settings"):
            st.write("Settings clicked")
