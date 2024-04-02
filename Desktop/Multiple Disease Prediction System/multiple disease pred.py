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
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))


# loading the saved models

diabetes_model = pickle.load(open('C:/Users/KIIT/Desktop/Multiple Disease Prediction System/saved model/diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('C:/Users/KIIT/Desktop/Multiple Disease Prediction System/saved model/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/KIIT/Desktop/Multiple Disease Prediction System/saved model/parkinsons_model.sav','rb'))

breast_cancer = pickle.load(open("C:/Users/KIIT/Desktop/Multiple Disease Prediction System/saved model/breast_cancer.sav", 'rb'))

lung_cancer = pickle.load(open("C:/Users/KIIT/Desktop/Multiple Disease Prediction System/saved model/lung_cancer_model.pkl", "rb"))

kidney_disease_model = pickle.load(open("C:/Users/KIIT/Desktop/Multiple Disease Prediction System/saved model/kidney_disease.sav",'rb'))

liver_disease_model = pickle.load(open("C:/Users/KIIT/Desktop/Multiple Disease Prediction System/saved model/liver.sav",'rb'))




# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction',
                            "Lung Cancer Prediction",
                            'Kideny Disease Prediction',
                            'Liver Disease Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person','gender-female',"lungs","virus",'virus2'],
                           default_index=0)

#icons name shown from https://icons.getbootstrap.com/

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    
    
    
# Breast Cancer Prediction Page:


if (selected == "Breast Cancer Prediction"):

    # page title
    st.title("Breast Cancer Prediction using ML")

    # getting the input data from the user

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        id = st.text_input("id")

    with col2:
        radius_mean = st.text_input("radius_mean")

    with col3:
        texture_mean = st.text_input("texture_mean")

    with col4:
        perimeter_mean = st.text_input("perimeter_mean")

    with col5:
        area_mean = st.text_input("area_mean")

    with col1:
        smoothness_mean = st.text_input("smoothness_mean")

    with col2:
        compactness_mean = st.text_input("compactness_mean")

    with col3:
        concavity_mean = st.text_input("concavity_mean")

    with col4:
        concave_points_mean = st.text_input("concave points_mean")

    with col5:
        symmetry_mean = st.text_input("symmetry_mean")

    with col1:
        fractal_dimension_mean = st.text_input("fractal_dimension_mean")

    with col2:
        radius_se = st.text_input("radius_se")

    with col3:
        texture_se = st.text_input("texture_se")

    with col4:
        perimeter_se = st.text_input("perimeter_se")

    with col5:
        area_se = st.text_input("area_se")

    with col1:
        smoothness_se = st.text_input("smoothness_se")

    with col2:
        compactness_se = st.text_input("compactness_se")

    with col3:
        concavity_se = st.text_input("concavity_se")

    with col4:
        concave_points_se = st.text_input("concave points_se")

    with col5:
        symmetry_se = st.text_input("symmetry_se")

    with col1:
        fractal_dimension_se = st.text_input("fractal_dimension_se")

    with col2:
        radius_worst = st.text_input("radius_worst")

    with col3:
        texture_worst = st.text_input("texture_worst")

    with col4:
        perimeter_worst = st.text_input("perimeter_worst")

    with col5:
        area_worst = st.text_input("area_worst")

    with col1:
        smoothness_worst = st.text_input("smoothness_worst")

    with col2:
        compactness_worst = st.text_input("compactness_worst")

    with col3:
        concavity_worst = st.text_input("concavity_worst")

    with col4:
        concave_points_worst = st.text_input("concave points_worst")

    with col5:
        symmetry_worst = st.text_input("symmetry_worst")

    with col1:
        fractal_dimension_worst = st.text_input("fractal_dimension_worst")

    # code for Prediction
    breast_cancer_check = " "

    if st.button("Breast Cancer Test Result"):
        user_input =[id, radius_mean, texture_mean, perimeter_mean, area_mean,
                     smoothness_mean, compactness_mean, concavity_mean,
                     concave_points_mean, symmetry_mean, fractal_dimension_mean,
                     radius_se, texture_se, perimeter_se, area_se, smoothness_se,
                     compactness_se, concavity_se, concave_points_se, symmetry_se,
                     fractal_dimension_se, radius_worst, texture_worst,
                     perimeter_worst, area_worst, smoothness_worst,
                     compactness_worst, concavity_worst, concave_points_worst,
                     symmetry_worst, fractal_dimension_worst]

        user_input = [float(x) for x in user_input]
          
        breast_cancer_prediction = breast_cancer.predict([user_input])
          
        if (breast_cancer_prediction[0] == 0):

            breast_cancer_check = "Hurrah! You have Benign Breast Cancer."
        else:
            breast_cancer_check = "Sorry! You have Malignant Breast Cancer."

    st.success(breast_cancer_check)


    
    
# Lung Cancer Prediction Page:



