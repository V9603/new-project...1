from sqlalchemy import Column, Integer, String
from app.onboarding.database import engine, Base

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    school_id = Column(Integer)
    name = Column(String)
    email = Column(String)