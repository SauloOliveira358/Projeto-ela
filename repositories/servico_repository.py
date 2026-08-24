# Repositório de Serviço
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
        return servico

    
