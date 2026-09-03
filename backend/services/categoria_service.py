# Serviço de Categoria
from fastapi import HTTPException, UploadFile
from repositories.categoria_repository import CategoriaRepository
from dtos.CategoriaDto import CategoriaDto
from models import Categoria
from services.upload_service import salvar_imagem


class CategoriaService:

    def __init__(self, categoria_repo: CategoriaRepository):
        self.categoria_repo = categoria_repo

    def criar_categoria(self, categoriaDto: CategoriaDto):
        categoria = self.categoria_repo.buscar_por_nome(categoriaDto.nome)
        if categoria:
            raise HTTPException(status_code=400, detail="Já existe uma categoria cadastrada com este nome!")

        nova_categoria = Categoria(
            nome=categoriaDto.nome,
            imagem_url=categoriaDto.imagem_url
        )
        
        categoria_salva = self.categoria_repo.salvar(nova_categoria)
        return {
            "message": f"Categoria cadastrada com sucesso! {categoriaDto.nome}",
            "categoria": {
                "id": categoria_salva.id,
                "nome": categoria_salva.nome,
                "imagem_url": categoria_salva.imagem_url
            }
        }

    def listar_categorias(self):
        categorias = self.categoria_repo.listar_todas()
        return [
            {
                "id": cat.id,
                "nome": cat.nome,
                "imagem_url": cat.imagem_url
            }
            for cat in categorias
        ]

    def salvar_imagem_categoria(self, id_categoria: int, arquivo: UploadFile):
        categoria = self.categoria_repo.buscar_por_id(id_categoria)
        if not categoria:
            raise HTTPException(status_code=404, detail="Categoria não encontrada!")

        url_imagem = salvar_imagem(arquivo, "categorias")
        categoria.imagem_url = url_imagem
        self.categoria_repo.salvar(categoria)

        return {
            "message": "Imagem da categoria atualizada com sucesso!",
            "id_categoria": categoria.id,
            "imagem_url": categoria.imagem_url
        }

