# -*- coding: utf-8 -*-
"""
Created on Sat Jun 21 18:52:06 2025

@author: haris
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models
diabetes_model = pickle.load(open('C:/Users/haris/Desktop/Project/Multiple Disease Prediction System/Savedmodel/diabetes_model.sav', 'rb'))

heart_model = pickle.load(open('C:/Users/haris/Desktop/Project/Multiple Disease Prediction System/Savedmodel/heart_disease_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction'],
                           icons = ['activity', 'heart'],
                           default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # Page title
    st.title("Diabetes Prediction Using ML")
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")
        
    with col2:
        Glucose = st.text_input("Glucose level")
        
    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")
    
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")
        
    with col2:
        Insulin = st.text_input("Insulin Level")
        
    with col3:
        BMI = st.text_input("BMI value")
        
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes pedigree Function Value")
        
    with col2:
        Age = st.text_input("Age of the Person")
        
    
    # code for prediction
    diab_diagonosis = ''
    
    #creating button
    if st.button('Diabetes Test Result'):
        try:
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            
            if (diab_prediction[0] == 1):
                diab_diagonosis = 'The Person is Diabetic.\n Person needs medical attention'
            else:
                diab_diagonosis = 'The Person is Not Diabetic.'
        except ValueError:
            diab_diagonosis = 'Please make sure all inputs are valid numbers.'
            
        st.success(diab_diagonosis)
        
# Heart Disease Page
if (selected == 'Heart Disease Prediction'):
    
    # Page title
    st.title("Heart Disease Prediction Using ML")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Age')
        
    with col2:
        Sex = st.text_input("Sex (0 = Female, 1 = Male)")
        
    with col3:
        Cp = st.text_input("Chest pain type (0-3)")
        
    with col1:
        Trestbps = st.text_input("Enter trestbps value")
        
    with col2:
        Cholestrol = st.text_input("Serum Cholestrol in mg/dl")
        
    with col3:
        FBS = st.text_input("Fasting Blood Sugar > 120 mg/dl")
    
    with col1:
        Restecg = st.text_input("Enter restecg value (0-2)")
        
    with col2:
        Thalach = st.text_input("Enter the thalach value")

    with col3:
        Exang = st.text_input("Enter the exang value(1 = Yes; 0 = No)")
        
    with col1:
        OldPeak = st.text_input("Enter the oldpeak value (float value)")
        
    with col2:
        Slope = st.text_input("Enter the Slope value (0-2)")
    
    with col3:
        Ca = st.text_input("Enter the ca value (0-3)")
    
    with col1:
        Thal = st.text_input("Enter the thal value(1 = Normal; 2 = Fixed defect; 3 = Reversable defect)")
        
    heart_diagonis = ''
    
    if st.button("Predict Heart Disease"):
        try:
            # Explicit type conversion
            input_data = [
                float(Age), int(Sex), int(Cp), float(Trestbps), float(Cholestrol),
                int(FBS), int(Restecg), float(Thalach), int(Exang), float(OldPeak),
                int(Slope), int(Ca), int(Thal)
            ]
            
            # Model prediction
            heart_prediction = heart_model.predict([input_data])
            
            if (heart_prediction[0] == 1):
                heart_diagonis = 'The person has Heart Disease.\nPerson needs medical attention.'
            else:
                heart_diagonis = 'The person has No Heart Disease.'
        except ValueError:
            heart_diagonis = 'Please make sure all inputs are valid numbers.'

    st.success(heart_diagonis)


