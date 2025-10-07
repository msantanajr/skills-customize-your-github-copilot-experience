from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    nome: str
    preco: float

class ItemOut(Item):
    id: int

items: List[ItemOut] = []

@app.get("/items", response_model=List[ItemOut])
def listar_itens():
    return items

@app.post("/items", response_model=ItemOut)
def adicionar_item(item: Item):
    novo_id = len(items) + 1
    item_out = ItemOut(id=novo_id, **item.dict())
    items.append(item_out)
    return item_out

@app.put("/items/{item_id}", response_model=ItemOut)
def atualizar_item(item_id: int, item: Item):
    for i, it in enumerate(items):
        if it.id == item_id:
            items[i] = ItemOut(id=item_id, **item.dict())
            return items[i]
    raise HTTPException(status_code=404, detail="Item não encontrado")

@app.delete("/items/{item_id}")
def remover_item(item_id: int):
    for i, it in enumerate(items):
        if it.id == item_id:
            del items[i]
            return {"ok": True}
    raise HTTPException(status_code=404, detail="Item não encontrado")
