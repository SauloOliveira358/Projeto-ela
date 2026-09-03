# Repositório de Serviço
from typing import Optional
from sqlalchemy.orm import Session
from models import Servico

class ServicoRepository:
    def __init__(self, session: Session):
        self.session = session


    def buscar_por_nome_e_empresa(self, nome: str , id_empresa: int):
        return self.session.query(Servico).filter(Servico.nome == nome, Servico.id_empresa == id_empresa).first()


    def salvar(self, servico: Servico):
        self.session.add(servico)
        self.session.commit()
        self.session.refresh(servico)
        return servico

    def buscar_por_id(self, id_servico: int):
        return self.session.query(Servico).filter(Servico.id == id_servico).first()


    def listar_por_id_empresa(self, id_empresa: int):
        return self.session.query(Servico).filter(Servico.id_empresa == id_empresa, Servico.status != "EXCLUIDO").all()

    def filtrar_servicos(
        self,
        nome: Optional[str] = None,
        id_categoria: Optional[int] = None,
        preco_min: Optional[float] = None,
        preco_max: Optional[float] = None,
        id_empresa: Optional[int] = None
    ):
        # 1. Query base: não traz excluídos
        query = self.session.query(Servico).filter(Servico.status != "EXCLUIDO")
        # 2. Adiciona filtros condicionais
        if nome:
            # ilike faz busca ignorando maiúsculas/minúsculas
            query = query.filter(Servico.nome.ilike(f"%{nome}%"))
        
        if id_categoria:
            query = query.filter(Servico.id_categoria == id_categoria)
            
        if preco_min is not None:
            query = query.filter(Servico.preco >= preco_min)
            
        if preco_max is not None:
            query = query.filter(Servico.preco <= preco_max)
        if id_empresa:
            query = query.filter(Servico.id_empresa == id_empresa)
        return query.all()
