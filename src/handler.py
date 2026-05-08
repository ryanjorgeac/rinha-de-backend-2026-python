from src.model import FraudScorePayload


def handle_fraud_score(transaction_data: FraudScorePayload) -> tuple[bool, float]:
    return True, 0.5  # Example response with a dummy fraud score