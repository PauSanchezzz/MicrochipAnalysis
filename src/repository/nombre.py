from sqlalchemy.orm import Session
from src.entity.raza import Raza
from src.entity.mascota import Mascota
from src.config.database import SessionLocal
from sqlalchemy import func

def repeated_name(id_especie:int):

    db = SessionLocal()

    try:
        return  db.query(Mascota.Nombre1, func.count()).filter(Mascota.idEspecie == id_especie).group_by(Mascota.Nombre1).order_by(func.count().desc()).limit(20).all()
    finally:
        db.close()
