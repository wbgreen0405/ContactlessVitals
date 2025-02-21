import streamlit as st

st.set_page_config(page_title="Blood Pressure Insights", layout="wide")

# Top row: Title on left, "Share Results" on right
col1, col2 = st.columns([6,1])
with col1:
    st.markdown("<h2 style='margin:0;'>Blood Pressure Insights</h2>", unsafe_allow_html=True)
    st.write("Detailed analysis and recommendations")
with col2:
    if st.button("Share Results"):
        st.write("Sharing results... (placeholder)")

st.write("---")

# Two columns for "Trend Analysis" (left) & "Health Tips" (right)
cA, cB = st.columns([2,2])

with cA:
    # Trend Analysis card
    st.markdown("""
    <div style="
        border:1px solid #E5E7EB; 
        border-radius:0.5rem; 
        padding:1rem;
        margin-bottom:1rem;
    ">
      <div style="display:flex; justify-content:space-between;">
        <h4 style="margin:0;">Trend Analysis</h4>
        <span style="color:green; font-weight:600;">Normal Range</span>
      </div>
      <p>Systolic: 120 mmHg (Average)</p>
      <p>Diastolic: 80 mmHg (Average)</p>
      <p>Variance: 5 mmHg</p>
      <div style="
        width:100%; 
        height:150px; 
        background-color:#F0F0F0;
        border-radius:0.25rem;
      ">
        <!-- placeholder for chart -->
        <p style="text-align:center; padding-top:50px; color:#666;">[Chart Placeholder]</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

with cB:
    # Health Tips card
    st.markdown("""
    <div style="
        border:1px solid #E5E7EB; 
        border-radius:0.5rem; 
        padding:1rem;
        margin-bottom:1rem;
    ">
      <h4 style="margin:0 0 1rem 0;">Health Tips</h4>
      <p><strong>Lifestyle</strong> (Recommendations):</p>
      <ul>
        <li>Maintain balanced diet</li>
        <li>Regular exercise</li>
        <li>Reduce sodium intake</li>
      </ul>
      <p><strong>When to Take Action</strong>:</p>
      <ul>
        <li>Persistent readings above 130/80</li>
        <li>Frequent dizziness or headaches</li>
      </ul>
    </div>
    """, unsafe_allow_html=True)

# Another card for "Comparison to Standard Ranges"
st.markdown("""
<div style="
    border:1px solid #E5E7EB; 
    border-radius:0.5rem; 
    padding:1rem;
    margin-top:1rem;
">
  <h4 style="margin-bottom:1rem;">Comparison to Standard Ranges <span style="float:right;">★★★★★</span></h4>
  <table style="width:100%; text-align:left;">
    <tr style="background-color:#F8F8F8;">
      <th style="padding:0.5rem;">Category</th>
      <th style="padding:0.5rem;">Systolic</th>
      <th style="padding:0.5rem;">Diastolic</th>
      <th style="padding:0.5rem;">Status</th>
    </tr>
    <tr>
      <td style="padding:0.5rem;">Your Reading</td>
      <td style="padding:0.5rem;">120</td>
      <td style="padding:0.5rem;">80</td>
      <td style="padding:0.5rem; color:green;">Normal</td>
    </tr>
    <tr>
      <td style="padding:0.5rem;">Optimal Range</td>
      <td style="padding:0.5rem;">90-120</td>
      <td style="padding:0.5rem;">60-80</td>
      <td style="padding:0.5rem;">Normal</td>
    </tr>
  </table>
</div>
""", unsafe_allow_html=True)

