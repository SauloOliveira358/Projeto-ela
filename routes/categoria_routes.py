from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from repositories.categoria_repository import CategoriaRepository
from services.categoria_service import CategoriaService
from dependecies import pegar_session

from dtos.CategoriaDto import CategoriaDto

categoria_router = APIRouter(prefix="/categorias", tags=["categorias"])


@categoria_router.post("/criar")
async def criar_categoria(categoriaDto: CategoriaDto, session : Session = Depends(pegar_session)):
   categoria_repo = CategoriaRepository(session)
   categoria_service = CategoriaService(categoria_repo)
   return categoria_service.criar_categoria(categoriaDto)
