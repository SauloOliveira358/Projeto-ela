# Repositório de Categoria
from sqlalchemy.orm import Session
from models import Categoria


class CategoriaRepository:
    def __init__(self, session: Session):
        self.session = session

    # Verifica se já existe uma categoria com o mesmo nome.
    def buscar_por_nome(self, nome: str):
        return self.session.query(Categoria).filter(Categoria.nome == nome).first()

    def buscar_por_id(self, id_categoria: int):
        return self.session.query(Categoria).filter(Categoria.id == id_categoria).first()

    def listar_todas(self):
        return self.session.query(Categoria).all()

    def salvar(self, categoria: Categoria):
        self.session.add(categoria)
        self.session.commit()
        self.session.refresh(categoria)
        return categoria