from typing import Optional
from fastapi import FastAPI, Request, Header, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates  
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.config.database import SessionLocal, engine
import src.entity.especie as especie
import src.entity.localidad as localidad
import src.entity.raza as raza
import src.entity.sexo as sexo
import src.entity.mascota as mascota
""" import src.file.dataFile as dataFile """
import src.routers.raza_routes as razaRoutes
import src.routers.esterilizado_routes as esterilizadoRoutes
import src.routers.microchip_routes as microchipRoutes
import src.routers.localidad_routes as localidadRoutes
import src.routers.estrato_routes as estratoRoutes
import src.routers.nombre_routes as nombreRoutes
import src.routers.fecha_micro_routes as fecha_microRoutes


especie.Base.metadata.create_all(bind=engine)
localidad.Base.metadata.create_all(bind=engine)
raza.Base.metadata.create_all(bind=engine)
sexo.Base.metadata.create_all(bind=engine)
mascota.Base.metadata.create_all(bind=engine)

app=FastAPI()
app.include_router(razaRoutes.raza)
app.include_router(esterilizadoRoutes.esterilizado)
app.include_router(microchipRoutes.microchip)
app.include_router(localidadRoutes.localidad)
app.include_router(estratoRoutes.estrato)
app.include_router(nombreRoutes.nombre)
app.include_router(fecha_microRoutes.fecha_microchip)


templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
