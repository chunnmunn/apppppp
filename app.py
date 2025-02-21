import streamlit as st
import requests
from PIL import Image
import io


# Predefined image sizes
IMAGE_SIZES = [(300, 250), (728, 90), (160, 600), (300, 600)]

# Twitter API credentials (replace with your credentials)
API_KEY = "BjjA6y4ce10Jt77QoKmY8ZTUh"
API_SECRET = "7DyFNhcGJ6X0EMg6HRNz6PS9lJwvdTFGv5cKWITkJltCjYBpFM"
ACCESS_TOKEN = "1892887165841133572-ojxUNDLwTLBI0DNqSul4JIjJy69gbb"
ACCESS_SECRET = "2fTIULXGanH19fJv0N7qNEh0HKMk1do28FQ87PyJdl1U4"

# Authenticate with Twitter

# Predefined image sizes
# IMAGE_SIZES = [(300, 250), (728, 90), (160, 600), (300, 600)]

# Resize image
def resize_image(image, size):
    return image.resize(size, Image.LANCZOS)

# Streamlit UI Design
st.set_page_config(page_title="Image Resizer", page_icon="📷", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #ff1f1f;
    }
    .stFileUploader>div {
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📷 Image Resizer")
st.write("Upload an image to resize it into predefined dimensions!")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"], help="Supported formats: JPG, PNG, JPEG")

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)
    
    st.write("### Resized Images")
    resized_images = [resize_image(image, size) for size in IMAGE_SIZES]
    
    cols = st.columns(len(resized_images))
    for i, (col, img) in enumerate(zip(cols, resized_images)):
        col.image(img, caption=f"{IMAGE_SIZES[i]}", use_column_width=True)
