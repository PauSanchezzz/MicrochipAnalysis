from fastapi import APIRouter
from src.repository.raza import count_razas,count_mascota_raza

raza = APIRouter()

#Total de razas
@raza.get('/raza')
def get_razas():
   """  count = count_razas()
    return {"count": count} """
   return count_razas()

#Mascota por raza
@raza.get('/mascota_raza')
def get_mascota_raza():
    result=count_mascota_raza()
    formatted_result = [{"codigo": row[0], "cantidad": row[1]} for row in result]
    return formatted_result


