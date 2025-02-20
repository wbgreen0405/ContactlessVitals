import streamlit as st

st.set_page_config(page_title="How to Measure Your Vitals", layout="wide")

# 1) Main Page Title (Centered)
st.markdown(
    """
    <h1 style="text-align: center; font-family: sans-serif; font-size: 2rem; margin-bottom: 0.5rem;">
      How to Measure Your Vitals
    </h1>
    <p style="text-align: center; color: #4B5563; font-family: sans-serif; margin-bottom: 2rem;">
      Follow these simple steps for accurate measurements
    </p>
    """,
    unsafe_allow_html=True
)

# 2) Steps Data
steps = [
    {
        "step_num": "1",
        "title": "Position Your Face",
        "description": "Center your face in the camera frame at arm's length distance",
        "image_url": "https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png"
    },
    {
        "step_num": "2",
        "title": "Ensure Good Lighting",
        "description": "Find a well-lit area, avoid backlighting",
        "image_url": "https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png"
    },
    {
        "step_num": "3",
        "title": "Stay Still",
        "description": "Hold your device steady for 30 seconds during measurement",
        "image_url": "https://storage.googleapis.com/uxpilot-auth.appspot.com/default-placeholder.png"
    },
]

# 3) Render Steps in Centered Blocks
for step in steps:
    st.markdown(
        f"""
        <div style="
            margin: 0 auto; 
            max-width: 500px; 
            border: 1px solid #E5E7EB; 
            border-radius: 8px;
            padding: 1.5rem; 
            text-align: center;
            margin-bottom: 1.5rem;
            font-family: sans-serif;
            background-color: #FFFFFF;
        ">
            <!-- Step Number Badge -->
            <div style="
                background-color: #E5E7EB; 
                color: #111827;
                width: 2rem; 
                height: 2rem; 
                border-radius: 9999px;
                display: flex; 
                align-items: center; 
                justify-content: center; 
                font-size: 0.875rem; 
                font-weight: 600; 
                margin: 0 auto 1rem auto;
            ">
                {step['step_num']}
            </div>

            <!-- Step Image -->
            <img src="{step['image_url']}" 
                 alt="Step image" 
                 style="width:140px; height:100px; object-fit:cover; border-radius:4px; background-color:#F9FAFB; margin-bottom:1rem;" />

            <!-- Step Title -->
            <h3 style="font-size:1.125rem; font-weight:700; color:#111827; margin-bottom:0.5rem;">
                {step['title']}
            </h3>

            <!-- Step Description -->
            <p style="font-size:1rem; color:#4B5563; line-height:1.4; margin:0 auto;">
                {step['description']}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# 4) Pinned Footer with a Wide, Centered Button
# We use absolute positioning in HTML + a real Streamlit button for the click.
st.markdown(
    """
    <div style="
        position: fixed; 
        bottom: 0; 
        left: 0; 
        right: 0; 
        background-color: #3B82F6; 
        padding: 1rem; 
        text-align: center; 
        z-index: 9999;
        margin: 0;
    ">
    """,
    unsafe_allow_html=True
)

if st.button("Got It, Let's Start"):
    st.success("Tutorial complete! (placeholder)")

st.markdown("</div>", unsafe_allow_html=True)
