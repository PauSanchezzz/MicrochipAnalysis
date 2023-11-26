import pandas as pd
from sqlalchemy.orm import Session
from src.config.database import Base,engine

def Datos(data, file):
  if(data=='Especie'):
    df=pd.read_excel(file,'Especie')
    df.to_sql(name='Especie',con=engine,if_exists='append',index=False)
  elif(data=='Sexo'):
    df=pd.read_excel(file,'Sexo')
    df.to_sql(name='Sexo',con=engine,if_exists='append',index=False)
  elif(data=='Raza'):
    df=pd.read_excel(file,'Raza')
    df.to_sql(name='Raza',con=engine,if_exists='append',index=False)
  elif(data=='Localidad'):
    df=pd.read_excel(file,'Localidad')
    df.to_sql(name='Localidad',con=engine,if_exists='append',index=False)
  elif(data=='Mascota'):
    df=pd.read_excel(file,'Mascota')
    df.to_sql(name='Mascota',con=engine,if_exists='append',index=False)
 
with pd.ExcelFile('reporte_microchips.xlsx') as xls:
  for sheet_name in xls.sheet_names:
    Datos(sheet_name,xls) 
    