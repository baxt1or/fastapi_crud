from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime


class ItemRequestSchema(BaseModel):
    name : str
    description : Optional[str] = None
    price : float


class ItemResponseSchema(BaseModel):
    id :str
    name :str
    description : Optional[str] = None
    price : float
    created_at : datetime
    updated_at : datetime

    model_config = ConfigDict(from_attributes=True)