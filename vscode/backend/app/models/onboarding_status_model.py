from sqlalchemy import Column, Integer, String
from backend.app.database import Base

class OnboardingStatus(Base):
    __tablename__ = "onboarding_status"

    id = Column(Integer, primary_key=True, index=True)
    school_id = Column(Integer)
    step = Column(String)
    status = Column(String)