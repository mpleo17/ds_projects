FROM python:3.12-slim  
WORKDIR /app # set the working directory
COPY requirements.txt . 
RUN pip install pandas matplotlib seaborn numpy scipy statsmodels scikit-learn xgboost pydantic fastapi uvicorn joblib
COPY app/ .
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]