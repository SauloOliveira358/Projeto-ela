
from models import Usuario

from security import criar_token
from services.auth_service import AuthService

from repositories.usuario_repository import UsuarioRepository
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from dependecies import pegar_session, verificar_token
from dtos.UsuarioDto import LoginDTO

auth_router = APIRouter(prefix="/auth", tags=["auth"])

# Login _> email e Senha e Tokin usando JWT
@auth_router.post("/login")
async def login(loginDTO : LoginDTO , session :Session = Depends(pegar_session) ):
    usuario_repo = UsuarioRepository(session)
    login_service = AuthService(usuario_repo)
    return login_service.login(loginDTO)

@auth_router.get("/refresh")
async def use_refresh_token(usuario : Usuario = Depends(verificar_token)):

    acess_token = criar_token(usuario.id)
    return {
                "access_token" : acess_token,
                "token_type" : "Bearer"
                    }


