from sqlalchemy import Column, Integer, String
from app.onboarding.database import engine, Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    school_id = Column(Integer)
    address = Column(String)
    phone = Column(String)