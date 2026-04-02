from sqlalchemy import Column, Integer, String
from app.onboarding.database import engine, Base

class School(Base):
    __tablename__ = "schools"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = Column(String)