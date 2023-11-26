from fastapi import APIRouter
from src.repository.localidad import count_mascota_localidad

localidad = APIRouter()

@localidad.get('/gato_localidad')
def get_gato_localidad():
    id_especie = 1;
    result = count_mascota_localidad(id_especie)
    formatted_result = [{"codigo": row[0], "localidad": row[1], "count cats": row[2]} for row in result]

    return formatted_result

@localidad.get('/perro_localidad')
def get_perro_localidad():
    id_especie = 2;
    result = count_mascota_localidad(id_especie)
    formatted_result = [{"codigo": row[0], "localidad": row[1], "count dogs": row[2]} for row in result]

    return formatted_result