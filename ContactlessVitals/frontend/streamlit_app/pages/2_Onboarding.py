import streamlit as st

st.set_page_config(layout="wide")

# Inject custom CSS to replicate your Tailwind-like classes and remove extra padding
st.markdown(
    """
    <style>
    /* Remove default Streamlit spacing */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"], .block-container {
        margin: 0 !important;
        padding: 0 !important;
        background: #F9FAFB; /* Matches bg-gray-50 */
    }

    /* Container that holds everything */
    .permissions-setup {
        min-height: 100vh; 
        padding: 1rem; /* p-4 */
    }
    @media (min-width: 768px) {
        .permissions-setup {
            padding: 1.5rem; /* md:p-6 */
        }
    }

    .max-w-lg {
        max-width: 32rem; /* ~512px */
        margin-left: auto;
        margin-right: auto;
    }
    .space-y-8 > * + * {
        margin-top: 2rem;
    }
    .space-y-4 > * + * {
        margin-top: 1rem;
    }
    .text-center {
        text-align: center;
    }
    .text-3xl {
        font-size: 1.875rem;
        line-height: 2.25rem;
    }
    .text-base {
        font-size: 1rem;
    }
    .font-bold {
        font-weight: 700;
    }
    .leading-tight {
        line-height: 1.25;
    }
    .tracking-tight {
        letter-spacing: -0.015em;
    }
    .text-base-800 {
        color: #1f2937;
    }
    .text-base-700 {
        color: #374151;
    }
    .text-base-600 {
        color: #4b5563;
    }
    .rounded-lg {
        border-radius: 0.5rem;
    }
    .text-base-content {
        color: #1f2937;
    }
    .bg-base {
        background-color: #ffffff;
    }
    .border-base-200 {
        border-color: #e5e7eb;
    }
    .p-0 {
        padding: 0 !important;
    }
    .shadow {
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
    }
    .flex {
        display: flex;
    }
    .flex-col {
        flex-direction: column;
    }
    .justify-start {
        justify-content: flex-start;
    }
    .justify-center {
        justify-content: center;
    }
    .items-center {
        align-items: center;
    }
    .gap-4 {
        gap: 1rem;
    }
    .mb-6 {
        margin-bottom: 1.5rem;
    }
    .h-full {
        height: 100%;
    }
    .h-16 {
        height: 4rem;
    }
    .w-16 {
        width: 4rem;
    }
    .text-primary-500 {
        color: #3b82f6; 
    }
    .text-primary-content {
        color: #ffffff;
    }
    .bg-primary-500 {
        background-color: #3b82f6;
    }
    .hover\\:bg-primary-600:hover {
        background-color: #2563eb;
    }
    .focus\\:ring-primary-300:focus {
        box-shadow: 0 0 0 2px rgba(147,197,253,0.5);
    }
    .px-5 {
        padding-left: 1.25rem;
        padding-right: 1.25rem;
    }
    .py-3 {
        padding-top: 0.75rem;
        padding-bottom: 0.75rem;
    }
    .transition-colors {
        transition: color 0.2s, background-color 0.2s;
    }
    .duration-200 {
        transition-duration: 200ms;
    }
    .ease-in-out {
        transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
    }
    .focus\\:outline-none:focus {
        outline: none;
    }
    .focus\\:ring-2:focus {
        box-shadow: 0 0 0 2px rgba(0,0,0,0.1);
    }
    .focus\\:ring-offset-2:focus {
        outline-offset: 2px;
    }
    .text-xl {
        font-size: 1.25rem;
    }
    .bg-transparent {
        background: transparent;
    }
    .text-primary {
        color: #3b82f6;
    }
    .hover\\:underline:hover {
        text-decoration: underline;
    }
    .hover\\:text-primary-focus:hover {
        color: #2563eb;
    }
    .px-3 {
        padding-left: 0.75rem;
        padding-right: 0.75rem;
    }
    .py-2 {
        padding-top: 0.5rem;
        padding-bottom: 0.5rem;
    }
    .text-sm {
        font-size: 0.875rem;
    }
    .list-disc {
        list-style-type: disc;
    }
    .list-inside {
        list-style-position: inside;
    }
    .space-y-1 > * + * {
        margin-top: 0.25rem;
    }
    .pt-4 {
        padding-top: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create the HTML structure inside Streamlit
html_content = """
<div id="permissions-setup" class="permissions-setup">
  <div class="max-w-lg space-y-8">
  
    <!-- Header -->
    <div id="header" class="text-center space-y-4">
      <h2 ds-name="H2" class="text-3xl font-bold leading-tight tracking-tight text-base-800">Camera Access Required</h2>
      <p ds-name="Paragraph" class="text-base leading-relaxed text-base-600">
        To measure your vital signs accurately, ContactlessVitals needs access to your device's camera.
      </p>
    </div>

    <!-- Camera Permission Card -->
    <div ds-id="camera-permission" ds-name="Card" class="rounded-lg text-base-content flex flex-col bg-base border border-base-200 p-0 shadow text-center">
      <div class="flex h-full flex-col justify-start gap-4 p-6">
        <div class="flex justify-center mb-6">
          <svg class="h-5 w-auto h-16 w-16 text-primary-500" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M4 5a2 2 0 00-2 2v8a2 2 0 002 2h12a2 2 0 002-2V7a2 2 0 00-2-2h-1.586a1 1 0 01-.707-.293l-1.121-1.121A2 2 0 0011.172 3H8.828a2 2 0 00-1.414.586L6.293 4.707A1 1 0 015.586 5H4zm6 9a3 3 0 100-6 3 3 0 000 6z" clip-rule="evenodd"></path>
          </svg>
        </div>
        <h4 ds-name="H4" class="text-xl font-bold leading-tight tracking-tight text-base-700">Enable Camera Access</h4>
        <p ds-name="Paragraph" class="text-base leading-relaxed text-base-600 mb-6">
          Your camera will only be used during vital measurements. No videos or images are stored.
        </p>
        <button ds-variant="primary" ds-size="lg" ds-name="Button" 
                class="flex justify-center items-center font-medium transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-opacity-50 rounded-lg bg-primary-500 text-primary-content hover:bg-primary-600 focus:ring-primary-300 px-5 py-3 text-base">
          Allow Camera Access
        </button>
      </div>
    </div>

    <!-- Privacy Note Card -->
    <div ds-id="privacy-note" ds-name="Card" class="rounded-lg text-base-content flex flex-col bg-base border border-base-200 p-0 shadow">
      <div class="flex h-full flex-col justify-start gap-4 p-6">
        <div class="space-y-4">
          <div class="flex items-center gap-2">
            <svg class="h-5 w-auto h-5 w-5 text-primary-500" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
              <path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd"></path>
            </svg>
            <h5 ds-name="H5" class="text-lg font-bold leading-tight tracking-tight text-base-700">Privacy Guarantee</h5>
          </div>
          <ul ds-name="List" class="space-y-1 text-base-content list-inside list-disc">
            <li ds-icon="HiCheckCircle" ds-name="List.Item" class="flex items-start text-base-content">
              <svg class="w-3.5 h-3.5 me-2 my-auto text-base-content" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
              </svg>
              All measurements are processed locally on your device
            </li>
            <li ds-icon="HiCheckCircle" ds-name="List.Item" class="flex items-start text-base-content">
              <svg class="w-3.5 h-3.5 me-2 my-auto text-base-content" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
              </svg>
              Your data is encrypted and never shared without consent
            </li>
            <li ds-icon="HiCheckCircle" ds-name="List.Item" class="flex items-start text-base-content">
              <svg class="w-3.5 h-3.5 me-2 my-auto text-base-content" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
              </svg>
              You can delete your data at any time
            </li>
          </ul>
          <div class="pt-4">
            <button ds-variant="link" ds-size="sm" ds-name="Button" 
                    class="flex justify-center items-center font-medium transition-colors duration-200 ease-in-out focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-opacity-50 rounded-lg bg-transparent text-primary hover:underline hover:text-primary-focus px-3 py-2 text-sm">
              Read Privacy Policy
            </button>
          </div>
        </div>
      </div>
    </div>

  </div>
</div>
"""

st.markdown(html_content, unsafe_allow_html=True)

# Additional Streamlit logic can go here (e.g. handling button clicks)


# You can add additional Streamlit logic below (e.g. button clicks, camera checks, etc.)
