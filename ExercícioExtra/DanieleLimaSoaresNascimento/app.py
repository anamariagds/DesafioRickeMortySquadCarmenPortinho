from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Role
from uuid import UUID, uuid4

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("2e153724-235d-4084-99ba-52f00a082255"),
        first_name="Daniele",
        last_name="Soares",
        email="email@gmail.com",
        role=[Role.role_1]
        ),
    User(
        id=UUID("b6e04b66-1a1a-4fd0-909a-7aee1a3ef832"),
        first_name="Gustavo",
        last_name="Nascimento",
        email="email@gmail.com",
        role=[Role.role_2]
    ),
     User(
        id=UUID("f7d61325-d5eb-46ed-b5b4-8f377d822d7a"),
        first_name="Maria",
        last_name="Inez",
        email="email@gmail.com",
        role=[Role.role_3]
    ),
]

@app.get("/")
async def root():
    return {"message": "Olá, WoMakers!"}

@app.get("/api/users")
async def get_users():
    return db    

@app.get("/api/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return User
    return {"message": "Usuário não encontrado!"}

@app.post("/api/users")
async def add_users(user: User): 
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

@app.post("/api/users")
async def add_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.put("/api/users/{id}")
async def update_user(id: UUID, updated_user: User):
    for i, user in enumerate(db):
        if user.id == id:
            db[i] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="Usuário não encontrado!")

@app.delete("/api/users/{id}")
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove (user)
            return {"message": "Usuário deletado com sucesso!"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado!")

