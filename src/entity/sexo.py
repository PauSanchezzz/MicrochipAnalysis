from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import Date
from src.config.database import Base

class Sexo(Base):
    __tablename__ = 'Sexo'
    codigo = Column(Integer, primary_key=True, autoincrement=True)
    sexo = Column(String(50), nullable=False)