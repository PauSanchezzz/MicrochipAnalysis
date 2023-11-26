from src.entity.mascota import Mascota
from src.entity.localidad import Localidad
from src.config.database import SessionLocal
from sqlalchemy import func

def count_mascota_localidad(id_especie:int):
  db=SessionLocal()
  try:
    return db.query(Localidad.codigo,Localidad.localidad,(func.count(Mascota.idEspecie))).join(Mascota, Localidad.codigo == Mascota.idLocalidad).filter(Mascota.idEspecie==id_especie).group_by(Localidad.codigo).all()
  finally:
    db.close()
