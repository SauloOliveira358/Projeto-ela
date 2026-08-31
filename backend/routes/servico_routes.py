from dependecies import verificar_token_empresa
from fastapi import APIRouter, Depends
from dtos.ServicosDto import ServicosDto
from sqlalchemy.orm import Session
from models import Empresa
from dependecies import pegar_session
from repositories.servico_repository import ServicoRepository
from services.servico_service import ServicoService


servico_router = APIRouter(prefix="/servicos", tags=["servicos"])


@servico_router.post("/criar")
async def criar_servico(servicoDto: ServicosDto, session: Session = Depends(pegar_session), empresa : Empresa = Depends(verificar_token_empresa) ):
    servico_repo = ServicoRepository(session)
    servico_service = ServicoService(servico_repo)
    return servico_service.criar_servico(servicoDto,empresa.id)


@servico_router.post("/cancelar/{id_servico}")
async def cancelar_servico(id_servico : int, session: Session = Depends(pegar_session), empresa : Empresa = Depends(verificar_token_empresa)):
    servico_repo = ServicoRepository(session)
    servico_service = ServicoService(servico_repo)
    return servico_service.cancelar_servico(id_servico,empresa.id)
    
@servico_router.get("/meus-servicos")
async def listar_servicos_empresa(session: Session = Depends(pegar_session), empresa : Empresa = Depends(verificar_token_empresa)):
    servico_repo = ServicoRepository(session)
    servico_service = ServicoService(servico_repo)
    return servico_service.listar_servicos(empresa.id)


    
