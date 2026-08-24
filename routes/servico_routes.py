from fastapi import APIRouter, Depends
from dtos.ServicosDto import ServicosDto
from sqlalchemy.orm import Session
from dependecies import pegar_session
from repositories.servico_repository import ServicoRepository
from services.servico_service import ServicoService

servico_router = APIRouter(prefix="/servicos", tags=["servicos"])


@servico_router.post("/criar")
async def criar_servico(servicoDto: ServicosDto, session: Session = Depends(pegar_session)):
    servico_repo = ServicoRepository(session)
    servico_service = ServicoService(servico_repo)
    return servico_service.criar_servico(servicoDto)
    
    
