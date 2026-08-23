# Serviço de Categoria
from fastapi import HTTPException
from repositories.categoria_repository import CategoriaRepository
from dtos.CategoriaDto import CategoriaDto
from models import Categoria


class CategoriaService:

    def __init__(self, categoria_repo: CategoriaRepository):
        self.categoria_repo = categoria_repo

        
    def criar_categoria(self, CategoriaDto : CategoriaDto):
        categoria = self.categoria_repo.buscar_por_nome(CategoriaDto.nome)
        if categoria:
            raise HTTPException(status_code=400, detail="Já existe uma categoria cadastrada com este nome!")

        nova_categoria = Categoria(
            nome=CategoriaDto.nome
        )
        
        self.categoria_repo.salvar(nova_categoria)
        return {"message" : f"Categoria cadastrada com sucesso! {CategoriaDto.nome}"}
