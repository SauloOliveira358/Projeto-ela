
from fastapi import HTTPException
from dtos import UsuarioDto
from dtos import AgendamentoDto
from models import Usuario,Empresa
from security import criar_token
from services.auth_service import AuthService
from repositories.usuario_repository import UsuarioRepository
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from dependecies import pegar_session, verificar_token_usuario,verificar_token_empresa
from dtos.UsuarioDto import LoginDTO
from dtos.EmpresaDto import EmpresaLoginDto
from repositories.empresa_repository import EmpresaRepository
from fastapi.security import OAuth2PasswordRequestForm

auth_router = APIRouter(prefix="/auth", tags=["auth"])

# Login _> email e Senha e Tokin usando JWT
@auth_router.post("/login")
async def login(loginDTO : LoginDTO , session :Session = Depends(pegar_session) ):
    usuario_repo = UsuarioRepository(session)
    login_service = AuthService(usuario_repo)
    return login_service.login(loginDTO)

@auth_router.post("/login/empresa")
async def login_empresa(empresaLoginDto: EmpresaLoginDto, session: Session = Depends(pegar_session)):
    empresa_repo = EmpresaRepository(session)
    auth_service = AuthService(empresa_repo=empresa_repo)
    return auth_service.login_empresa(empresaLoginDto)



@auth_router.get("/refresh")
async def use_refresh_token(usuario : Usuario = Depends(verificar_token_usuario)):

    acess_token = criar_token(usuario.id,tipo= "usuario")
    return {
                "access_token" : acess_token,
                "token_type" : "Bearer"
                    }

@auth_router.get("/refresh/empresa")
async def use_refresh_token_empresa(empresa : Empresa = Depends(verificar_token_empresa)):
    acess_token = criar_token(empresa.id,tipo= "empresa")
    return {
                "access_token" : acess_token,
                "token_type" : "Bearer"
                    }




@auth_router.post("/token")
async def login_docs(
    dados_formulario: OAuth2PasswordRequestForm = Depends(), 
    session: Session = Depends(pegar_session)
):
    usuario_repo = UsuarioRepository(session)
    empresa_repo = EmpresaRepository(session)


    login_service = AuthService(usuario_repo = usuario_repo,empresa_repo = empresa_repo)
    # Adaptamos username -> email e password -> senha para reaproveitar seu LoginDTO
    login_dto = LoginDTO(email=dados_formulario.username, senha=dados_formulario.password)
    login_empresaDTO = EmpresaLoginDto(email=dados_formulario.username, senha=dados_formulario.password)
    try:
        return login_service.login(login_dto)
    except HTTPException:
        return login_service.login_empresa(login_empresaDTO)

