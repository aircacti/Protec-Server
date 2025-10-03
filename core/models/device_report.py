from sqlalchemy import Column, String, BigInteger
from core.database import Base

class DeviceReport(Base):
    __tablename__ = "device_reports"

    device_name = Column(String, primary_key=True)
    last_seen = Column(BigInteger)
    last_ip = Column(String)
