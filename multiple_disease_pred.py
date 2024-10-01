# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 22:46:34 2024

@author: 2105208_Milan_Kumar_sahoo
"""

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="🧑‍⚕️")

# Get the working directory of the current script
working_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the models
models_dir = os.path.join(working_dir, "DatasetModel")  # Adjust the directory name if needed

# Loading the saved models
diabetes_model = pickle.load(
    open(os.path.join(models_dir, "diabetes_model.sav"), "rb")
)

heart_disease_model = pickle.load(
    open(os.path.join(models_dir, "heart_disease_model.sav"), "rb")
)

parkinsons_model = pickle.load(
    open(os.path.join(models_dir, "parkinsons_model.sav"), "rb")
)

breast_cancer = pickle.load(
    open(os.path.join(models_dir, "breast_cancer.sav"), "rb")
)

lung_cancer = pickle.load(
    open(os.path.join(models_dir, "lung_cancer_model.pkl"), "rb")
)

kidney_disease_model = pickle.load(
    open(os.path.join(models_dir, "kidney_disease.sav"), "rb")
)

liver_disease_model = pickle.load(
    open(os.path.join(models_dir, "liver.sav"), "rb")
)

# sidebar for navigation
with st.sidebar:
    selected = option_menu(
        "Multiple Disease Prediction System",
        [
            "Diabetes Prediction",
            "Heart Disease Prediction",
            "Parkinsons Prediction",
            "Breast Cancer Prediction",
            "Lung Cancer Prediction",
            "Kideny Disease Prediction",
            "Liver Disease Prediction",
        ],
        menu_icon="hospital-fill",
        icons=[
            "activity",
            "heart",
            "person",
            "gender-female",
            "lungs",
            "virus",
            "virus2",
        ],
        default_index=0,
    )

# icons name shown from https://icons.getbootstrap.com/

# Diabetes Prediction Page
if selected == "Diabetes Prediction":

    # Page title
    st.title("Diabetes Prediction using ML")

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")

    with col2:
        Glucose = st.text_input("Plasma Glucose Concentration (2 hours after an oral glucose tolerance test)")

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

    # Code for Prediction
    diab_diagnosis = ""

    # Creating a button for Prediction
    if st.button("Diabetes Test Result"):
        
        # Check if any input is empty
        if (not Pregnancies or not Glucose or not BloodPressure or not SkinThickness or 
            not Insulin or not BMI or not DiabetesPedigreeFunction or not Age):
            st.error("Please fill all the boxes before making a prediction.")
        else:
            try:
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


# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # Page title
    st.title('Heart Disease Prediction using ML')
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


# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # Page title
    st.title("Parkinson's Disease Prediction using ML")

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


# Breast Cancer Prediction Page:
if selected == "Breast Cancer Prediction":

    # Page title
    st.title("Breast Cancer Prediction using ML")

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


# Lung Cancer Prediction Page:
# Function to check if any input field is empty
def check_empty_fields(inputs):
    return any(x is None or x == '' for x in inputs)

if selected == "Lung Cancer Prediction":

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


# kideny prediction page
def check_empty_fields(inputs):
    return any(not x for x in inputs)
if selected == "Kideny Disease Prediction":

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


# LIVER DISEASE PREDICTION
def check_empty_fields(inputs):
    return any(not x for x in inputs)

if selected == "Liver Disease Prediction":

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
