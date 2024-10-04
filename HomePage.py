
import streamlit as st
import requests
from streamlit_lottie import st_lottie
import os
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from PIL import Image

def get_image_base64(image_path):
    """Convert image file to base64 format."""
    import base64

    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Topic-specific pages
def exercise_page():
    # Set the image path
    image_path = r"D:\2105208_PROGRAM\ML Project\Multiple Disease Prediction System\images\image7.jpg"
    st.markdown(
        """
            <div style="display: flex; justify-content: center;">
                <img src="data:image/jpeg;base64,{}" style="max-width: 100%; width: 300px;">
            </div>
            """.format(
            get_image_base64(image_path)
        ),
        unsafe_allow_html=True,
    )
    st.title("Exercise")
    st.write(
        """
        1. **Physical Health Benefits**: Regular exercise enhances cardiovascular health, strengthens muscles, and improves flexibility. It helps maintain a healthy weight and reduces the risk of chronic diseases like diabetes and heart disease.

        2. **Mental Health Improvement**: Physical activity releases endorphins, which boost mood and alleviate symptoms of depression and anxiety. Exercise can serve as a natural antidepressant.

        3. **Enhanced Cognitive Function**: Engaging in regular physical activity is linked to improved memory, attention, and problem-solving skills. It promotes neurogenesis, contributing to better brain health.

        4. **Stress Relief**: Exercise acts as a healthy outlet for stress, providing a distraction from daily pressures. Activities like yoga or running can enhance relaxation and promote mental clarity.

        5. **Social Interaction**: Group exercises, sports, or fitness classes encourage social connections, reducing feelings of isolation. Building relationships through exercise can foster a sense of community.

        6. **Sleep Quality**: Regular physical activity can improve sleep patterns, helping individuals fall asleep faster and deepening sleep quality. Better sleep enhances overall well-being.

        7. **Goal Setting and Achievement**: Setting fitness goals can boost motivation and self-esteem. Achieving these goals fosters a sense of accomplishment and encourages ongoing participation in physical activities.
        """
    )
    st.write("[Health and Wellness](https://services.india.gov.in/service/listing?cat_id=5&ln=en)")

def mental_health_page():
    image_path = r"D:\2105208_PROGRAM\ML Project\Multiple Disease Prediction System\images\image6.jpg"
    st.markdown(
        """
            <div style="display: flex; justify-content: center;">
                <img src="data:image/jpeg;base64,{}" style="max-width: 100%; width: 300px;">
            </div>
            """.format(
            get_image_base64(image_path)
        ),
        unsafe_allow_html=True,
    )
    st.title("Mental Health")
    st.write(
        """
        1. **Understanding Mental Health**: Mental health encompasses emotional, psychological, and social well-being. It affects how individuals think, feel, and act, influencing daily life and relationships.

        2. **Importance of Awareness**: Raising awareness about mental health is crucial for reducing stigma and encouraging individuals to seek help. Open conversations can foster understanding and acceptance.

        3. **Signs of Mental Health Issues**: Common signs include prolonged sadness, anxiety, changes in appetite or sleep, withdrawal from social activities, and difficulty concentrating. Recognizing these signs early can lead to timely intervention.

        4. **Coping Mechanisms**: Healthy coping strategies, such as mindfulness, meditation, journaling, and engaging in hobbies, can significantly improve mental health. These activities promote relaxation and self-reflection.

        5. **Therapeutic Interventions**: Professional help, including therapy and counseling, can provide individuals with coping strategies and support. Cognitive-behavioral therapy (CBT) is effective for various mental health issues.

        6. **Community Support**: Strong social support systems can enhance mental health. Connecting with friends, family, or support groups fosters a sense of belonging and reduces feelings of isolation.

        7. **Self-Care Practices**: Prioritizing self-care routines, such as maintaining a balanced lifestyle, practicing gratitude, and seeking professional help when needed, is essential for mental well-being.
        """
    )
    st.write("[Mental Health Programme](http://dghs.gov.in/content/1350_3_NationalMentalHealthProgramme.aspx)")

