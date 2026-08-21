from database import engine
from models import Usuario
from fastapi import APIRouter
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix="/auth", tags =["auth"])

@auth_router.get("/")
async def get_auth():
    return {"message": "Auth encontrado com sucesso!"}


@auth_router.post("/criar")
async def criar_conta(email:str, senha:str,nome:str):
    Session = sessionmaker(bind=engine)
    session = Session()
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if usuario:
        return {"message": "Já existe um usuario com este email!"}
    else:
        novo_usuario = Usuario(email, senha, nome)
        session.add(novo_usuario)
        session.commit()
        session.close()
        return {"message": "Usuario criado com sucesso!"}
 