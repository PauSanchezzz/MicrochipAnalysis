from fastapi import APIRouter
from src.repository.esterilizado import count_mascota_esterilizado

esterilizado = APIRouter()

@esterilizado.get('/gato_esterilizado')
def get_razas():
   id_especie = 1;
   return count_mascota_esterilizado(id_especie)

@esterilizado.get('/perro_esterilizado')
def get_razas():
   id_especie = 2;
   return count_mascota_esterilizado(id_especie)