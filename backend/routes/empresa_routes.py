from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from dependecies import pegar_session, verificar_token_empresa
from dtos.EmpresaDto import EmpresaDto
from repositories.empresa_repository import EmpresaRepository
from services.empresa_service import EmpresaService
from models import Empresa

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


@empresa_router.post("/upload-foto")
async def upload_foto_empresa(
    arquivo: UploadFile = File(...),
    session: Session = Depends(pegar_session),
    empresa: Empresa = Depends(verificar_token_empresa)
):
    """
    Rota para a empresa logada atualizar sua única foto de perfil / logo.
    """
    empresa_repo = EmpresaRepository(session)
    empresa_service = EmpresaService(empresa_repo)
    return empresa_service.atualizar_foto_perfil(empresa.id, arquivo)