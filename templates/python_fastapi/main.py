# uvicorn main:app --reload para lanzar el servidor

from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# Ruta principal de la API
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Ruta con parametros
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

# Ruta con parametros predefinidos
# solo son validos estos parametros
class Elementos(str, Enum):
    fuego = "fuego"
    agua = "agua"
    tierra = "tierra"
    aire = "aire"

@app.get("/elementos/{elemento}")
async def get_model(elemento: Elementos):
    if elemento is Elementos.fuego:
        return {"model_name": elemento, "message": "El fuego quema"}

    if elemento.value == "agua":
        return {"model_name": elemento, "message": "El agua moja"}

    if elemento == Elementos.tierra:
        return {"model_name": elemento, "message": "La tierra es dura"}
    
    if elemento == Elementos.aire:
        return {"model_name": elemento, "message": "El aire es invisible"}

