from fastapi import FastAPI, HTTPException
from typing import List
from uuid import UUID
from models import User, Role

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("eeac69b0-3341-4faa-bd7d-5d16f2f28a4f"),
        first_name="Ana",
        last_name="Maria", 
        email="email@gmail.com", 
        role=[Role.role_1]
    ),
    User(
        id=UUID("54c15e94-51f9-43a3-ad9b-f24a416e4860"),
        first_name="Gabriela",
        last_name="Nunez", 
        email="email@gmail.com", 
        role=[Role.role_2]
    ),
    User(
        id=UUID("2f00505a-9d1e-4dba-a267-5ac357b71c8a"),
        first_name="Camilla",
        last_name="Silva", 
        email="email@gmail.com", 
        role=[Role.role_3]
    )
]

@app.get("/")
async def root():
    return {"message": "Olá, WoMakers!"}

@app.get("/api/users")
async def get_users():
    return db;

@app.get("/api/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "Usuário não encontrado!"}

@app.post("/api/users")
async def add_user(user: User):
    '''
    Adiciona um usuário na base de dados:
    - **id**: UUID
    - **first_name**: string
    - **last_name**: string
    - **email**: string
    - **role**: Role
    '''
    db.append(user)
    return {"id": user.id}

@app.put("/api/users/{id}")
async def update_user(id: UUID, user: User):
    for user in db:
        if user.id == id:
            db.remove(user)

@app.put("/api/users/{id}")
async def update_user(id: UUID, user: User):
    '''
    Atualiza um usuário na base de dados:
    - **id**: UUID
    - **first_name**: string
    - **last_name**: string
    - **email**: string
    - **role**: Role
    '''
    for i, u in enumerate(db):
        if u.id == id:
            u.first_name = user.first_name if user.first_name else u.first_name
            u.last_name = user.last_name if user.last_name else u.last_name
            u.email = user.email if user.email else u.email
            u.role = user.role if user.role else u.role
            return {"message": "Usuário atualizado com sucesso!"}
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com {id} não encontrado!"
    )

@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com {id} não encontrado!"
    )