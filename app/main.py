from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from datetime import datetime, timedelta
import pandas as pd
import joblib
from pathlib import Path
from typing import Union

# ----------------------------
# Initialize FastAPI app
# ----------------------------
app = FastAPI(
    title="Weather Prediction API",
    description="API to predict rain in 7 days and cumulative precipitation over 3 days for Sydney.",
    version="1.0"
)


# ----------------------------
# Load models & preprocessing
# ----------------------------
# project_root = Path(__file__).resolve().parent
# models_path = project_root / "models"

# # Rain prediction model (classification)
# rain_model = joblib.load(models_path / "rain_or_not" / "best_rf_model.joblib")  # change filename if needed
# rain_preprocessor = joblib.load(models_path / "rain_or_not" / "transform_pipe.joblib")  # optional if saved

# # Precipitation prediction model (regression)
# precip_model = joblib.load(models_path / "precipitation_fall" / "best_lr_model.joblib")
# precip_preprocessor = joblib.load(models_path /"precipitation_fall" / "transform_pipe_LR.joblib")  # optional if saved

# ----------------------------
# Root endpoint
# ----------------------------
@app.get("/")
def root():
    return {
        "project": "Weather Forecasting",
        "description": "Predicts rainfall after 7 days and cumulative precipitation for 3 days in Sydney.",
        "endpoints": {
            "/health/": "GET: Health check",
            "/predict/rain/": "GET: Predicts if it will rain in 7 days",
            "/predict/precipitation/fall/": "GET: Predicts cumulative precipitation over 3 days"
        },
        "github": "https://github.com/yourusername/yourrepo"
    }

# ----------------------------
# Health check endpoint
# ----------------------------
@app.get("/health/")
def health():
    return {"status": 200, "message": "Welcome to the Weather Forecasting API!"}

# # ----------------------------
# # Rain prediction endpoint
# # ----------------------------
# @app.get("/predict/rain/")
# def predict_rain(date: str = Query(..., description="Start date in YYYY-MM-DD format")):
#     try:
#         input_date = datetime.strptime(date, "%Y-%m-%d")
#         predict_date = input_date + timedelta(days=7)

#         # Create input dataframe (modify according to required features)
#         df_input = pd.DataFrame({"time": [input_date]})
#         X_input = rain_preprocessor.transform(df_input)
        
#         prediction = rain_model.predict(X_input)[0]
#         will_rain = bool(prediction)

#         return {
#             "input_date": input_date.strftime("%Y-%m-%d"),
#             "prediction": {
#                 "date": predict_date.strftime("%Y-%m-%d"),
#                 "will_rain": will_rain
#             }
#         }
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

# # ----------------------------
# # Precipitation prediction endpoint
# # ----------------------------
# @app.get("/predict/precipitation/fall/")
# def predict_precipitation(date: str = Query(..., description="Start date in YYYY-MM-DD format")):
#     try:
#         input_date = datetime.strptime(date, "%Y-%m-%d")
#         start_date = input_date + timedelta(days=1)
#         end_date = input_date + timedelta(days=3)

#         # Create input dataframe (modify according to required features)
#         df_input = pd.DataFrame({"time": [input_date]})
#         X_input = precip_preprocessor.transform(df_input)
        
#         precipitation = float(precip_model.predict(X_input)[0])

#         return {
#             "input_date": input_date.strftime("%Y-%m-%d"),
#             "prediction": {
#                 "start_date": start_date.strftime("%Y-%m-%d"),
#                 "end_date": end_date.strftime("%Y-%m-%d"),
#                 "precipitation_fall": round(precipitation, 2)
#             }
#         }
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
