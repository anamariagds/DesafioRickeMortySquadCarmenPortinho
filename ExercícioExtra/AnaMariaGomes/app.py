from fastapi import FastAPI, HTTPException
from typing import List
from uuid import UUID
from models import User, Role

app = FastAPI()

db: List[User] = [
   User(
    id= UUID("07a17a42-c0d7-4d86-8214-0ffe37ba4a2a"),
    first_name='Ana',
    last_name='Maria',
    email='email@email.com',
    role = [Role.role_1]
   ),
   User(
       id= UUID("81364833-7276-4528-873e-ffa210d1d245"),
       first_name='Cynthia',
       last_name='Zanoni',
       email='email@email.com',
       role = [Role.role_2]
   ),
   User(
       id= UUID("d2f33220-b31d-44e7-accb-8c1b082d4119"),
       first_name='Camila',
       last_name='Silva',
       email='email@email.com',
       role = [Role.role_3]
   ),
]

@app.get('/')
async def root():
    return {"mensagem": "Olá, Mundo!"}

@app.get('/api/users')
async def get_users():
    return db;

@app.get('/api/users/{id}')
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "User not found"}

@app.post('/api/users')
async def add_user(user: User):
    """
    Adiciona usuário na base de dados
    - **id**: UUID
    - **first_name**: string
    - **last_name**: string
    - **email**: string
    - **role**: Role
    """
    db.append(user)
    return {'message': 'Usuario criado com sucesso!'}

@app.delete('/api/user/{id}')
async def remove_user(id: UUID):
    for user in db:
        if user.id ==id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"Usuário com o id {id} não encontrado!"
    ) 
@app.put('/api/users/{id}')
async def update_user(id: UUID, user: User):
    modify_user = user.model_dump()
    for user in db:
        if user.id == id:
            indice = db.index(user)
            db[indice]= modify_user
            return {'novo nome': {user.first_name}}
        
