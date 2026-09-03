# Repositório de Empresa
from sqlalchemy.orm import Session
from models import Empresa


class EmpresaRepository:
    def __init__(self, session: Session):
        self.session = session

    """Busca uma Empresa no banco através do e-mail."""
    def buscar_por_email(self, email: str):
        return self.session.query(Empresa).filter(Empresa.email == email).first()

    def buscar_por_id(self, id_empresa: int):
        return self.session.query(Empresa).filter(Empresa.id == id_empresa).first()

    def salvar(self, empresa: Empresa):
        self.session.add(empresa)
        self.session.commit()
        self.session.refresh(empresa)
        return empresa