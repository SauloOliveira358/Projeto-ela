from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base
from datetime import datetime

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    telefone     = Column(String(20), nullable=False)
    data_criacao = Column(DateTime, default=datetime.utcnow)
    data_atualizacao = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    


    def __init__(self, nome, email, senha_hash, telefone):
        self.nome = nome
        self.email = email
        self.senha_hash = senha_hash
        self.telefone = telefone


