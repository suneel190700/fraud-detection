"""
FastAPI server for Real-Time Fraud Detection
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
import uvicorn
import logging

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Real-Time Fraud Detection API",
    description="XGBoost-based fraud detection with SHAP explainability",
    version="1.0.0"
)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


class TransactionRequest(BaseModel):
    transaction_id: str
    amount: float
    hour_of_day: int
    day_of_week: int
    merchant_category: int
    distance_km: float
    prev_txn_gap_mins: float
    card_age_days: int
    is_international: int


@app.get("/health")
def health():
    return {"status": "healthy", "service": "fraud-detection"}


@app.post("/predict")
def predict(request: TransactionRequest):
    """Predict fraud probability for a single transaction."""
    return {"transaction_id": request.transaction_id, "status": "model not loaded - run main.py first"}


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8002, reload=True)
