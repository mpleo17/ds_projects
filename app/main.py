from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os

# Initialize the FastAPI application
app = FastAPI(
    title="Iris Prediction API",
    description="A simple API to predict Iris species based on sepal and petal measurements."
)

model_path = r'iris_model.joblib'
try:
    model = joblib.load(model_path)
    print("Machine learning model loaded successfully!")
except FileNotFoundError:
    print(f"Error: Model file not found at {model_path}. Please ensure 'train_model.py' was run.")
    model = None # Set model to None to handle cases where it couldn't be loaded

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# define root for getting health
@app.get("/")
async def read_root():
    return {'message': 'Iris Prediction API is up and running!'} 

# Define the prediction endpoint
@app.post("/predict")
async def predict_iris(features: IrisFeatures):
    
    if not model:
        result = {"error": "Model not loaded. Please check server logs."}
        
    if model:
        
        data_array = np.array([
            features.sepal_length,
            features.sepal_width,
            features.petal_length,
            features.petal_width
        ]).reshape(1, -1)
        
        prediction = model.predict(data_array)[0]

        iris_species = {
            0: "setosa",
            1: "versicolor",
            2: "virginica"
        }
        
        predicted_species = iris_species.get(prediction, "unknown") 
        
        result = {"predicted_species": predicted_species}
        
    return result