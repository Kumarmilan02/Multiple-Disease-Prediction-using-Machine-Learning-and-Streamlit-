import os
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import base64
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Health Predictor", page_icon="⚕️", layout="wide")

# Import pages
from DiseasePage import (
    diabetes_page, heart_disease_page, parkinsons_page,
    breast_cancer_page, lung_cancer_page, kidney_disease_page,
    liver_disease_page
)
from HomePage import (
    exercise_page, mental_health_page,
    balanced_diet_page, hydration_page, checkup_page
)

# Function to load Lottie animations from a URL
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animations for the "Welcome" text
lottie_left = load_lottie_url("https://lottie.host/22289fa4-1f2d-4e6f-9519-b401a851646c/A9C8Brwsy6.json")
lottie_middle = load_lottie_url("https://lottie.host/05a0c3b0-871a-462b-8a6a-499b40b9bff3/bkBd4NpFTZ.json")
lottie_right = load_lottie_url("https://lottie.host/22289fa4-1f2d-4e6f-9519-b401a851646c/A9C8Brwsy6.json")

# Create animation for the welcome message
def display_welcome():
    col1, col2, col3 = st.columns([1, 2, 1])  # Adjust column sizes as needed
    with col1:
        st_lottie(lottie_left, height=150, key="left")
    with col2:
        st_lottie(lottie_middle, height=150, key="middle")
    with col3:
        st_lottie(lottie_right, height=150, key="right")
    
    st.markdown(
        """
        <div style="text-align:center; font-size:50px; font-weight:bold;">
            Welcome to Health Predictor
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")

def get_base64_image(image_path):
    """Helper function to convert image to base64 encoding"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def disease_prediction_page():
    st.write(""" 
        ### Stages of Disease Development in Humans
        1. **Exposure**: The body comes into contact with a pathogen (bacteria, virus, etc.) through various means like air, food, or direct contact.
        2. **Infection**: The pathogen enters the body and begins to multiply, starting to affect the host's cells and systems.
        3. **Incubation**: The pathogen grows within the body, but symptoms have not yet appeared. This stage can last from hours to days or weeks.
        4. **Symptoms Onset**: The body starts showing signs of the disease, such as fever, cough, or fatigue, as the immune system reacts.
        5. **Progression**: The disease may intensify, leading to more severe symptoms, depending on the immune response and treatment.
        6. **Resolution or Chronicity**: With treatment or the body's immune response, the disease may resolve. If untreated, some diseases can become chronic or lead to complications.
    """)
    st.write("""#### Let's go to the different disease predictions:""")

    disease_topics = {
        "Diabetes": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\dibetics.jpg",
        "Heart": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\heart.jpg",
        "Kidney": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\kidney.jpg",
        "Lungs": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\lungs.jpg",
        "Breast Cancer": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\breastcancer.jpg",
        "Parkinson": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\parkinson.jpg",
        "Liver": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\liver.jpg",
    }

    css = """
    <style>
    .circle-image {
        border-radius: 50%;
        width: 200px;
        height: 200px;
        object-fit: cover;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

    cols = st.columns(3)

    for idx, (disease, image_path) in enumerate(disease_topics.items()):
        with cols[idx % 3]:
            st.markdown(
                f'<img src="data:image/jpeg;base64,{get_base64_image(image_path)}" class="circle-image" alt="{disease}">', 
                unsafe_allow_html=True
            )
            button_key = f"Go For Prediction {disease}"
            if st.button(f"Go For Prediction {disease}", key=button_key):
                st.session_state.current_page = "Disease Prediction"
                st.session_state.current_paged = disease  # Switch to the selected disease page

def home_page():
    st.write("Learn more about maintaining a healthy lifestyle by exploring these key topics:")

    topics = {
        "Exercise": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\image3.jpg",
        "Mental Health": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\image2.jpg",
        "Hydration": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\image5.jpg",
        "Balanced Diet": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\image1.jpg",
        "Regular Checkups": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\image4.jpg",
    }

    cols = st.columns(len(topics))

    st.markdown(
        """
        <style>
        .circular-image {
            border-radius: 50%;
            overflow: hidden;
            width: 200px;  
            height: 200px; 
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    for i, (topic, image_path) in enumerate(topics.items()):
        with cols[i]:
            image = Image.open(image_path)
            st.image(image, caption=topic, width=200)
            if st.button(f"Learn more about {topic}", key=f"learn_more_{topic}"):
                st.session_state.current_page = "Home"  # Switch to Home page
                st.session_state.current_pageh = topic  # Set the current topic for further display

def navigation_buttons(page_type):
    col1, col2 = st.columns([4, 1])
    with col2:
        if st.button(f"Go Back to {'Home Page' if page_type == 'home' else 'Disease Prediction Page'}", key="go_back_button"):
            if page_type == 'home':
                st.session_state.current_page = "Home"
                st.session_state.current_pageh = "Home"  # Reset topic
            else:
                st.session_state.current_page = "Disease Prediction"
                st.session_state.current_paged = "disease_prediction_page"  # Reset to the disease prediction page

# Sidebar navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

if 'current_pageh' not in st.session_state:
    st.session_state.current_pageh = "Home"

if 'current_paged' not in st.session_state:
    st.session_state.current_paged = "disease_prediction_page"

with st.sidebar:
    selected_option = option_menu(
        menu_title="Main Menu",
        options=["Home", "Disease Prediction"],
        icons=["house", "activity"],
        menu_icon="cast",
        default_index=0 if st.session_state.current_page == "Home" else 1,
    )

    if selected_option == "Home":
        st.session_state.current_page = "Home"
        st.session_state.current_pageh = "Home"  # Reset to the home topic
    elif selected_option == "Disease Prediction":
        st.session_state.current_page = "Disease Prediction"
        st.session_state.current_paged = "disease_prediction_page"  # Reset to the disease prediction page

# Main content
if st.session_state.current_page == "Home":
    display_welcome()
    home_page()
    if st.session_state.current_pageh in ["Exercise", "Mental Health", "Regular Checkups", "Hydration", "Balanced Diet"]:
        if st.session_state.current_pageh == "Exercise":
            exercise_page()
        elif st.session_state.current_pageh == "Mental Health":
            mental_health_page()
        elif st.session_state.current_pageh == "Regular Checkups":
            checkup_page()
        elif st.session_state.current_pageh == "Hydration":
            hydration_page()
        elif st.session_state.current_pageh == "Balanced Diet":
            balanced_diet_page()
        navigation_buttons(page_type='home')  # Navigation button for home
    # else:
    #     st.write("Page not found.")
elif st.session_state.current_page == "Disease Prediction":
    display_welcome()
    disease_prediction_page()
    if st.session_state.current_paged in ["Diabetes", "Heart", "Parkinson", "Breast Cancer", "Kidney", "Liver", "Lungs"]:
        if st.session_state.current_paged == "Diabetes":
            diabetes_page()
        elif st.session_state.current_paged == "Heart":
            heart_disease_page()
        elif st.session_state.current_paged == "Parkinson":
            parkinsons_page()
        elif st.session_state.current_paged == "Breast Cancer":
            breast_cancer_page()
        elif st.session_state.current_paged == "Kidney":
            kidney_disease_page()
        elif st.session_state.current_paged == "Liver":
            liver_disease_page()
        elif st.session_state.current_paged == "Lungs":
            lung_cancer_page()
        navigation_buttons(page_type='disease')  # Navigation button for disease prediction
    # else:
    #     st.write("Page not found.")

# Disclaimer
st.markdown(
    """
    ---
    <span style="color:red;">**Disclaimer:**  
    This content is developed to demonstrate the capabilities of Machine Learning in the field of Healthcare. The text, graphics, images, and content used is general in nature and for informational purposes only and does not constitute medical advice; the content is not intended to be a substitute for professional medical advice, diagnosis, or treatment. Always consult your doctor or other qualified healthcare provider with any questions you may have regarding a medical condition.**</span>

    <span style="color:red;">**Made with Streamlit**  
    **Built & developed by Milan Kumar Sahoo**</span>
    """,
    unsafe_allow_html=True  # Allow HTML rendering
)


st.markdown(
    """
    <div style="text-align:center; font-size:18px;">
        Made with ❤️ using Streamlit by Milan Kumar Sahoo
    </div>
    """,
    unsafe_allow_html=True,
)
