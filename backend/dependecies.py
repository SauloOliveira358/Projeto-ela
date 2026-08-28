from dtos import UsuarioDto
from fastapi import Depends, HTTPException
from database import engine
from sqlalchemy.orm import sessionmaker, Session
from models import Usuario, Empresa
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


def verificar_token_usuario(token : str = Depends(oauth2_scheme), session = Depends(pegar_session)):
    try:
        dic_info = jwt.decode(token,SECRET_KEY,ALGORITHM)
        tipo = dic_info.get("tipo")
        id_usuario = int(dic_info.get("sub"))

        if tipo != "usuario":
            raise HTTPException(status_code=403, detail="Acesso exclusivo para usuarios")

    except JWTError:
      
        
        raise HTTPException(status_code=401, detail="Acesso Negado, Verifique a Validade do Token")
    


    usuario = session.query(Usuario).filter(Usuario.id == id_usuario).first()
    
    if not usuario: 
        raise HTTPException(status_code=401, detail="Acesso Negado")
    
    return usuario




def verificar_token_empresa(token: str = Depends(oauth2_scheme), session: Session = Depends(pegar_session)):
    try:
        dic_info = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id_empresa = int(dic_info.get("sub"))
        tipo = dic_info.get("tipo")
        if tipo != "empresa":
            raise HTTPException(status_code=403, detail="Acesso exclusivo para empresas")
            
    except JWTError:
        raise HTTPException(status_code=401, detail="Acesso Negado, Verifique a Validade do Token")
    
    empresa = session.query(Empresa).filter(Empresa.id == id_empresa).first()
    if not empresa:
        raise HTTPException(status_code=401, detail="Empresa não encontrada")
    
    return empresa
