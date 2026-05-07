from fastapi import FastAPI, status, Response

from src.model import FraudScorePayload
from src.handler import handle_fraud_score

app = FastAPI()

@app.get("/ready")
async def healthcheck():
    return Response(status_code=status.HTTP_200_OK)

@app.post("/fraud-score")
async def detect_fraud(payload: FraudScorePayload):
    is_approved, score = await handle_fraud_score(payload)
    content = {"approved": is_approved, "fraud_score": score}
    return Response(status_code=status.HTTP_200_OK, content=content)