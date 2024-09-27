import uuid
from sqlalchemy import Column, String, Float, DateTime
from db import Base
from datetime import datetime, timezone

class Item(Base):
    __tablename__ = "items"

    id = Column("id",String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column("name", String(255), nullable=False)
    description = Column("description", String(255), nullable=True)
    price = Column("price", Float, nullable=False)

    created_at = Column(DateTime, default=datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=datetime.now(timezone.utc),onupdate=datetime.now(timezone.utc),nullable=False)

    def __repr__(self):
        return f"<Item(id={self.id}, name={self.name}, price={self.price}, created_at={self.created_at}, updated_at={self.updated_at})>"