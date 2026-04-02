from sqlalchemy import Column, Integer, String
from app.onboarding.database import engine, Base

class Features(Base):
    __tablename__ = "features"

    id = Column(Integer, primary_key=True, index=True)
    school_id = Column(Integer)
    features = Column(String)