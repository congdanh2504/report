from database import Base
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class Asset(Base):
    __tablename__ = 'asset'
    id = Column(UUID, primary_key=True, default=generate_uuid, index=True)

    name = Column(String(255))
    label = Column(String(255))
    type = Column(String(255))
    search_text = Column(String(255))
