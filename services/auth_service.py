# Serviço de Autenticação
from dtos.UsuarioDto import LoginDTO
from repositories.usuario_repository import UsuarioRepository
import bcrypt
from fastapi import HTTPException


def criar_token(id_usuario):
    token = f"fmiosdjfdsif{id_usuario}" 
    return token

class AuthService:
    def __init__(self, usuario_repo : UsuarioRepository):
        self.usuario_repo = usuario_repo
    
    def login(self , loginDTO : LoginDTO):
        usuario = self.usuario_repo.buscar_por_email(loginDTO.email)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        else:
            acesso_token = criar_token(usuario.id)

            return {
                "access_token" : acesso_token,
                    "token_type" : "Bearer"
                    }



           # JWT Bearer

           # headers = {"Access-Token" : "Bearer  token"}
            
