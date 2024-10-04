
import os
import pickle
import streamlit as st
from PIL import Image
import base64
import joblib
import requests
from streamlit_lottie import st_lottie
from joblib import load

# Get the working directory of the current script
working_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the models
models_dir = os.path.join(working_dir, "DatasetModel")  # Adjust the directory name if needed

# Loading the saved models
diabetes_model = joblib.load(
    os.path.join(models_dir, "diabetes_model.joblib")
)

heart_disease_model = joblib.load(
    os.path.join(models_dir, "heart_disease_model.joblib")
)

parkinsons_model = joblib.load(
    os.path.join(models_dir, "parkinsons_model.joblib")
)

breast_cancer_model = joblib.load(
    os.path.join(models_dir, "breast_cancer.joblib")
)

lung_cancer_model = joblib.load(
    os.path.join(models_dir, "lung_cancer_model.joblib")
)

kidney_disease_model = joblib.load(
    os.path.join(models_dir, "kidney_disease.joblib")
)

liver_disease_model = joblib.load(
    os.path.join(models_dir, "liver.joblib")
)


def diabetes_page():
    # Function to load Lottie animations from URL
    def load_lottie_url(url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        st.error(f"Failed to load Lottie animation from {url}")
        return None

    # Left, middle, and right Lottie animation URLs
    left_animation_url = ("https://lottie.host/4ab409b6-8297-4161-9c0d-c531ab8b39a9/agpua2BZms.json")
    middle_animation_url = ("https://lottie.host/20964f4c-483a-4349-a93b-9b417c6f20c7/mPKJTJllTE.json")
    right_animation_url = ("https://lottie.host/4ab409b6-8297-4161-9c0d-c531ab8b39a9/agpua2BZms.json")  # Same as middle

    # Create a flex container using Streamlit's layout
    col1, col2, col3 = st.columns(3)  # 3 equal columns

    # Set width and height for Lottie animations
    animation_width = 150
    animation_height = 150

    # Left animation
    with col1:
        st_lottie(
            load_lottie_url(left_animation_url),
            width=animation_width,
            height=animation_height,
        )

    # Middle animation
    with col2:
        st_lottie(
            load_lottie_url(middle_animation_url),
            width=animation_width,
            height=animation_height,
        )

    # Right animation
    with col3:
        st_lottie(
            load_lottie_url(right_animation_url),
            width=animation_width,
            height=animation_height,
        )
    st.title("Diabetes Disease Assessment")
    # Create Tabs
    tab1, tab2, tab3 = st.tabs(["About", "Make Prediction", "Remedies"])

    # Tab 1: About
    with tab1:
        st.header("What is Diabetes?")
        st.write(
            """
    - **Definition**: A metabolic disease that leads to high blood sugar levels.
    - **Insulin Role**: Insulin is a hormone that facilitates the movement of sugar from the blood into cells for energy storage and usage.
    - **Malfunction**: Diabetes occurs when the body either doesn't produce enough insulin or cannot effectively utilize the insulin produced.
    - **Consequences**: Untreated high blood sugar can damage nerves, eyes, kidneys, and other organs.
    - **Management**: Educating oneself about diabetes and taking proactive measures can help manage and prevent complications.

    ### Health Parameters for Diabetes Prediction (Only for Females)
    1. **Number of Pregnancies**: Multiple pregnancies can increase insulin resistance and the risk of gestational diabetes, which may lead to type 2 diabetes later.
    2. **Triceps Skin Fold Thickness (mm)**: Higher skin fold thickness indicates increased body fat, which can lead to insulin resistance.
    3. **Diabetes Pedigree Function**: A family history of diabetes increases the likelihood of developing the condition due to genetic factors.
    4. **Plasma Glucose Concentration**: Elevated glucose levels indicate impaired insulin function, a key factor in diagnosing diabetes.
    5. **2-Hour Serum Insulin (mu U/ml)**: Insulin levels help assess how well the body responds to glucose, influencing diabetes risk.
    6. **Age (years)**: Older age increases the risk of developing type 2 diabetes due to declining insulin sensitivity and beta-cell function.
    7. **Diastolic Blood Pressure (mm Hg)**: High diastolic blood pressure is associated with insulin resistance and increased risk of cardiovascular complications in diabetics.
    8. **Body Mass Index (BMI)**: A higher BMI is linked to increased fat accumulation, leading to greater insulin resistance and a higher risk of type 2 diabetes.

    ### Types of Diabetes
    1. **Type 1 Diabetes**: 
    - An autoimmune disease that destroys insulin-producing cells in the pancreas.
    - Cause of immune system attack is unclear.
    
    2. **Type 2 Diabetes**:
    - The most common type, accounting for 90-95% of diabetes cases.
    - Occurs when the body becomes resistant to insulin, causing sugar to build up in the blood.

    3. **Type 1.5 Diabetes (LADA)**:
    - Also known as latent autoimmune diabetes in adults.
    - Gradual onset in adulthood, similar to type 2 diabetes.
    - Not treatable by diet or lifestyle changes.

    4. **Gestational Diabetes**:
    - High blood sugar that occurs during pregnancy due to insulin-blocking hormones from the placenta.

    5. **Diabetes Insipidus**:
    - A rare condition not related to diabetes mellitus.
    - Characterized by excessive fluid removal by kidneys.

    ### Symptoms of Diabetes
    - **General Symptoms**:
    - Increased hunger
    - Increased thirst
    - Weight loss
    - Frequent urination
    - Blurry vision
    - Extreme fatigue
    - Sores that do not heal

    - **Symptoms in Men**:
    - Decreased sex drive
    - Erectile dysfunction
    - Poor muscle strength

    - **Symptoms in Women**:
    - Vaginal dryness
    - Urinary tract infections
    - Yeast infections
    - Dry, itchy skin

    - **Gestational Diabetes Symptoms**:
    - Often asymptomatic, but may include increased thirst or urination in rare cases.
    - Usually detected during routine blood tests.

    ### Conclusion
    - **Detection**: Symptoms can be mild and may go unnoticed initially.
    - **Action**: Recognizing symptoms early can prompt timely medical consultation.
        """
        )
        st.markdown(
            "[Learn More](https://my.clevelandclinic.org/health/diseases/7104-diabetes)"
        )

    # Tab 2: Make Prediction
    with tab2:
        st.header("Diabetes Prediction (Only for Females)")
        st.write(
            "Enter the following health parameters to predict if you are diabetic:"
        )

        # Collect input data
        col1, col2, col3 = st.columns(3)

        with col1:
            Pregnancies = st.text_input("Number of Pregnancies")

        with col2:
            Glucose = st.text_input("Plasma Glucose Concentration")

        with col3:
            BloodPressure = st.text_input("Diastolic Blood Pressure (mm Hg)")

        with col1:
            SkinThickness = st.text_input("Triceps Skin Fold Thickness (mm)")

        with col2:
            Insulin = st.text_input("2-Hour Serum Insulin (mu U/ml)")

        with col3:
            BMI = st.text_input("Body Mass Index (weight in kg/(height in m)^2)")

        with col1:
            DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")

        with col2:
            Age = st.text_input("Age (years)")

        # Prediction button
        if st.button("Get Diabetes Prediction"):
            # Check if any input is empty
            if (
                not Pregnancies
                or not Glucose
                or not BloodPressure
                or not SkinThickness
                or not Insulin
                or not BMI
                or not DiabetesPedigreeFunction
                or not Age
            ):
                st.error("Please fill all the boxes before making a prediction.")
            else:
                try:
                    # Collect input data and make prediction
                    user_input = [
                        float(Pregnancies),
                        float(Glucose),
                        float(BloodPressure),
                        float(SkinThickness),
                        float(Insulin),
                        float(BMI),
                        float(DiabetesPedigreeFunction),
                        float(Age),
                    ]

                    diab_prediction = diabetes_model.predict([user_input])

                    if diab_prediction[0] == 1:
                        diab_diagnosis = "The person is diabetic"
                    else:
                        diab_diagnosis = "The person is not diabetic"

                    st.success(diab_diagnosis)

                except ValueError:
                    st.error("Please enter valid numeric values in all fields.")

        st.warning(
            "**Note:** This prediction is designed specifically for females based on the input parameters."
        )

    # Tab 3: Remedies
    with tab3:
        st.header("Remedies and Treatment for Diabetes")
        st.write(
            """
        Managing diabetes involves lifestyle changes like regular exercise, maintaining a balanced diet, and monitoring blood sugar levels. 
        Medications like insulin and other drugs may also be required. Consult a healthcare provider for a tailored treatment plan.
        """
        )
        st.markdown(
            "[Learn More](https://www.stamfordhealth.org/healthflash-blog/diabetes-and-endocrine/type-2-diabetes-natural-remedies/)"
        )



def heart_disease_page():
    # Function to load Lottie animations from URL
    def load_lottie_url(url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        st.error(f"Failed to load Lottie animation from {url}")
        return None

    # Left, middle, and right Lottie animation URLs
    left_animation_url = (
        "https://lottie.host/ca70c368-b0d2-42ce-b3c7-b069fdc9cbba/vYJ82qthEw.json"
    )
    middle_animation_url = (
        "https://lottie.host/e332cd18-6e8e-4f51-8d37-7c5f43427f91/Y7vt3ky1Z1.json"
    )
    right_animation_url = "https://lottie.host/ca70c368-b0d2-42ce-b3c7-b069fdc9cbba/vYJ82qthEw.json"  # Same as middle

    # Create a flex container using Streamlit's layout
    col1, col2, col3 = st.columns(3)  # 3 equal columns

    # Set width and height for Lottie animations
    animation_width = 150
    animation_height = 150

    # Left animation
    with col1:
        st_lottie(
            load_lottie_url(left_animation_url),
            width=animation_width,
            height=animation_height,
        )

    # Middle animation
    with col2:
        st_lottie(
            load_lottie_url(middle_animation_url),
            width=animation_width,
            height=animation_height,
        )

    # Right animation
    with col3:
        st_lottie(
            load_lottie_url(right_animation_url),
            width=animation_width,
            height=animation_height,
        )
    st.title("Heart Disease Assessment")
    # Create Tabs
    tab1, tab2, tab3 = st.tabs(["About", "Make Prediction", "Remedies"])

    # Tab 1: About
    with tab1:
        st.header("What is Heart Disease?")
        st.write(
            """
        - Discomfort/pain along the front body, between neck and upper abdomen.
        - Common symptom of poor blood flow to the heart or heart attack (angina).
        - Can vary from mild discomfort to crushing pain.
        - Pain may spread to the neck, arms, stomach, jaw, or upper back.
        - May feel heavy, squeezing, sharp, or burning.
        - Triggered by activity or emotion, relieved by rest or nitroglycerin.
        - Can also be caused by indigestion.
        - Women, older adults, and diabetics may have no chest pain or atypical symptoms (e.g., fatigue, shortness of breath).

        ### Other Symptoms of a Heart Attack
        - Extreme anxiety
        - Fainting, lightheadedness, or dizziness
        - Nausea or vomiting
        - Palpitations
        - Heavy sweating

        ### Shortness of Breath
        - Due to heart failure and fluid build-up in lungs.
        - Occurs during activity, rest, or while lying flat.
        - May cause coughing or wheezing, possibly with pink or bloody mucus.

        ### Swelling (Edema)
        - Swelling in legs, ankles, feet, or stomach.
        - Caused by slow blood flow and fluid build-up.
        - May be accompanied by weight gain.

        ### Poor Blood Supply to Extremities
        - Narrowed arteries increase heart attack risk.
        - Causes pain, fatigue, or discomfort in legs during activity.
        - Numbness or coolness in legs or feet at rest.

        ### Stroke Symptoms
        - Difficulty moving or loss of sensation on one side.
        - Face drooping, speech problems, or language difficulty.

        ### Fatigue
        - Unusual tiredness, especially in women before/during a heart attack.
        - Extreme weakness, unable to perform daily activities.

        ### Fast or Uneven Heartbeat (Palpitations)
        - Heart may race or throb to compensate for poor pumping.
        - Can indicate arrhythmia (irregular heart rhythm).
                """
        )
        st.markdown(
            "[Learn More](https://www.who.int/news-room/fact-sheets/detail/climate-change-heat-and-health)"
        )

    # Tab 2: Make Prediction
    with tab2:
        # Page title
        st.title('Heart Disease Prediction')
        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.text_input('Age')

        with col2:
            sex = st.radio('Sex', options=[1, 0], index=0, format_func=lambda x: 'Male' if x == 1 else 'Female')

        with col3:
            cp = st.radio('Chest Pain Types', options=[0, 1, 2, 3])

        with col1:
            trestbps = st.text_input('Resting Blood Pressure')

        with col2:
            chol = st.text_input('Serum Cholestoral in mg/dl')

        with col3:
            fbs = st.radio('Fasting Blood Sugar > 120 mg/dl', options=[1, 0], index=1)

        with col1:
            restecg = st.radio('Resting Electrocardiographic Results', options=[0, 1, 2])

        with col2:
            thalach = st.text_input('Maximum Heart Rate Achieved')

        with col3:
            exang = st.radio('Exercise Induced Angina', options=[1, 0], index=1)

        with col1:
            oldpeak = st.text_input('ST Depression Induced by Exercise')

        with col2:
            slope = st.text_input('Slope of the Peak Exercise ST Segment')

        with col3:
            ca = st.text_input('Major Vessels Colored by Flourosopy (0-3)')

        with col1:
            thal = st.radio('Thal', options=[0, 1, 2], index=0, format_func=lambda x: 'Normal' if x == 0 else ('Fixed Defect' if x == 1 else 'Reversible Defect'))

        # Prediction and validation
        heart_diagnosis = ''

        if st.button('Heart Disease Test Result'):
            if all([age, trestbps, chol, thalach, oldpeak, slope, ca]):
                user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
                user_input = [float(x) for x in user_input]

                heart_prediction = heart_disease_model.predict([user_input])

                if heart_prediction[0] == 1:
                    heart_diagnosis = 'The person is having heart disease'
                else:
                    heart_diagnosis = 'The person does not have any heart disease'

                st.success(heart_diagnosis)
            else:
                st.error('Please fill all the fields!')
    # Tab 3: Remedies
    with tab3:
        st.header("Remedies and Treatment")
        st.write(
            """
            ### Remedies and Treatment
            Managing heart disease often involves a combination of lifestyle changes, medications, and sometimes medical procedures. A healthy lifestyle plays a crucial role in preventing and managing heart disease. This includes eating a heart-healthy diet rich in fruits, vegetables, whole grains, lean proteins, and healthy fats such as omega-3 fatty acids. Regular physical activity is essential, with at least 30 minutes of moderate exercise most days of the week being recommended. Quitting smoking is also critical, as smoking is a major risk factor for heart disease. Limiting alcohol intake and managing stress through relaxation techniques like yoga, meditation, or deep breathing exercises can further help reduce heart disease risk. Maintaining a healthy weight is also important to minimize stress on the heart.

            Medications are often prescribed to manage heart disease. Blood pressure medications, such as ACE inhibitors and beta-blockers, help control high blood pressure. Cholesterol-lowering drugs like statins reduce plaque build-up in the arteries, while antiplatelet drugs, like aspirin, prevent blood clots and reduce the risk of heart attacks. In some cases, anticoagulants (blood thinners) are used to prevent clot formation. For individuals with advanced heart disease, medical procedures such as angioplasty, stent placement, or bypass surgery may be necessary to restore proper blood flow to the heart. Following a treatment plan tailored to individual needs, under a healthcare provider's guidance, is vital for managing heart disease effectively.
            """
        )
        st.markdown(
            "[Learn More](https://www.nhs.uk/conditions/coronary-heart-disease/treatment/)"
        )



def parkinsons_page():
    # Function to load Lottie animations from URL
    def load_lottie_url(url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        st.error(f"Failed to load Lottie animation from {url}")
        return None

    # Left, middle, and right Lottie animation URLs
    left_animation_url = ("https://lottie.host/b7851483-cd8a-411b-8504-3081cc176210/jjqHnILeWW.json")
    middle_animation_url = ("https://lottie.host/ce44f556-7973-408b-a4b8-59c266153ecf/kAjVMaNC5Y.json")
    right_animation_url = ("https://lottie.host/b7851483-cd8a-411b-8504-3081cc176210/jjqHnILeWW.json") # Same as middle

    # Create a flex container using Streamlit's layout
    col1, col2, col3 = st.columns(3)  # 3 equal columns

    # Set width and height for Lottie animations
    animation_width = 150
    animation_height = 150

    # Left animation
    with col1:
        st_lottie(
            load_lottie_url(left_animation_url),
            width=animation_width,
            height=animation_height,
        )

    # Middle animation
    with col2:
        st_lottie(
            load_lottie_url(middle_animation_url),
            width=animation_width,
            height=animation_height,
        )

    # Right animation
    with col3:
        st_lottie(
            load_lottie_url(right_animation_url),
            width=animation_width,
            height=animation_height,
        )
    st.title("Parkinson Disease Assessment")
    # Create Tabs
    tab1, tab2, tab3 = st.tabs(["About", "Make Prediction", "Remedies"])

    # Tab 1: About
    with tab1:
        st.header("What is Parkinsons Disease?")
        st.write( """
        Parkinson's disease is a progressive neurological disorder that primarily affects movement. It occurs when the nerve cells in the brain that produce dopamine, a neurotransmitter responsible for coordinating movement, begin to degenerate or die. This leads to a range of motor symptoms, including tremors, rigidity, slowness of movement, and balance issues. Non-motor symptoms such as sleep disturbances, depression, and cognitive changes can also occur, significantly impacting daily life and quality of life. Although the exact cause of Parkinson's disease is unknown, a combination of genetic and environmental factors is believed to contribute to its development.
        """
        )
        st.markdown(
            "[Learn More](https://www.ninds.nih.gov/health-information/disorders/parkinsons-disease)"
        )

    # Tab 2: Make Prediction
    with tab2:
        # Page title
        st.title("Parkinson's Disease Prediction")

        # Creating input fields for each parameter
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            fo = st.text_input("Average vocal fundamental frequency (MDVP:Fo(Hz))")
        with col2:
            fhi = st.text_input("Maximum vocal fundamental frequency (MDVP:Fhi(Hz))")
        with col3:
            flo = st.text_input("Minimum vocal fundamental frequency (MDVP:Flo(Hz))")
        with col4:
            Jitter_percent = st.text_input("MDVP:Jitter(%) - Variation in fundamental frequency")
        with col5:
            Jitter_Abs = st.text_input("MDVP:Jitter(Abs) - Absolute variation in fundamental frequency")

        with col1:
            RAP = st.text_input("MDVP:RAP - Relative Amplitude Perturbation")
        with col2:
            PPQ = st.text_input("MDVP:PPQ - Five-Point Period Perturbation Quotient")
        with col3:
            DDP = st.text_input("Jitter:DDP - Average absolute difference of differences between successive periods")
        with col4:
            Shimmer = st.text_input("MDVP:Shimmer - Variation in amplitude")
        with col5:
            Shimmer_dB = st.text_input("MDVP:Shimmer(dB) - Logarithmic variation in amplitude")

        with col1:
            APQ3 = st.text_input("Shimmer:APQ3 - Amplitude Perturbation Quotient over 3 cycles")
        with col2:
            APQ5 = st.text_input("Shimmer:APQ5 - Amplitude Perturbation Quotient over 5 cycles")
        with col3:
            APQ = st.text_input("MDVP:APQ - Amplitude Perturbation Quotient")
        with col4:
            DDA = st.text_input("Shimmer:DDA - Average absolute difference of differences between successive amplitudes")
        with col5:
            NHR = st.text_input("NHR - Noise-to-Harmonics Ratio")

        with col1:
            HNR = st.text_input("HNR - Harmonics-to-Noise Ratio")
        with col2:
            RPDE = st.text_input("RPDE - Recurrence Period Density Entropy")
        with col3:
            DFA = st.text_input("DFA - Signal fractal scaling exponent")
        with col4:
            spread1 = st.text_input("spread1 - Nonlinear measure of fundamental frequency variation")
        with col5:
            spread2 = st.text_input("spread2 - Nonlinear measure of fundamental frequency variation")

        with col1:
            D2 = st.text_input("D2 - Nonlinear dynamical complexity measure")
        with col2:
            PPE = st.text_input("PPE - Pitch Period Entropy")

        # Code for Prediction
        parkinsons_diagnosis = ""

        # Creating a button for Prediction
        if st.button("Parkinson's Test Result"):

            # Check if all fields are filled
            if any(field == "" for field in [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]):
                st.warning("Please fill in all the boxes.")
            else:
                # Convert inputs to float
                user_input = [
                    float(fo),
                    float(fhi),
                    float(flo),
                    float(Jitter_percent),
                    float(Jitter_Abs),
                    float(RAP),
                    float(PPQ),
                    float(DDP),
                    float(Shimmer),
                    float(Shimmer_dB),
                    float(APQ3),
                    float(APQ5),
                    float(APQ),
                    float(DDA),
                    float(NHR),
                    float(HNR),
                    float(RPDE),
                    float(DFA),
                    float(spread1),
                    float(spread2),
                    float(D2),
                    float(PPE),
                ]

                # Make prediction
                parkinsons_prediction = parkinsons_model.predict([user_input])

                if parkinsons_prediction[0] == 1:
                    parkinsons_diagnosis = "The person has Parkinson's disease"
                else:
                    parkinsons_diagnosis = "The person does not have Parkinson's disease"

                st.success(parkinsons_diagnosis)


    # Tab 3: Remedies
    with tab3:
        st.header("Remedies and Treatment ")
        st.write(
            """
        While there is currently no cure for Parkinson's disease, various treatments and remedies can help manage symptoms and improve quality of life. Medications are often the first line of treatment, with levodopa being the most effective. Levodopa is converted to dopamine in the brain, helping to alleviate motor symptoms. Other medications, such as dopamine agonists and MAO-B inhibitors, may also be prescribed to help manage symptoms.

In addition to medication, lifestyle modifications can be beneficial. Regular physical exercise is crucial, as it can improve mobility, flexibility, and balance. Engaging in activities like walking, swimming, or tai chi can enhance overall physical well-being. Occupational and physical therapy can provide personalized strategies to manage daily activities and maintain independence. Furthermore, speech therapy may be useful for those experiencing communication difficulties.

Diet also plays a significant role in managing Parkinson's disease. A well-balanced diet rich in fruits, vegetables, whole grains, and lean proteins can support overall health. Some studies suggest that antioxidants, found in foods like berries and green leafy vegetables, may help protect brain cells.

In more advanced stages of Parkinson's disease, surgical options like deep brain stimulation (DBS) may be considered. This involves implanting a device that sends electrical impulses to specific brain regions, reducing symptoms and improving quality of life. Overall, a comprehensive approach involving medication, lifestyle changes, and support can significantly enhance the management of Parkinson's disease.
        """
        )
        st.markdown(
            "[Learn More](https://www.mayoclinic.org/diseases-conditions/parkinsons-disease/diagnosis-treatment/drc-20376062)"
        )

    '''
    # Display disclaimer
    st.markdown("""
        <div style="color: red; font-weight: bold;">
            <p>Disclaimer: This application is for informational purposes only. 
            It is not intended to provide medical advice, diagnosis, or treatment. 
            Always seek the advice of your physician or other qualified health provider 
            with any questions you may have regarding a medical condition.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        <div style="text-align:center; font-size:18px;">
            Made with ❤️ using Streamlit by Milan Kumar Sahoo
        </div>
        """,
        unsafe_allow_html=True,
    )
    '''


def breast_cancer_page():
    # Function to load Lottie animations from URL
    def load_lottie_url(url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        st.error(f"Failed to load Lottie animation from {url}")
        return None

    # Left, middle, and right Lottie animation URLs
    left_animation_url = ("https://lottie.host/2b059688-42d5-4384-b794-6044945177bb/WkbDVniQ1L.json")
    middle_animation_url = ("https://lottie.host/93b960d1-a273-42b1-89c9-06d6f9fff12a/61VI2eKIkW.json")
    right_animation_url = ("https://lottie.host/2b059688-42d5-4384-b794-6044945177bb/WkbDVniQ1L.json") # Same as middle

    # Create a flex container using Streamlit's layout
    col1, col2, col3 = st.columns(3)  # 3 equal columns

    # Set width and height for Lottie animations
    animation_width = 150
    animation_height = 150

    # Left animation
    with col1:
        st_lottie(
            load_lottie_url(left_animation_url),
            width=animation_width,
            height=animation_height,
        )

    # Middle animation
    with col2:
        st_lottie(
            load_lottie_url(middle_animation_url),
            width=animation_width,
            height=animation_height,
        )

    # Right animation
    with col3:
        st_lottie(
            load_lottie_url(right_animation_url),
            width=animation_width,
            height=animation_height,
        )

    st.title("Breast Cancer Disease Assessment")
    # Create Tabs
    tab1, tab2, tab3 = st.tabs(["About", "Make Prediction", "Remedies"])

    # Tab 1: About
    with tab1:
        st.header("Breast Cancer Overview")
        st.write(
            """
    Breast cancer is a type of cancer that forms in the cells of the breasts. It can occur in both men and women, though it is far more common in women. The disease is characterized by the uncontrolled growth of breast cells, which can lead to the formation of tumors. Early detection through screening methods like mammograms, clinical exams, and self-exams can significantly increase the chances of successful treatment. Risk factors for breast cancer include genetics (family history), age, certain reproductive history, lifestyle factors such as alcohol consumption, obesity, and lack of physical activity, as well as exposure to radiation.

    ### Symptoms

    Common symptoms of breast cancer may include a lump or mass in the breast, changes in the size or shape of the breast, changes in the skin or appearance of the nipple, and unusual discharge from the nipple. However, early-stage breast cancer may not present any noticeable symptoms, making regular screening essential for early detection. 

    ### Treatment Options

    Treatment for breast cancer typically involves a combination of surgery, radiation therapy, chemotherapy, hormone therapy, and targeted therapy, depending on the type and stage of cancer. Surgery may involve lumpectomy (removing the tumor) or mastectomy (removing one or both breasts). Radiation therapy is often used to eliminate remaining cancer cells after surgery. Chemotherapy uses drugs to kill rapidly dividing cancer cells, while hormone therapy can block hormones that fuel some breast cancers. Targeted therapy employs drugs that specifically attack cancer cells without harming normal cells.
    """
        )
        st.markdown(
            "[Learn More](https://www.who.int/news-room/fact-sheets/detail/breast-cancer)"
        )

    # Tab 2: Make Prediction
    with tab2:
        st.header("Breast Cancer Prediction (Only for Females)")
        
        # Getting the input data from the user
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            id = st.text_input("ID Number")

        with col2:
            radius_mean = st.text_input("Radius Mean")

        with col3:
            texture_mean = st.text_input("Texture Mean")

        with col4:
            perimeter_mean = st.text_input("Perimeter Mean")

        with col5:
            area_mean = st.text_input("Area Mean")

        with col1:
            smoothness_mean = st.text_input("Smoothness Mean")

        with col2:
            compactness_mean = st.text_input("Compactness Mean")

        with col3:
            concavity_mean = st.text_input("Concavity Mean")

        with col4:
            concave_points_mean = st.text_input("Concave Points Mean")

        with col5:
            symmetry_mean = st.text_input("Symmetry Mean")

        with col1:
            fractal_dimension_mean = st.text_input("Fractal Dimension Mean")

        with col2:
            radius_se = st.text_input("Radius SE")

        with col3:
            texture_se = st.text_input("Texture SE")

        with col4:
            perimeter_se = st.text_input("Perimeter SE")

        with col5:
            area_se = st.text_input("Area SE")

        with col1:
            smoothness_se = st.text_input("Smoothness SE")

        with col2:
            compactness_se = st.text_input("Compactness SE")

        with col3:
            concavity_se = st.text_input("Concavity SE")

        with col4:
            concave_points_se = st.text_input("Concave Points SE")

        with col5:
            symmetry_se = st.text_input("Symmetry SE")

        with col1:
            fractal_dimension_se = st.text_input("Fractal Dimension SE")

        with col2:
            radius_worst = st.text_input("Radius Worst")

        with col3:
            texture_worst = st.text_input("Texture Worst")

        with col4:
            perimeter_worst = st.text_input("Perimeter Worst")

        with col5:
            area_worst = st.text_input("Area Worst")

        with col1:
            smoothness_worst = st.text_input("Smoothness Worst")

        with col2:
            compactness_worst = st.text_input("Compactness Worst")

        with col3:
            concavity_worst = st.text_input("Concavity Worst")

        with col4:
            concave_points_worst = st.text_input("Concave Points Worst")

        with col5:
            symmetry_worst = st.text_input("Symmetry Worst")

        with col1:
            fractal_dimension_worst = st.text_input("Fractal Dimension Worst")

        # Code for Prediction
        breast_cancer_check = ""

        if st.button("Breast Cancer Test Result"):
            user_input = [
                radius_mean,
                texture_mean,
                perimeter_mean,
                area_mean,
                smoothness_mean,
                compactness_mean,
                concavity_mean,
                concave_points_mean,
                symmetry_mean,
                fractal_dimension_mean,
                radius_se,
                texture_se,
                perimeter_se,
                area_se,
                smoothness_se,
                compactness_se,
                concavity_se,
                concave_points_se,
                symmetry_se,
                fractal_dimension_se,
                radius_worst,
                texture_worst,
                perimeter_worst,
                area_worst,
                smoothness_worst,
                compactness_worst,
                concavity_worst,
                concave_points_worst,
                symmetry_worst,
                fractal_dimension_worst,
            ]

            # Check if all fields are filled
            if any(x == "" for x in user_input):
                st.error("Please fill all fields with valid numeric values.")
            else:
                try:
                    # Convert to float
                    user_input = [float(x) for x in user_input]

                    # Make prediction
                    prediction = breast_cancer.predict([user_input])

                    if prediction[0] == 0:
                        breast_cancer_check = "Hurrah! You have Benign Breast Cancer."
                    else:
                        breast_cancer_check = "Sorry! You have Malignant Breast Cancer."
                except ValueError:
                    st.error("Please ensure all inputs are numeric.")

        st.success(breast_cancer_check)

        st.warning(
            "**Note:** This prediction is designed specifically for females based on the input parameters."
        )

    # Tab 3: Remedies
    with tab3:
        st.header("### Remedies and Supportive Care")
        st.write(
            """
    In addition to conventional medical treatments, several complementary therapies can support breast cancer patients. These include a balanced diet rich in fruits, vegetables, whole grains, and lean proteins to boost overall health. Regular physical activity can help reduce fatigue and improve mental well-being. Psychological support through counseling or support groups can help patients cope with the emotional challenges of a breast cancer diagnosis. Mindfulness practices like yoga and meditation may also contribute to emotional health and stress reduction. Furthermore, discussing any interest in complementary therapies with a healthcare provider ensures they align with the overall treatment plan and support the patient's health. 
    """
        )
        st.markdown(
            "[Learn More](https://www.cancer.gov/types/breast/patient/breast-treatment-pdq)"
        )

    '''
    # Display disclaimer
    st.markdown("""
        <div style="color: red; font-weight: bold;">
            <p>Disclaimer: This application is for informational purposes only. 
            It is not intended to provide medical advice, diagnosis, or treatment. 
            Always seek the advice of your physician or other qualified health provider 
            with any questions you may have regarding a medical condition.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        <div style="text-align:center; font-size:18px;">
            Made with ❤️ using Streamlit by Milan Kumar Sahoo
        </div>
        """,
        unsafe_allow_html=True,
    )
    '''


def lung_cancer_page():
    # Function to load Lottie animations from URL
    def load_lottie_url(url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        st.error(f"Failed to load Lottie animation from {url}")
        return None

    # Left, middle, and right Lottie animation URLs
    left_animation_url = ("https://lottie.host/4ab409b6-8297-4161-9c0d-c531ab8b39a9/agpua2BZms.json")
    middle_animation_url = ("https://lottie.host/8ed4646c-6580-4caf-8451-937013ed7f26/vk4aYoYeXT.json")
    right_animation_url = ("https://lottie.host/4ab409b6-8297-4161-9c0d-c531ab8b39a9/agpua2BZms.json")  # Same as middle

    # Create a flex container using Streamlit's layout
    col1, col2, col3 = st.columns(3)  # 3 equal columns

    # Set width and height for Lottie animations
    animation_width = 150
    animation_height = 150

    # Left animation
    with col1:
        st_lottie(
            load_lottie_url(left_animation_url),
            width=animation_width,
            height=animation_height,
        )

    # Middle animation
    with col2:
        st_lottie(
            load_lottie_url(middle_animation_url),
            width=animation_width,
            height=animation_height,
        )

    # Right animation
    with col3:
        st_lottie(
            load_lottie_url(right_animation_url),
            width=animation_width,
            height=animation_height,
        )
    st.title(" Lungs Cancer Assessment")
    # Create Tabs
    tab1, tab2, tab3 = st.tabs(["About", "Make Prediction", "Remedies"])

    # Tab 1: About
    with tab1:
        st.write(
            """
        ### Lung Cancer Disease Overview

        Lung cancer is one of the most common and serious types of cancer, primarily affecting the lungs but can also spread to other parts of the body. It is categorized into two main types: non-small cell lung cancer (NSCLC) and small cell lung cancer (SCLC). Risk factors include smoking, exposure to secondhand smoke, environmental pollutants, and genetic predisposition. Symptoms often include persistent cough, chest pain, shortness of breath, unexplained weight loss, and coughing up blood. Early detection is crucial for improving the chances of successful treatment, which can significantly impact survival rates.
        """
        )
        st.markdown(
            "[Learn More](https://www.cancer.org/cancer/types/lung-cancer/about/what-is.html)"
        )

    # Tab 2: Make Prediction
    with tab2:
        # Page title
        st.title("Lung Cancer Prediction using ML")

        # Getting the input data from the user
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            AGE = st.text_input("Age of the patient")

        with col2:
            SMOKING = st.radio("Smoking", options=["NO", "YES"])

        with col3:
            YELLOW_FINGERS = st.radio("Yellow fingers", options=["NO", "YES"])

        with col4:
            ANXIETY = st.radio("Anxiety", options=["NO", "YES"])

        with col1:
            PEER_PRESSURE = st.radio("Peer Pressure", options=["NO", "YES"])

        with col2:
            CHRONIC_DISEASE = st.radio("Chronic Disease", options=["NO", "YES"])

        with col3:
            FATIGUE = st.radio("Fatigue", options=["NO", "YES"])

        with col4:
            ALLERGY = st.radio("Allergy", options=["NO", "YES"])

        with col1:
            WHEEZING = st.radio("Wheezing", options=["NO", "YES"])

        with col2:
            ALCOHOL_CONSUMING = st.radio("Alcohol Consuming", options=["NO", "YES"])

        with col3:
            COUGHING = st.radio("Coughing", options=["NO", "YES"])

        with col4:
            SHORTNESS_OF_BREATH = st.radio("Shortness of Breath", options=["NO", "YES"])

        with col1:
            SWALLOWING_DIFFICULTY = st.radio("Swallowing Difficulty", options=["NO", "YES"])

        with col2:
            CHEST_PAIN = st.radio("Chest Pain", options=["NO", "YES"])

        # Convert 'YES' to 2 and 'NO' to 1
        def convert_input(value):
            return 2 if value == "YES" else 1

        # Code for Prediction
        lung_cancer_result = ""

        # Creating a button for Prediction
        if st.button("Lung Cancer Test Result"):
            user_input = [
                AGE,
                convert_input(SMOKING),
                convert_input(YELLOW_FINGERS),
                convert_input(ANXIETY),
                convert_input(PEER_PRESSURE),
                convert_input(CHRONIC_DISEASE),
                convert_input(FATIGUE),
                convert_input(ALLERGY),
                convert_input(WHEEZING),
                convert_input(ALCOHOL_CONSUMING),
                convert_input(COUGHING),
                convert_input(SHORTNESS_OF_BREATH),
                convert_input(SWALLOWING_DIFFICULTY),
                convert_input(CHEST_PAIN)
            ]

            # Check if any field is empty
            if check_empty_fields(user_input):
                st.warning("Please fill all the fields.")
            else:
                # Convert input to float (for age) and int (for other attributes)
                try:
                    user_input[0] = float(user_input[0])  # Age needs to be a float
                except ValueError:
                    st.warning("Please enter a valid number for Age.")
                    user_input[0] = 0

                # Predict the result
                lung_cancer_prediction = lung_cancer.predict([user_input])

                if lung_cancer_prediction[0] == 1:
                    lung_cancer_result = "Hurrah! You have no Lung Cancer."
                else:
                    lung_cancer_result = "Sorry! You have Lung Cancer."

                st.success(lung_cancer_result)

    # Tab 3: Remedies
    with tab3:
        st.header("Remedies and Treatment")
        st.write(
            """
        ### Remedies and Treatment for Lung Cancer

The treatment for lung cancer typically depends on the type and stage of the disease. Common treatment options include surgery to remove tumors, chemotherapy to kill cancer cells, and radiation therapy to target and shrink tumors. Targeted therapies and immunotherapy are also becoming increasingly important in the treatment of lung cancer, especially for specific genetic mutations and advanced stages of the disease. Clinical trials may offer access to innovative therapies that are still under investigation.

In addition to medical treatments, supportive care plays a vital role in managing lung cancer. This can include palliative care to alleviate symptoms and improve quality of life. Patients are often encouraged to adopt healthy lifestyle changes, such as quitting smoking, eating a balanced diet rich in fruits and vegetables, and engaging in regular physical activity, which can help enhance overall well-being and recovery. Regular follow-up care is essential for monitoring the disease and managing any side effects of treatment.
        """
        )
        st.markdown(
            "[Learn More](https://www.nhs.uk/conditions/lung-cancer/treatment/)"
        )


def check_empty_fields(inputs):
    return any(x is None or x == '' for x in inputs)


def kidney_disease_page():
    # Function to load Lottie animations from URL
    def load_lottie_url(url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        st.error(f"Failed to load Lottie animation from {url}")
        return None

    # Left, middle, and right Lottie animation URLs
    left_animation_url = ("https://lottie.host/e873ba17-6e3d-43ae-9837-a64c547203fb/WoCYefuzii.json")
    middle_animation_url = ("https://lottie.host/013e6b24-f875-438a-aff2-89a6a3af740f/Ohp4akijMn.json")
    right_animation_url = ("https://lottie.host/e873ba17-6e3d-43ae-9837-a64c547203fb/WoCYefuzii.json") # Same as middle

    # Create a flex container using Streamlit's layout
    col1, col2, col3 = st.columns(3)  # 3 equal columns

    # Set width and height for Lottie animations
    animation_width = 150
    animation_height = 150

    # Left animation
    with col1:
        st_lottie(
            load_lottie_url(left_animation_url),
            width=animation_width,
            height=animation_height,
        )

    # Middle animation
    with col2:
        st_lottie(
            load_lottie_url(middle_animation_url),
            width=animation_width,
            height=animation_height,
        )

    # Right animation
    with col3:
        st_lottie(
            load_lottie_url(right_animation_url),
            width=animation_width,
            height=animation_height,
        )
    st.title("Chronic Kideny Disease Assessment")
    # Create Tabs
    tab1, tab2, tab3 = st.tabs(["About", "Make Prediction", "Remedies"])

    # Tab 1: About
    with tab1:
        st.write(
            """
        ### Chronic Kidney Disease (CKD)
        Chronic Kidney Disease (CKD) is a progressive condition characterized by a gradual loss of kidney function over time. The kidneys play a crucial role in filtering waste products and excess fluids from the blood, maintaining electrolyte balance, and regulating blood pressure. CKD is often caused by underlying health conditions such as diabetes, hypertension, and glomerulonephritis. As kidney function declines, waste products can accumulate in the body, leading to complications such as anemia, bone disease, and cardiovascular issues. Early stages of CKD may not present noticeable symptoms, but as the disease progresses, individuals may experience fatigue, swelling in the legs and ankles, changes in urination, and persistent high blood pressure.
            """
        )
        st.markdown(
            "[Learn More](https://www.kidney.org/kidney-topics/chronic-kidney-disease-ckd)"
        )

    # Tab 2: Make Prediction
    with tab2:
        # page title
        st.title("Chronic kidney Diseaser Prediction using ML")

        # getting the input data from the user
        col1, col2, col3, col4, col5 = st.columns(5)
        # 1
        with col1:
            ID = st.text_input("ID")

        with col2:
            Age = st.text_input("AGE")

        with col3:
            Blood_Pressure = st.text_input("Blood Pressure")

        with col4:
            Specific_Gravity = st.selectbox("Specific Gravity", ["1.005", "1.010", "1.015", "1.020", "1.025"])

        with col5:
            Albumin = st.selectbox("Albumin", ["0", "1", "2", "3", "4", "5"])

        # 2 row
        with col1:
            Sugar = st.selectbox("Sugar", ["0", "1", "2", "3", "4", "5"])

        with col2:
            Red_Blood_Cells = st.selectbox("Red Blood Cells", ["normal", "abnormal"])
            # st.write(rbc)

        with col3:
            Pus_Cell = st.selectbox("Pus Cell", ["normal", "abnormal"])

        with col4:
            Pus_Cell_Clumps = st.selectbox("Pus Cell Clumps", ["present", "notpresent"])

        with col5:
            Bacteria = st.selectbox("Bacteria", ["present", "notpresent"])

        # 3 row
        with col1:
            Blood_Glucose_Random = st.text_input("Blood Glucose Random")

        with col2:
            Blood_Urea = st.text_input("Blood Urea")

        with col3:
            Serum_Creatinine = st.text_input("Serum Creatinine")

        with col4:
            Sodium = st.text_input("Sodium")

        with col5:
            Potassium = st.text_input("Potassium")
        # 4
        with col1:
            Hemoglobin = st.text_input("Hemoglobin")

        with col2:
            Packed_Cell_Volume = st.text_input("Packed Cell Volume")

        with col3:
            White_Blood_Cell_Count = st.text_input("White Blood Cell Count")

        with col4:
            Red_Blood_Cell_Count = st.text_input("Red Blood Cell Count")

        with col5:
            Hypertension = st.selectbox("Hypertension", ["yes", "no"])
            # htn = st.radio("htn",['yes','no'])
        # 5
        with col1:
            Diabetes_Mellitus = st.selectbox("Diabetes Mellitus", ["yes", "no"])

        with col2:
            Coronary_Artery_Disease = st.selectbox("Coronary Artery Disease", ["yes", "no"])

        with col3:
            # appet = st.text_input("appet")
            Appetite = st.selectbox("Appetite", ["good", "poor"])

        with col4:
            Pedal_Edema = st.selectbox("Pedal Edema", ["yes", "no"])

        with col5:
            Anemia = st.selectbox("Anemia", ["yes", "no"])

        # code for Prediction
        kidney_disease_result = " "

        # creating a button for Prediction

        if st.button("Kidney Test Result"):

            user_input = [
                ID,Age, Blood_Pressure, Specific_Gravity, Albumin, Sugar, Red_Blood_Cells,
                Pus_Cell, Pus_Cell_Clumps, Bacteria, Blood_Glucose_Random, Blood_Urea,
                Serum_Creatinine, Sodium, Potassium, Hemoglobin, Packed_Cell_Volume,
                White_Blood_Cell_Count, Red_Blood_Cell_Count, Hypertension, Diabetes_Mellitus,
                Coronary_Artery_Disease, Appetite, Pedal_Edema, Anemia
            ]

            if check_empty_fields(user_input):
                st.warning("Please fill all the fields to make a prediction.")
            else:
                user_input_float = []
                for value in user_input:
                    try:
                        user_input_float.append(float(value))
                    except ValueError:
                        # For categorical fields
                        if value == "yes":
                            user_input_float.append(1)
                        elif value == "no":
                            user_input_float.append(0)
                        elif value == "present":
                            user_input_float.append(1)
                        elif value == "notpresent":
                            user_input_float.append(0)
                        elif value == "good":
                            user_input_float.append(1)
                        elif value == "poor":
                            user_input_float.append(0)
                        elif value == "normal":
                            user_input_float.append(0)
                        elif value == "abnormal":
                            user_input_float.append(1)
                        else:
                            user_input_float.append(float(value))

            # Predict the result
                kidney_prediction = kidney_disease_model.predict([user_input_float])

                if kidney_prediction[0] == 0:
                    kidney_disease_result = "Hurrah! You have no kidney disease."
                else:
                    kidney_disease_result = "Sorry! You have kidney disease."

                st.success(kidney_disease_result)


    # Tab 3: Remedies
    with tab3:
        st.write(
            """
        ### Remedies and Treatment for Chronic Kidney Disease

Managing Chronic Kidney Disease involves a multifaceted approach that focuses on slowing disease progression and alleviating symptoms. Key lifestyle changes include adopting a kidney-friendly diet, which typically involves reducing sodium, phosphorus, and potassium intake while ensuring adequate protein consumption. Staying hydrated and maintaining a healthy weight are also important. Regular physical activity can help manage blood pressure and improve overall health. Medication may be prescribed to control underlying conditions such as diabetes and hypertension, as well as to address symptoms like anemia or high cholesterol levels. In advanced stages of CKD, treatment options may include dialysis to artificially filter waste from the blood or kidney transplantation for those with end-stage renal disease. Regular monitoring and collaboration with healthcare providers are essential for effectively managing CKD and improving quality of life.
        """
        )
        st.markdown(
            "[Learn More](https://www.nhs.uk/conditions/kidney-disease/treatment/)"
        )


def liver_disease_page():
    # Function to load Lottie animations from URL
    def load_lottie_url(url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        st.error(f"Failed to load Lottie animation from {url}")
        return None

    # Left, middle, and right Lottie animation URLs
    left_animation_url = ("https://lottie.host/efbc8109-b2e2-4ee4-953d-cc9903662538/dhtgzVSIlf.json")
    middle_animation_url = ("https://lottie.host/18e403f1-9b95-4fad-84b2-ac6a671b8f46/BO3sgj2RXo.json")
    right_animation_url = ("https://lottie.host/efbc8109-b2e2-4ee4-953d-cc9903662538/dhtgzVSIlf.json")  # Same as middle

    # Create a flex container using Streamlit's layout
    col1, col2, col3 = st.columns(3)  # 3 equal columns

    # Set width and height for Lottie animations
    animation_width = 150
    animation_height = 150

    # Left animation
    with col1:
        st_lottie(
            load_lottie_url(left_animation_url),
            width=animation_width,
            height=animation_height,
        )

    # Middle animation
    with col2:
        st_lottie(
            load_lottie_url(middle_animation_url),
            width=animation_width,
            height=animation_height,
        )

    # Right animation
    with col3:
        st_lottie(
            load_lottie_url(right_animation_url),
            width=animation_width,
            height=animation_height,
        )
    st.title("Liver Disease Assessment")
    # Create Tabs
    tab1, tab2, tab3 = st.tabs(["About", "Make Prediction", "Remedies"])

    # Tab 1: About
    with tab1:
        st.write(
            """
    ### Liver Disease Overview

    Liver disease refers to any condition that impairs the function of the liver, a vital organ responsible for detoxifying harmful substances, producing bile for digestion, and regulating metabolism. Common liver diseases include fatty liver disease, hepatitis (inflammation of the liver), cirrhosis (scarring of the liver), and liver cancer. Symptoms may vary depending on the type of liver disease but often include fatigue, jaundice (yellowing of the skin and eyes), abdominal pain, swelling in the legs, and easy bruising. Early diagnosis and treatment are essential to prevent severe complications, including liver failure.
    """
        )
        st.markdown(
            "[Learn More](https://www.niddk.nih.gov/health-information/liver-disease)"
        )

    # Tab 2: Make Prediction
    with tab2:
        # Page title
        st.title("Liver Disease Prediction using ML")

        col1, col2, col3 = st.columns(3)

        with col1:
            Age = st.text_input("Age")

        with col2:
            Gender = st.radio("Gender", ["Male", "Female"])

        with col3:
            Total_Bilirubin = st.text_input("Total_Bilirubin")

        with col1:
            Direct_Bilirubin = st.text_input("Direct_Bilirubin")

        with col2:
            Alkaline_Phosphotase = st.text_input("Alkaline_Phosphotase")

        with col3:
            Alamine_Aminotransferase = st.text_input("Alamine_Aminotransferase")

        with col1:
            Aspartate_Aminotransferase = st.text_input("Aspartate_Aminotransferase")

        with col2:
            Total_Protiens = st.text_input("Total_Protiens")

        with col3:
            Albumin = st.text_input("Albumin")

        with col1:
            Albumin_and_Globulin_Ratio = st.text_input("Albumin_and_Globulin_Ratio")

        # Code for Prediction
        liver_diagnosis = ""

        # Creating a button for Prediction
        if st.button("Liver Disease Test Result"):

            user_input = [
                Age,
                Gender,
                Total_Bilirubin,
                Direct_Bilirubin,
                Alkaline_Phosphotase,
                Alamine_Aminotransferase,
                Aspartate_Aminotransferase,
                Total_Protiens,
                Albumin,
                Albumin_and_Globulin_Ratio,
            ]

            # Check if any field is empty
            if check_empty_fields(user_input):
                st.warning("Please fill all the fields to make a prediction.")
            else:
                # Convert numerical inputs to float
                user_input_without_gender = user_input[:1] + user_input[2:]  # Exclude 'Gender'
                user_input_float = [float(x) for x in user_input_without_gender]

                # Predict the result
                liver_prediction = liver_disease_model.predict([user_input_float])

                if liver_prediction[0] == 1:
                    liver_diagnosis = "The person is having liver disease."
                else:
                    liver_diagnosis = "The person does not have any liver disease."

                st.success(liver_diagnosis)


    # Tab 3: Remedies
    with tab3:
        st.header("Remedies and Treatment for Diabetes")
        st.write(
            """
        ### Remedies and Treatments for Liver Disease

The treatment for liver disease depends on the underlying cause and severity of the condition. Lifestyle modifications play a critical role in managing liver health. A balanced diet rich in fruits, vegetables, whole grains, and lean proteins can support liver function. Reducing alcohol intake is essential, as excessive drinking can exacerbate liver damage. Regular exercise helps maintain a healthy weight, as obesity is a significant risk factor for liver disease. 

In cases of viral hepatitis, antiviral medications may be prescribed to reduce inflammation and prevent further liver damage. For fatty liver disease, lifestyle changes, including weight loss and dietary adjustments, are often recommended. In advanced cases, such as cirrhosis or liver cancer, more intensive treatments like medications, liver transplant, or surgery may be necessary. Monitoring liver function through regular check-ups is crucial for individuals at risk, ensuring timely intervention and maintaining overall liver health.
        """
        )
        st.markdown(
            "[Learn More](https://www.niddk.nih.gov/health-information/liver-disease/cirrhosis/treatment)"
        )

# # Custom CSS for responsive images
# css = """
# <style>
#     .responsive-image {
#         width: 100%;
#         height: auto;
#         max-width: 200px;  /* Limit max width */
#     }
#     @media (max-width: 768px) {
#         .responsive-image {
#             max-width: 150px;  /* For smaller screens */
#         }
#     }
#     @media (max-width: 480px) {
#         .responsive-image {
#             max-width: 100px;  /* For very small screens */
#         }
#     }
# </style>
# """
# st.markdown(css, unsafe_allow_html=True)

# def get_base64_image(image_path):
#     """Helper function to convert image to base64 encoding"""
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode("utf-8")
    
# def disease_prediction_page():
#     st.write(""" 
#         ### Stages of Disease Development in Humans
#         1. **Exposure**: The body comes into contact with a pathogen (bacteria, virus, etc.) through various means like air, food, or direct contact.
#         2. **Infection**: The pathogen enters the body and begins to multiply, starting to affect the host's cells and systems.
#         3. **Incubation**: The pathogen grows within the body, but symptoms have not yet appeared. This stage can last from hours to days or weeks.
#         4. **Symptoms Onset**: The body starts showing signs of the disease, such as fever, cough, or fatigue, as the immune system reacts.
#         5. **Progression**: The disease may intensify, leading to more severe symptoms, depending on the immune response and treatment.
#         6. **Resolution or Chronicity**: With treatment or the body's immune response, the disease may resolve. If untreated, some diseases can become chronic or lead to complications.
#     """)
#     st.write("""
#         #### Let's Go to the different disease .................
#     """)
#     disease_topics = {
#         "Diabetes": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\dibetics.jpg",
#         "Heart": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\heart.jpg",
#         "Kidney": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\kidney.jpg",
#         "Lungs": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\lungs.jpg",
#         "Breast Cancer": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\breastcancer.jpg",
#         "Parkinson": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\parkinson.jpg",
#         "Liver": "D:\\2105208_PROGRAM\\ML Project\\Multiple Disease Prediction System\\images\\liver.jpg",
#     }

#     # Custom CSS for circular images
# # Custom CSS for circular images
#     css = """
#     <style>
#     .circle-image {
#         border-radius: 50%;
#         width: 200px;
#         height: 200px;
#         object-fit: cover;
#     }
#     </style>
#     """
#     st.markdown(css, unsafe_allow_html=True)

#     cols = st.columns(3)

#     for idx, (disease, image_path) in enumerate(disease_topics.items()):
#         with cols[idx % 3]:
#             # Display the image with the circular effect using CSS
#             st.markdown(
#                 f'<img src="data:image/jpeg;base64,{get_base64_image(image_path)}" class="circle-image" alt="{disease}">', 
#                 unsafe_allow_html=True
#             )
#             button_key = f"Go For Prediction {disease}"
#             # Display the button for prediction
#             if st.button(f"Go For Prediction {disease}", key=button_key):
#                 st.session_state.current_paged = disease  # Set the current page to the disease name
#                 #st.write(f"Button clicked: Current page set to {disease}")  # Deb # Debug message


# def navigation_buttons_disease():
#     """Display navigation buttons on the right side of the page."""
#     col1, col2 = st.columns([4, 1])  # Create two columns: left and right
#     with col1:
#         st.write("")  # Leave this column empty or add content if needed

#     with col2:
#         if st.button("Go Back to Home Page", key="go_back_button"):
#             st.session_state.current_paged = "disease_prediction_page"

# # if 'current_paged' not in st.session_state:
# #     st.session_state.current_paged = "disease_prediction_page" 

# # Disease prediction pages navigation
# if st.session_state.current_paged == "disease_prediction_page":
#     disease_prediction_page()
# elif st.session_state.current_paged == "Diabetes":
#     diabetes_page()
#     navigation_buttons_disease()
# elif st.session_state.current_paged == "Heart":
#     heart_disease_page()
#     navigation_buttons_disease()
# elif st.session_state.current_paged == "Parkinson":
#     parkinsons_page()
#     navigation_buttons_disease()
# elif st.session_state.current_paged == "Breast Cancer":
#     breast_cancer_page()
#     navigation_buttons_disease()
# elif st.session_state.current_paged == "Lungs":
#     lung_cancer_page()
#     navigation_buttons_disease()
# elif st.session_state.current_paged == "Kidney":
#     kidney_disease_page()
#     navigation_buttons_disease()
# elif st.session_state.current_paged == "Liver":
#     liver_disease_page()
#     navigation_buttons_disease()
# else:
#     st.write("Page not found.")



# # # Disclaimer
# # st.markdown(
# #     """
# #     ---
# #     **Disclaimer:**  
# #     This content is developed to demonstrate the capabilities of Machine Learning in the field of Healthcare. The text, graphics, images, and content used is general in nature and for informational purposes only and does not constitute medical advice; the content is not intended to be a substitute for professional medical advice, diagnosis, or treatment. Always consult your doctor or other qualified healthcare provider with any questions you may have regarding a medical condition.
    
# #     **Made with Streamlit**  
# #     **Built & developed by Milan Kumar Sahoo**
# # """
# # )

# # st.markdown(
# #     """
# #     <div style="text-align:center; font-size:18px;">
# #         Made with ❤️ using Streamlit by Milan Kumar Sahoo
# #     </div>
# #     """,
# #     unsafe_allow_html=True,
# # ) 
