from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session
from repositories.categoria_repository import CategoriaRepository
from services.categoria_service import CategoriaService
from dependecies import pegar_session, verificar_token_empresa
from models import Empresa
from dtos.CategoriaDto import CategoriaDto

categoria_router = APIRouter(prefix="/categorias", tags=["categorias"])


@categoria_router.get("/")
async def listar_categorias(session: Session = Depends(pegar_session)):
    """
    Retorna todas as categorias cadastradas com seus nomes e imagens.
    """
    categoria_repo = CategoriaRepository(session)
    categoria_service = CategoriaService(categoria_repo)
    return categoria_service.listar_categorias()


@categoria_router.post("/criar")
async def criar_categoria(
    categoriaDto: CategoriaDto,
    session: Session = Depends(pegar_session),
    empresa: Empresa = Depends(verificar_token_empresa)
):
    """
    Cria uma nova categoria com nome e imagem_url opcional.
    """
    categoria_repo = CategoriaRepository(session)
    categoria_service = CategoriaService(categoria_repo)
    return categoria_service.criar_categoria(categoriaDto)


@categoria_router.post("/{id_categoria}/upload-imagem")
async def upload_imagem_categoria(
    id_categoria: int,
    arquivo: UploadFile = File(...),
    session: Session = Depends(pegar_session),
    empresa: Empresa = Depends(verificar_token_empresa)
):
    """
    Realiza o upload direto de uma imagem para a categoria especificada.
    """
    categoria_repo = CategoriaRepository(session)
    categoria_service = CategoriaService(categoria_repo)
    return categoria_service.salvar_imagem_categoria(id_categoria, arquivo)

