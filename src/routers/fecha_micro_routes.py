from fastapi import APIRouter
from src.repository.fecha_microchip import añoImp_micro

fecha_microchip = APIRouter()

@fecha_microchip.get('/fecha_microchip')
def get_fecha_microchip():
    return añoImp_micro()