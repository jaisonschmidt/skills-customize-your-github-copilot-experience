from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    nome: str
    preco: float
    id: int = None

itens: List[Item] = []

@app.get("/")
def boas_vindas():
    return {"mensagem": "Bem-vindo à API FastAPI!"}

@app.post("/items")
def criar_item(item: Item):
    item.id = len(itens) + 1
    itens.append(item)
    return item

@app.get("/items")
def listar_itens():
    return itens
