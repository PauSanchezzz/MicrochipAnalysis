from sqlalchemy.orm import Session
from src.entity.mascota import Mascota
from src.config.database import SessionLocal
from sqlalchemy import func

def count_mascota_esterilizado(id_especie:int):

    db = SessionLocal()

    try:
        return db.query(func.count()).select_from(Mascota).filter(Mascota.idEspecie == id_especie, Mascota.esterilizacion == 'TRUE').scalar()
    finally:
        db.close()

