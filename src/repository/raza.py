from sqlalchemy.orm import Session
from src.entity.raza import Raza
from src.entity.mascota import Mascota
from src.config.database import SessionLocal
from sqlalchemy import func

def count_razas():

    db = SessionLocal()

    try:
        return db.query(func.count()).select_from(Raza).scalar()
    finally:
        db.close()

def count_mascota_raza():
    db=SessionLocal()
    try:
        return db.query(Raza.raza, func.count(Mascota.idEspecie)).join(Raza, Raza.codigo == Mascota.idRaza).group_by(Raza.raza).order_by(func.count(Mascota.idEspecie).asc()).all()
    finally:
        db.close()