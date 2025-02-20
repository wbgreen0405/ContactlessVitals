import streamlit as st

st.set_page_config(page_title="ContactlessVitals", layout="wide")

# 1) Top Bar (logo on the left, nav links on the right)
colA, colB, colC = st.columns([1,5,2])
with colA:
    # Replace with your actual logo URL or st.image for a local file
    st.image("https://via.placeholder.com/120x40?text=ContactlessVitals", width=120)
with colC:
    # Right-aligned nav links
    st.write("""<p style="text-align:right; font-size:1rem; margin:0;">
                <a href="#" style="margin-right:1rem; text-decoration:none; color:#000;">Home</a>
                <a href="#" style="margin-right:1rem; text-decoration:none; color:#000;">History</a>
                <a href="#" style="text-decoration:none; color:#000;">Settings</a>
                </p>""",
             unsafe_allow_html=True)

st.write("---")  # A horizontal rule under the top bar

# 2) Centered Welcome + Subheading
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("<h2 style='text-align:center; margin-bottom:0.5rem;'>Welcome to ContactlessVitals</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666; margin-bottom:1.5rem;'>Measure your vital signs instantly using your camera</p>", unsafe_allow_html=True)

# 3) "Start Measurement" Button (centered)
colA2, colB2, colC2 = st.columns([1,2,1])
with colB2:
    # Force the button to be a certain color (blue) with inline CSS
    # We'll do minimal styling here:
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
        button_clicked = st.button("Start Measurement", key="start-btn")
    if button_clicked:
        st.success("Starting measurement... (placeholder)")

st.write("")  # Some vertical space

# 4) Two Cards Side by Side
colCard1, colCard2, colCard3 = st.columns([1,2,1])
with colCard2:
    # We'll do two columns for the two cards
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div style="
            border:1px solid #E5E7EB; 
            border-radius:0.5rem; 
            padding:1rem; 
            text-align:center; 
            background-color:#F8F8F8;">
            <h4 style="margin-bottom:0.5rem;">Last Reading</h4>
            <p style="margin:0;">BP: 120/80</p>
            <p style="margin:0;">Pulse: 72 bpm</p>
            <p style="margin:0;">SpO2: 98%</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div style="
            border:1px solid #E5E7EB; 
            border-radius:0.5rem; 
            padding:1rem; 
            text-align:center; 
            background-color:#F8F8F8;">
            <h4 style="margin-bottom:0.5rem;">Weekly Avg</h4>
            <p style="margin:0;">BP: 117/76</p>
            <p style="margin:0;">Pulse: 70 bpm</p>
            <p style="margin:0;">SpO2: 97%</p>
        </div>
        """, unsafe_allow_html=True)

# 5) Bottom Navigation Bar with icons
st.markdown("""
<style>
.bottom-nav {
    position: fixed;
    bottom: 0; 
    left: 0; 
    right: 0; 
    height: 60px;
    background-color: #FFF;
    border-top: 1px solid #E5E7EB;
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    z-index: 9999;
}
.bottom-nav a {
    text-decoration: none;
    color: #000;
    font-size: 0.9rem;
    text-align: center;
}
.bottom-nav a:hover {
    color: #3B82F6;
}
.nav-icon {
    display: block;
    margin: 0 auto 4px auto;
}
</style>
<div class="bottom-nav">
    <a href="#">
        <img src="https://img.icons8.com/ios-filled/24/000000/home.png" class="nav-icon"/>
        <span>Home</span>
    </a>
    <a href="#">
      
