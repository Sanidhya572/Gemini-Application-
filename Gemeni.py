import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()  # Loading all the environment variables

import google.generativeai as genai
from PIL import Image

# Configure GenerativeAI with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro text generation model
text_model = genai.GenerativeModel("gemini-pro")

# Function to get text generation response
def get_text_response(question):
    response = text_model.generate_content(question)
    return response.text

# Function to load Gemini Pro vision model for image analysis
image_model = genai.GenerativeModel("gemini-pro-vision")

# Function to get image analysis response
def get_image_response(image):
    response = image_model.generate_content(image)
    return response.text


# Streamlit application with basic theming
st.set_page_config(
    page_title="Gemini Multi-Purpose App", layout="wide"
)

# Sidebar for selecting functionality
selected_option = st.sidebar.selectbox(
    "Select Functionality", ("Text Generation", "Image Analysis")
)

# Display content based on selection
if selected_option == "Text Generation":
    with st.container():  # Group text generation elements
        st.title("Gemini LLM Text Generation")
        input_text = st.text_input("Input:", key="input")
        submit = st.button("Ask the question")

        if submit:
            response = get_text_response(input_text)
            st.subheader("The Response is:")
            st.write(response)

elif selected_option == "Image Analysis":
    with st.container():  # Group image analysis elements
        st.title("Gemini Image Analysis")
        input_text = st.text_input(
            "Enter a description (optional):", key="input"
        )
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        image = ""
        col1, col2 = st.columns(2)  # Create two columns for layout
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            with col1:
                st.image(image, caption="Uploaded Image", use_column_width=True)

        submit = st.button("Tell me about the image")

        if submit:
            if image:
                response = get_image_response(image)
                st.subheader("The Response is:")
                st.write(response)
            else:
                st.warning("Please upload an image.")

else:
    st.write("Invalid selection")

