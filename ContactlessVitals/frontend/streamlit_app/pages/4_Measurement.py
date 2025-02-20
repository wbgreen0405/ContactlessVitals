import streamlit as st

st.set_page_config(page_title="ContactlessVitals", layout="wide")

########################################
# 1) Top Bar
########################################
# We'll keep the same columns approach: logo on left, app name in middle, 
# "Home/History/Settings" buttons on the far right.
colA, colB, colC = st.columns([1,4,3])

with colA:
    # Replace with your actual logo or local image if needed
    st.image("https://via.placeholder.com/120x40?text=ContactlessVitals", width=120)

with colB:
    # Just the app name in the middle if desired
    st.markdown("<h3 style='margin:0; text-align:center;'>ContactlessVitals</h3>", unsafe_allow_html=True)

with colC:
    # Three columns for Home, History, Settings
    cHome, cHist, cSet = st.columns(3)
    with cHome:
        if st.button("Home"):
            st.write("Home clicked")
    with cHist:
        if st.button("History"):
            st.write("History clicked")
    with cSet:
        if st.button("Settings"):
            st.write("Settings clicked")

st.write("---")  # horizontal rule under top bar

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

    st.markdown('<div class="center-btn">', unsafe_allow_html=True)
    measure_btn = st.button("Start Measurement")
    st.markdown('</div>', unsafe_allow_html=True)

    if measure_btn:
        st.success("Starting measurement... (placeholder)")

st.write("")  # vertical space

########################################
# 4) Two Cards Side by Side
########################################
colCard1, colCard2, colCard3 = st.columns([1,2,1])
with colCard2:
    c1, c2 = st.columns(2)

    # Icons for BP, Pulse, SpO2
    bp_icon    = "https://img.icons8.com/ios-filled/20/000000/heart-with-pulse.png"
    pulse_icon = "https://img.icons8.com/ios-filled/20/000000/pulse.png"
    spo2_icon  = "https://img.icons8.com/ios-filled/20/000000/oxygen-saturation.png"  # Fix this icon

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

