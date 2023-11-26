from sqlalchemy import  Column, Integer, String, ForeignKey
from sqlalchemy.sql.sqltypes import Date
from src.config.database import Base


class Localidad(Base):
    __tablename__ = 'Localidad'
    codigo = Column(Integer, primary_key=True, autoincrement=True)
    localidad = Column(String(50), nullable=False)

