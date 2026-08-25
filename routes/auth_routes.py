from services.auth_service import AuthService

from repositories.usuario_repository import UsuarioRepository
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from dependecies import pegar_session
from dtos.UsuarioDto import LoginDTO

auth_router = APIRouter(prefix="/auth", tags=["auth"])

# Login _> email e Senha e Tokin usando JWT
@auth_router.post("/login")
async def login(loginDTO : LoginDTO , session :Session = Depends(pegar_session) ):
    usuario_repo = UsuarioRepository(session)
    login_service = AuthService(usuario_repo)
    return login_service.login(loginDTO)