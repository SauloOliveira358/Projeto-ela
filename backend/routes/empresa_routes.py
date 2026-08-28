from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from dependecies import pegar_session
from dtos.EmpresaDto import EmpresaDto
from repositories.empresa_repository import EmpresaRepository
from services.empresa_service import EmpresaService

empresa_router = APIRouter(prefix="/empresas", tags=["empresas"])


@empresa_router.post("/criar")
async def criar_empresa(empresaDto: EmpresaDto, session: Session = Depends(pegar_session)):
    """
    Rota para cadastrar uma nova Empresa.
    Recebe os dados via DTO, obtém a sessão do banco via Depends,
    instancia o repositório e serviço, e delega a criação.
    """
    empresa_repo = EmpresaRepository(session)
    empresa_service = EmpresaService(empresa_repo)
    return empresa_service.criar_empresa(empresaDto)    
    