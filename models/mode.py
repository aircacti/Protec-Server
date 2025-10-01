from sqlalchemy import Column, Integer, String
from database import Base

class Mode(Base):
    __tablename__ = "modes"

    id = Column(Integer, primary_key=True, index=True)
    mode = Column(String, default="normal")  # normal | lockdown | shutdown
