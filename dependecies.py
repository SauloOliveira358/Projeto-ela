from dtos import UsuarioDto
from fastapi import Depends, HTTPException
from database import engine
from sqlalchemy.orm import sessionmaker, Session
from models import Usuario
from jose import jwt, JWTError
from database import SECRET_KEY, ALGORITHM
from security import oauth2_scheme

def pegar_session():
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        yield session
    finally:
        session.close()


def verificar_token(token : str = Depends(oauth2_scheme), session = Depends(pegar_session)):
    try:
        dic_info = jwt.decode(token,SECRET_KEY,ALGORITHM)
        id_usuario = int(dic_info.get("sub"))


    except JWTError:
      
        
        raise HTTPException(status_code=401, detail="Acesso Negado, Verifique a Validade do Token")
    


    usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
    
    if not usuario: 
        raise HTTPException(status_code=401, detail="Acesso Negado")
    
    return usuario

