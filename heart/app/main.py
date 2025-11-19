from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

app = FastAPI(
    title="Heart Disease Classification",
    description="With the input vitals, classify if the patient has change of having a heart disease."
)


model_path = r'heart_xgboost_model_v1.joblib'
try:
    model = joblib.load(model_path)
    print("Machine learning model loaded successfully!")
except FileNotFoundError:
    model = None
    print("Error: Model file not found at {}.".format(model_path))


class Heart_patient_inputs(BaseModel):
    age: int # age of the patient
    sex: int  # gender of the patient                                                                               
    cp: int  # type of chest pain (1:'Typical Angina', 2:'atypical angina', 3:'non-anginal pain', 4:'asymptomatic')
    trestbps: int # resting blood pressure (in mm Hg on admission to the hospital)        
    chol: int # serum  cholesterol in mg/dl
    fbs: int # (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
    restecg: int  # resting ECG results (0: 'normal', 1 and 2: 'abnormal')
    thalach: int # maximum heart rate achieved
    exang: int # exercise induced angina (1 = yes; 0 = no)
    oldpeak: float # ST depression induced by exercise relative to rest
    slope : int # the slope of the peak exercise ST segment (1: 'upsloping', 2: 'flat', 3: 'down sloping') 
    ca: float # number of major vessels (0-3) colored by fluoroscopy
    thal: float # thalassemia (3: 'normal', 6: 'fixed defect' , 7: 'reversible defect')


@app.get("/")
async def read_root():
    return {'message': 'Heart Disease Prediction API is up and running!'} 

@app.post("/predict")
async def predict_heart(features: Heart_patient_inputs):

    if model is None:
        result = {'message': 'Model file not found!'}

    else:
        data_array = np.array([
            features.age,
            features.sex,
            features.cp,
            features.trestbps,
            features.chol,
            features.fbs,
            features.restecg,
            features.thalach,
            features.exang,
            features.oldpeak,
            features.slope,
            features.ca,
            features.thal
        ]).reshape(1,-1)

        prediction = model.predict(data_array)[0]
        
        prediction_lookup = {
            0: "No Heart Disease",
            1: "Heart Disease"
        }

        predicted_heart_disease = prediction_lookup.get(prediction, "Unknown") 

        result = {"predicted_heart_disease": predicted_heart_disease}
        
    return result