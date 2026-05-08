from datetime import datetime
from pydantic import BaseModel, model_validator

class Transaction(BaseModel):
    amount: float
    installments: int
    requested_at: str

    @model_validator(mode='before')
    def validate_requested_at(cls, values):
        try:
            datetime.strptime(values['requested_at'], '%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            raise ValueError("requested_at must be in the format 'YYYY-MM-DDTHH:MM:SSZ'")
        return values


class Customer(BaseModel):
    avg_amount: float
    tx_count_24h: int
    known_merchants: list[str]


class Merchant(BaseModel):
    id: str
    mcc: str
    avg_amount: float


class Terminal(BaseModel):
    is_online: bool
    card_present: bool
    km_from_home: float


class LastTransaction(BaseModel):
    timestamp: str
    km_from_current: float

    @model_validator(mode='before')
    def validate_timestamp(cls, values):
        try:
            datetime.strptime(values['timestamp'], '%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            raise ValueError("timestamp must be in the format 'YYYY-MM-DDTHH:MM:SSZ'")
        return values


class FraudScorePayload(BaseModel):
    id: str
    transaction: Transaction
    customer: Customer
    merchant: Merchant
    terminal: Terminal
    last_transaction: LastTransaction | None = None