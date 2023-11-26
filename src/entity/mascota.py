from sqlalchemy import  Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.sql.sqltypes import Date
from src.config.database import Base
import src.entity.especie as especie
import src.entity.sexo as sexo
import src.entity.raza as raza
import src.entity.localidad as localidad

class Mascota(Base):
    __tablename__ = 'Mascota'
    codMicrochip = Column(Integer, primary_key=True, autoincrement=True)
    fechaRegMicropchip = Column(Date, nullable=False)
    Nombre1 = Column(String(50), nullable=False)
    Nombre2 = Column(String(50), nullable=False)
    Apellido1 = Column(String(50), nullable=False)
    Apellido2 = Column(String(50), nullable=False)
    esterilizacion = Column(Boolean, nullable=False)
    estrato = Column(Integer, nullable=False)
    idEspecie = Column(Integer, ForeignKey(especie.Especie.codigo))
    idSexo = Column(Integer, ForeignKey(sexo.Sexo.codigo))
    idRaza = Column(Integer, ForeignKey(raza.Raza.codigo))
    idLocalidad = Column(Integer, ForeignKey(localidad.Localidad.codigo))
