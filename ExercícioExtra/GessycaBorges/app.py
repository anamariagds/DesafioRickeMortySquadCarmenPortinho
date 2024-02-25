from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Role
from uuid import UUID, uuid4

app = FastAPI()

db: List[User] = [
        User(
        id= UUID("76eb3975-aac5-441d-9619-96723e73599a"),
        first_name="Ana",
        last_name= "Maria",
        email= "ana@email.com",
        role=[Role.role_1]
    ),
        User(
        id= UUID("acacd22b-8bfa-471a-97ae-ab38a297d59e"),
        first_name="José",
        last_name= "Henrique",
        email= "jose@email.com",
        role=[Role.role_2]
    ),
        User(
        id= UUID("4c03c3fb-718f-4690-ae91-a79d8ea6d32d"),
        first_name="Vanessa",
        last_name= "Lins",
        email= "vanessa@email.com",
        role=[Role.role_3]
    )
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
            return user
        return {"message": "Usuário não encontrado!"}
    
@app.post("/api/users/")
async def add_user(user: User):
    """
    Adiciona um usuário na base de dados:
    - **id**: UUID
    - **first_name**: string
    - **last_name**: string
    - **email**: string
    - **role**: Role
    """
    db.append(user)
    return {"id": user.id}

@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com o id {id} não encontrado!"
    )
        
# crie uma função assíncrona de http put requests, criando e passando a rota se necessário.
@app.put("/api/users/{id}")
async def update_user(id: UUID, newUser: User):
    """
    Alterar dados dados:
    - Não precisa informar o id no body
    - **first_name**: string
    - **last_name**: string
    - **email**: string
    - **role**: Role
    """
    for user in db:
        if user.id == id:
            user.first_name = newUser.first_name
            user.last_name = newUser.last_name
            user.email = newUser.email
            user.role = newUser.role
            return
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com o id {id} não encontrado!"
    )