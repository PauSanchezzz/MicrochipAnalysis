from fastapi import APIRouter
from src.repository.nombre import repeated_name

nombre = APIRouter()

@nombre.get('/nombre_comun_gato')
def get_nombre_comun_gato():
    id_especie = 1;
    result = repeated_name(id_especie)
    formatted_result = [{"name": row[0], "repeat cat": row[1]} for row in result]

    return formatted_result

@nombre.get('/nombre_comun_perro')
def get_nombre_comun_perro():
    id_especie = 2;
    result = repeated_name(id_especie)
    formatted_result = [{"name": row[0], "repeat dog": row[1]} for row in result]

    return formatted_result