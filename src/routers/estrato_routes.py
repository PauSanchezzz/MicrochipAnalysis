from fastapi import APIRouter
from src.repository.estrato import count_mascota_estrato

estrato = APIRouter()

@estrato.get('/gato_estrato')
def get_gato_estrato():
    id_especie = 1;
    result = count_mascota_estrato(id_especie)
    formatted_result = [{"estrato": row[0], "count cats": row[1]} for row in result]

    return formatted_result

@estrato.get('/perro_estrato')
def get_perro_estrato():
    id_especie = 2;
    result = count_mascota_estrato(id_especie)
    formatted_result = [{"estrato": row[0], "count dogs": row[1]} for row in result]

    return formatted_result

