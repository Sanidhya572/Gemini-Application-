# Gemini Multi-Purpose App

This is a Streamlit application that utilizes Google GenerativeAI's Gemini Pro models for text generation and image analysis.

## Features

- **Text Generation:** Ask the Gemini LLM any question and receive human-quality text responses.
- **Image Analysis:** Upload an image and get insights from the Gemini Pro vision model.

## Running the Application

### Prerequisites:

- Python 3.7 or later
- Streamlit: `pip install streamlit`
- Google GenerativeAI library: `pip install google-generativeai`
- Pillow (PIL Fork): `pip install Pillow`

### Obtain a Google GenerativeAI API Key:

1. Create a project and enable the GenerativeAI API in the Google Cloud Console.
2. Create an API key and set the environment variable `GOOGLE_API_KEY` with your key value. You can use dotenv to manage environment variables.

### Instructions:

1. Clone or download this repository.
2. Run the application:

    ```bash
    streamlit run main.py
    ```

**Use code with caution.**

## Code Structure

The `main.py` file includes:

```python
# Import libraries
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
from PIL import Image

# ... (rest of the code)
