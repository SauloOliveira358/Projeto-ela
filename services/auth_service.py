# Serviço de Autenticação
from datetime import timedelta
from security import criar_token
from database import ACESS_TOKEN_EXPIRE_MINUTES
from security import verificar_senha
from dtos.UsuarioDto import LoginDTO
from repositories.usuario_repository import UsuarioRepository

from fastapi import HTTPException






def autenticar_usuario(email,senha, usuario_repo :UsuarioRepository  ):
    usuario = usuario_repo.buscar_por_email(email)
    if not usuario or not verificar_senha(senha, usuario.senha_hash):
        return False
    return usuario
       
    
    
        
class AuthService:
    def __init__(self, usuario_repo : UsuarioRepository):
        self.usuario_repo = usuario_repo
    
    def login(self , loginDTO : LoginDTO):
        usuario = autenticar_usuario(loginDTO.email, loginDTO.senha, self.usuario_repo)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado ou senha incorreta")
        else:

            acesso_token = criar_token(usuario.id)
            refresh_token = criar_token(usuario.id, timedelta(days=7))


            return {
                "access_token" : acesso_token,
                "refresh_token" : refresh_token,
                "token_type" : "Bearer"
                    }



           # JWT Bearer

           # headers = {"Access-Token" : "Bearer  token"}
            