def checkup_page():
    image_path = r"D:\2105208_PROGRAM\ML Project\Multiple Disease Prediction System\images\image8.jpg"
    st.markdown(
        """
            <div style="display: flex; justify-content: center;">
                <img src="data:image/jpeg;base64,{}" style="max-width: 100%; width: 300px;">
            </div>
            """.format(
            get_image_base64(image_path)
        ),
        unsafe_allow_html=True,
    )
    st.title("Regular Checkups")
    st.write(
        """
        1. **Importance of Regular Checkups**: Regular medical checkups are vital for preventive health care. They allow for early detection of health issues, helping to manage conditions before they become severe.

        2. **Screening and Monitoring**: Routine screenings for blood pressure, cholesterol levels, and other health markers are essential. These tests help assess risks and identify potential health problems.

        3. **Vaccination Updates**: Regular checkups provide opportunities to stay up-to-date with vaccinations, ensuring protection against various diseases and enhancing overall community health.

        4. **Personalized Health Plans**: Healthcare professionals can create personalized health plans based on individual health needs, lifestyles, and family histories, ensuring comprehensive care.

        5. **Mental Health Assessment**: Checkups should include mental health assessments, allowing individuals to discuss concerns and seek support for emotional well-being.

        6. **Patient Education**: Regular visits to healthcare providers offer opportunities for patient education on healthy lifestyles, disease prevention, and managing chronic conditions.

        7. **Building a Relationship with Healthcare Providers**: Consistent checkups foster trust and communication between patients and healthcare providers, leading to better health outcomes and proactive care.
    """
    )
    st.write("[Checkup Recommendations](https://mohfw.gov.in/)")

def hydration_page():
    image_path = r"D:\2105208_PROGRAM\ML Project\Multiple Disease Prediction System\images\image9.jpg"
    st.markdown(
        """
            <div style="display: flex; justify-content: center;">
                <img src="data:image/jpeg;base64,{}" style="max-width: 100%; width: 300px;">
            </div>
            """.format(
            get_image_base64(image_path)
        ),
        unsafe_allow_html=True,
    )
    st.title("Hydration")
    st.write(
        """
        1. **Importance of Hydration**: Staying hydrated is crucial for maintaining bodily functions. Water regulates body temperature, aids digestion, and transports nutrients, supporting overall health.

        2. **Daily Water Intake**: The general recommendation is to drink at least 8-10 glasses of water daily. Individual needs may vary based on activity levels, climate, and overall health.

        3. **Signs of Dehydration**: Common symptoms of dehydration include dry mouth, fatigue, dizziness, dark yellow urine, and headache. Recognizing these signs early is essential to prevent complications.

        4. **Benefits of Proper Hydration**: Adequate hydration enhances physical performance, improves cognitive function, and boosts mood. It helps prevent fatigue and keeps the skin healthy and glowing.

        5. **Hydration Sources**: While water is the best source of hydration, fruits and vegetables also contribute. Foods like cucumbers, watermelon, and oranges are high in water content.

        6. **Hydration and Exercise**: Increased fluid intake is vital during exercise to replenish lost fluids. Drinking water before, during, and after physical activity prevents dehydration.

        7. **Hydration in Daily Life**: Incorporating hydration into daily routines, such as carrying a water bottle, setting reminders, and drinking a glass of water with meals, can help maintain proper hydration levels.
        """
    )
    st.write("[Hydration Tips](https://www.ncoa.org/article/10-reasons-why-hydration-is-important/)")

