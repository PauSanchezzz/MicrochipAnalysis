from src.entity.mascota import Mascota
from src.config.database import SessionLocal
from sqlalchemy import func

def añoImp_micro():
  db=SessionLocal()
  try:
    return db.query(func.extract('year', Mascota.fechaRegMicropchip).label('year'),func.count().label('Cantidad')).filter(Mascota.fechaRegMicropchip.isnot(None)).group_by('year').order_by('year').all()
  finally:
    db.close()