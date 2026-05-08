from fastapi import FastAPI, status, Response

from src.model import FraudScorePayload
from src.handler import handle_fraud_score

app = FastAPI()

@app.get("/ready", status_code=status.HTTP_200_OK)
async def healthcheck():
    return Response()

@app.post("/fraud-score", status_code=status.HTTP_200_OK)
async def detect_fraud(payload: FraudScorePayload):
    is_approved, score = handle_fraud_score(payload)
    return {"approved": is_approved, "fraud_score": score}
