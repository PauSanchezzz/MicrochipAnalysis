from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import Date
from src.config.database import Base

class Raza(Base):
    __tablename__ = 'Raza'
    codigo = Column(Integer, primary_key=True, autoincrement=True)
    raza = Column(String(50), nullable=False)