if (selected == "Lung Cancer Prediction"):

    # page title
    st.title("Lung Cancer Prediction using ML")

    # getting the input data from the user
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        AGE = st.text_input("AGE")

    with col2:
        SMOKING = st.text_input("SMOKING")

    with col3:
        YELLOW_FINGERS = st.text_input("YELLOW_FINGERS")

    with col4:
        ANXIETY = st.text_input("ANXIETY")

    with col1:
        PEER_PRESSURE = st.text_input("PEER_PRESSURE")

    with col2:
        CHRONIC_DISEASE = st.text_input("CHRONIC DISEASE")

    with col3:
        FATIGUE = st.text_input("FATIGUE")

    with col4:
        ALLERGY = st.text_input("ALLERGY")

    with col1:
        WHEEZING = st.text_input("WHEEZING")

    with col2:
        ALCOHOL_CONSUMING = st.text_input("ALCOHOL CONSUMING")

    with col3:
        COUGHING = st.text_input("COUGHING")

    with col4:
        SHORTNESS_OF_BREATH = st.text_input("SHORTNESS OF BREATH")

    with col1:
        SWALLOWING_DIFFICULTY = st.text_input("SWALLOWING DIFFICULTY")

    with col2:
        CHEST_PAIN = st.text_input("CHEST PAIN")

    # code for Prediction
    lung_cancer_result = " "

    # creating a button for Prediction

    if st.button("Lung Cancer Test Result"):
        user_input = [AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE,
                      CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING,
                      COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]
        
        user_input = [float(x) for x in user_input]

        lung_cancer_prediction = lung_cancer.predict([user_input])
        
        if (lung_cancer_prediction[0] == 0):
            lung_cancer_result = "Hurrah! You have no Lung Cancer."
        else:
            lung_cancer_result = "Sorry! You have Lung Cancer."

    st.success(lung_cancer_result)




#kideny prediction page

if (selected == "Kideny Disease Prediction"):

    # page title
    st.title("kidney Diseaser Prediction using ML")

    # getting the input data from the user
    col1, col2, col3, col4 ,col5= st.columns(5)
#1
    with col1:
        ID = st.text_input("ID")

    with col2:
        AGE = st.text_input("AGE")

    with col3:
        Blood_Pressure = st.text_input("Blood Pressure")

    with col4:
       Urinary_specific_gravity = st.text_input("Urinary specific gravity")

    with col5:
        al = st.text_input("al")
#2
    with col1:
        su = st.text_input("su")

    with col2:
        rbc = st.text_input("Enter rbc value")
        #st.write(rbc)

    with col3:
        pc = st.text_input("pc")
        st.write(pc)

    with col4:
       pcc = st.text_input("pcc")
       st.write(pcc)

    with col5:
        ba = st.text_input("ba")
        st.write(ba)
#3
    with col1:
        bgr = st.text_input("bgr")

    with col2:
        bu = st.text_input("bu")

    with col3:
        sc = st.text_input("sc")

    with col4:
        sod = st.text_input("sod")

    with col5:
        pot = st.text_input("pot")
#4        
    with col1:
        hemo = st.text_input("hemo")

    with col2:
        pcv = st.text_input("pcv")

    with col3:
        wc = st.text_input("wc")

    with col4:
        rc = st.text_input("rc")

    with col5:
        appet = st.text_input("appet")
        #htn = st.radio("htn",['yes','no'])
#5    
    with col1:
        dm = st.radio("dm", ["Yes", "No"])

    with col2:
        cad = st.radio("cad", ["Yes", "No"])

    with col3:
        #appet = st.text_input("appet")
        htn = st.radio("htn",['yes','no'])

    with col4:
        pe = st.radio("pe", ["Yes", "No"])

    with col5:
        ane = st.radio("ane", ["Yes", "No"])
    

    # code for Prediction
    kidney_disease_result = " "

    # creating a button for Prediction

    if st.button("Kidney Test Result"):
        kidney_disease_report = [ID,AGE,Blood_Pressure,Urinary_specific_gravity,al,
                                                   su,rbc,pc,pcc,ba,
                                                   bgr,bu,sc,sod,pot,
                                                   hemo,pcv,wc,rc,htn,
                                                   dm,cad,appet,pe,ane,classification]
        kidney_disease_report = [float(x) for x in  kidney_disease_report]
        
        kidney_prediction = kidney_disease_model.predict([kidney_disease_report])


        if (kidney_prediction[0] == 0):
            kidney_disease_result = "Hurrah! You have no kindey disease."
        else:
            kidney_disease_result = "Sorry! You have kidney disease."

    st.success(kidney_disease_result)



#LIVER DISEASE PREDICTION

if selected == 'Liver Disease Prediction':

    # page title
    st.title('Liver Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input('Age')

    with col2:
        Gender = st.radio("Gender", ["Male", "Female"])

    with col3:
        Total_Bilirubin = st.text_input('Total_Bilirubin')

    with col1:
        Direct_Bilirubin = st.text_input('Direct_Bilirubin')

    with col2:
        Alkaline_Phosphotase = st.text_input('Alkaline_Phosphotase')

    with col3:
        Alamine_Aminotransferase = st.text_input('Alamine_Aminotransferase')

    with col1:
        Aspartate_Aminotransferase = st.text_input('Aspartate_Aminotransferase')

    with col2:
        Total_Protiens = st.text_input('Total_Protiens')

    with col3:
        Albumin = st.text_input('Albumin')

    with col1:
        Albumin_and_Globulin_Ratio = st.text_input('Albumin_and_Globulin_Ratio')

    # code for Prediction 
    liver_diagnosis = ' '

    # creating a button for Prediction
    if st.button('Liver Disease Test Result'):

        user_input = [Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]

        # Exclude 'Gender' from user_input
        user_input_without_gender = user_input[:1] + user_input[2:]

        # Convert numerical inputs to float
        user_input_float = [float(x) for x in user_input_without_gender]

        liver_prediction = liver_disease_model.predict([user_input_float])

        #liver_prediction = liver_disease_model.predict([user_input])

        if liver_prediction[0] == 1:
            liver_diagnosis = 'The person is having liver disease'
        else:
            liver_diagnosis = 'The person does not have any liver disease'

        st.success(liver_diagnosis)  # Correct indentation for this line
