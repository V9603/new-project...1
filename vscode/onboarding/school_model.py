from sqlalchemy import Column, Integer, String
from onboarding.database import Base

class School(Base):
    __tablename__ = "schools"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = Column(String)