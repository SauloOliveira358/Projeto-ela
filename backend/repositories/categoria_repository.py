# Repositório de Categoria
from sqlalchemy.orm import Session
from models import Categoria


class CategoriaRepository:
    def __init__ (self, session: Session):
        self.session = session

    #Verifica se já existe uma categoria com o mesmo nome.
    def buscar_por_nome(self,nome : str):
        return self.session.query(Categoria).filter(Categoria.nome == nome).first()


    def salvar(self, categoria: Categoria):
        self.session.add(categoria)
        self.session.commit()
        return categoria