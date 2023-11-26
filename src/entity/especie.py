from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import Date
from src.config.database import Base

class Especie(Base):
    __tablename__ = 'Especie'
    codigo = Column(Integer, primary_key=True, autoincrement=True)
    especie = Column(String(50), nullable=False)
