

from sqlalchemy import Column, BigInteger, String, Text, Boolean, DateTime, ForeignKey, Numeric, Integer
from database import Base
from datetime import datetime


class Servico(Base):
    __tablename__ = "servico"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    descricao = Column(Text, nullable=False)
    preco = Column(Numeric(10, 2), nullable=False)
    duracao_servico = Column(Integer, nullable=False)   
    ativo = Column(Boolean, default=True)
    data_criacao = Column(DateTime, default=datetime.utcnow)
    data_atualizacao = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    id_empresa = Column(BigInteger, ForeignKey("empresa.id"), nullable=False)
    id_categoria = Column(BigInteger, ForeignKey("categoria.id"), nullable=False)
    
    def __init__(self, nome, descricao, preco,duracao_servico, id_empresa, id_categoria,ativo = True):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.duracao_servico = duracao_servico
        self.id_empresa = id_empresa
        self.id_categoria = id_categoria
        self.ativo = ativo
