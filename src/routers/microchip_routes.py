from fastapi import APIRouter
from src.repository.microchip import count_mascota_microchip

microchip = APIRouter()

@microchip.get('/gato_microchip')
def get_gato_microchip():
    id_especie = 1;
    return count_mascota_microchip(id_especie)

@microchip.get('/perro_microchip')
def get_perro_microchip():
    id_especie = 2;
    return count_mascota_microchip(id_especie)