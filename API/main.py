from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

origins = ['http://127.0.0.1:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Data = []

@app.get("/monitoramento/energia")
async def showEnergy():
    if len(Data) > 1:
        Data.pop(0)
    return Data

@app.put("/monitoramento/energia")
async def alterar(newData: Dict) -> None:
    Data.append(newData)

@app.get("/monitoramento/prevenergia")
async def showEnergy():
    if len(Data) > 1:
        Data.pop(0)
    return Data

@app.put("/monitoramento/prevenergia")
async def alterar(newData: Dict) -> None:
    Data.append(newData)

@app.get("/monitoramento/tensao")
async def showEnergy():
    if len(Data) > 1:
        Data.pop(0)
    return Data

@app.put("/monitoramento/tensao")
async def alterar(newData: Dict) -> None:
    Data.append(newData)

@app.get("/monitoramento/corrente")
async def showEnergy():
    if len(Data) > 1:
        Data.pop(0)
    return Data

@app.put("/monitoramento/corrente")
async def alterar(newData: Dict) -> None:
    Data.append(newData)

@app.get("/monitoramento/potencia")
async def showEnergy():
    if len(Data) > 1:
        Data.pop(0)
    return Data

@app.put("/monitoramento/potencia")
async def alterar(newData: Dict) -> None:
    Data.append(newData)