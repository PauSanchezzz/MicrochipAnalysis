from src.entity.mascota import Mascota
from src.config.database import SessionLocal
from sqlalchemy import func

def count_mascota_estrato(id_especie:int):
  db=SessionLocal()
  try:
    return db.query(Mascota.estrato,func.count(Mascota.idEspecie)).filter(Mascota.idEspecie==id_especie).group_by(Mascota.estrato).all()
  finally:
    db.close()