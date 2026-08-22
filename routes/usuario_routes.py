from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependecies import pegar_session
from dtos.UsuarioDto import UsuarioDto
from repositories.usuario_repository import UsuarioRepository
from services.usuario_service import UsuarioService

# Define o roteador com prefixo '/usuarios' e tag para a documentação Swagger
usuario_router = APIRouter(prefix="/usuarios", tags=["usuarios"])


@usuario_router.post("/criar")
async def criar_conta(usuarioDto: UsuarioDto, session: Session = Depends(pegar_session)):
    """
    Rota para cadastrar um novo usuário.
    Recebe os dados via DTO, obtém a sessão do banco via Depends,
    instancia o repositório e serviço, e delega a criação.
    """
    usuario_repo = UsuarioRepository(session)
    usuario_service = UsuarioService(usuario_repo)

    return usuario_service.criar_conta(usuarioDto)