def balanced_diet_page():
    image_path = r"D:\2105208_PROGRAM\ML Project\Multiple Disease Prediction System\images\image10.jpg"
    st.markdown(
        """
            <div style="display: flex; justify-content: center;">
                <img src="data:image/jpeg;base64,{}" style="max-width: 100%; width: 300px;">
            </div>
            """.format(
            get_image_base64(image_path)
        ),
        unsafe_allow_html=True,
    )
    st.title("Balanced Diet")
    st.write(
        """
        1. **Definition of a Balanced Diet**: A balanced diet includes a variety of foods in the right proportions, providing essential nutrients: carbohydrates, proteins, fats, vitamins, and minerals necessary for overall health.

        2. **Nutritional Benefits**: Consuming a balanced diet supports healthy growth, development, and overall well-being. It helps maintain a healthy weight, reduces the risk of chronic diseases, and enhances energy levels.

        3. **Food Groups**: Key food groups include fruits, vegetables, whole grains, lean proteins, and healthy fats. Incorporating diverse foods ensures a range of nutrients necessary for bodily functions.

        4. **Portion Control**: Understanding portion sizes is vital to avoid overeating. Using smaller plates, measuring servings, and being mindful of hunger cues can help maintain appropriate portions.

        5. **Hydration**: A balanced diet should include adequate hydration, primarily through water intake. Hydration is crucial for digestion, nutrient absorption, and maintaining energy levels.

        6. **Meal Planning**: Planning meals ahead can help ensure a balanced diet. It encourages mindful eating, reduces food waste, and allows for better control over nutritional intake.

        7. **Long-term Health**: Adopting a balanced diet contributes to long-term health benefits, including improved heart health, better digestive health, enhanced immune function, and overall longevity.
        """
    )
    st.write("[Balanced Diet Information](https://www.who.int/news-room/fact-sheets/detail/healthy-diet)")

# def navigation_buttons_home():
#     """Display navigation buttons on the right side of the page."""
#     col1, col2 = st.columns([4, 1])  # Create two columns: left and right
#     with col1:
#         st.write("")  # Leave this column empty or add content if needed

#     with col2:
#         if st.button("Go Back to Home Page", key="go_back_button"):
#             st.session_state.current_page = "Home"  # Switch to home page


# def home_page():

#     st.write("Learn more about maintaining a healthy lifestyle by exploring these key topics:")

#     topics = {
#         "Exercise": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\image3.jpg",
#         "Mental Health": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\image2.jpg",
#         "Regular Checkups": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\image4.jpg",
#         "Hydration": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\image5.jpg",
#         "Balanced Diet": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\image1.jpg",
#     }
#     # Create a container for the topics
#     cols = st.columns(len(topics))  # Create columns for each topic

#     # Add custom CSS for circular images once
#     st.markdown(
#         """
#         <style>
#         .circular-image {
#             border-radius: 50%;
#             overflow: hidden;
#             width: 200px;  /* Set width for the circular shape */
#             height: 200px; /* Set height for the circular shape */
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     for i, (topic, image_path) in enumerate(topics.items()):
#         with cols[i]:  # Use the column context
#             # Load and display the image
#             image = Image.open(image_path)
            
#             # Display circular images with CSS class
#             st.image(image, caption=topic, width=200, use_column_width=True)  # Use default behavior for now
            
#             # Add a button for each topic with a unique key
#             if st.button(f"Learn more about {topic}", key=f"learn_more_{topic}"):
#                 st.session_state.current_page = topic 



# if 'current_page' not in st.session_state:
#     st.session_state.current_page = "Home"  # Default to home

# if st.session_state.current_page == "Home":
#     home_page()
# elif st.session_state.current_page == "Exercise":
#     exercise_page()
#     navigation_buttons_home()
# elif st.session_state.current_page == "Mental Health":
#     mental_health_page()
#     navigation_buttons_home()
# elif st.session_state.current_page == "Regular Checkups":
#     checkup_page()
#     navigation_buttons_home()
# elif st.session_state.current_page == "Hydration":
#     hydration_page()
#     navigation_buttons_home()
# elif st.session_state.current_page == "Balanced Diet":
#     balanced_diet_page()
#     navigation_buttons_home()
# else:
#     st.write("Page not found.")



# # Disclaimer
# st.markdown(
#     """
#     ---
#     **Disclaimer:**  
#     This content is developed to demonstrate the capabilities of Machine Learning in the field of Healthcare. The text, graphics, images, and content used is general in nature and for informational purposes only and does not constitute medical advice; the content is not intended to be a substitute for professional medical advice, diagnosis, or treatment. Always consult your doctor or other qualified healthcare provider with any questions you may have regarding a medical condition.
    
#     **Made with Streamlit**  
#     **Built & developed by Milan Kumar Sahoo**
# """
# )

# st.markdown(
#     """
#     <div style="text-align:center; font-size:18px;">
#         Made with ❤️ using Streamlit by Milan Kumar Sahoo
#     </div>
#     """,
#     unsafe_allow_html=True,
# ) 

