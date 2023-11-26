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
import src.routers.general_routes as generalRoutes


especie.Base.metadata.create_all(bind=engine)
localidad.Base.metadata.create_all(bind=engine)
raza.Base.metadata.create_all(bind=engine)
sexo.Base.metadata.create_all(bind=engine)
mascota.Base.metadata.create_all(bind=engine)

app=FastAPI()
app.include_router(generalRoutes.router, prefix="/api")

templates = Jinja2Templates(directory="templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
