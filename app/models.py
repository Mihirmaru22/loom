from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime

class Transaction(BaseModel):
    amount: float = Field(..., gt=0, description="Transaction amount")
    category: str
    type: Literal["income", "expense"]
    description: Optional[str] = None
    date: datetime = Field(default_factory=datetime.utcnow)