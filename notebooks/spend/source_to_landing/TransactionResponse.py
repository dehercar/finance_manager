from pydantic import BaseModel
from typing import List

class ReceiptDetail(BaseModel):
    quantity: float
    description: str
    category: str
    unit_price: float
    subtotal: float

class PaymentMethod(BaseModel):
    payment_method_type: str
    payment_method_name: str
    paid_amount: float

class Transaction(BaseModel):
    transaction_date: str
    commerce: str
    receipt_detail: List[ReceiptDetail]
    receipt_payment_method: List[PaymentMethod]
    receipt_total: float
    total_payment: float

Transaction.model_rebuild() # This is required to enable recursive types

class Response(BaseModel):
    transaction: Transaction