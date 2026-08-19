from sqlalchemy import Column, BigInteger, String, Text, DateTime, Numeric
from database import Base
from datetime import datetime

class Empresa(Base):
    __tablename__ = "empresa"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    razao_social = Column(String(150), nullable=False)
    cnpj_cpf = Column(String(20), unique=True, nullable=False)
    nome_fantasia = Column(String(150), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    telefone = Column(String(20))
    descricao_perfil = Column(Text)
    endereco_rua = Column(String(200))
    endereco_numero = Column(String(20))
    cidade = Column(String(100))
    estado = Column(String(2))
    cep = Column(String(10))
    foto_perfil_url = Column(String(255))
    latitude = Column(Numeric(9, 6))
    longitude = Column(Numeric(9, 6))

    data_criacao = Column(DateTime, default=datetime.utcnow)
    data_atualizacao = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    bairro = Column(String(100))

    
    def __init__(self, razao_social, cnpj_cpf, nome_fantasia, email, senha_hash, telefone, descricao_perfil, endereco_rua, endereco_numero, cidade, estado, cep, foto_perfil_url, latitude, longitude, bairro):
        self.razao_social = razao_social
        self.cnpj_cpf = cnpj_cpf
        self.nome_fantasia = nome_fantasia
        self.email = email
        self.senha_hash = senha_hash
        self.telefone = telefone
        self.descricao_perfil = descricao_perfil
        self.endereco_rua = endereco_rua
        self.endereco_numero = endereco_numero
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.foto_perfil_url = foto_perfil_url
        self.latitude = latitude
        self.longitude = longitude
        self.bairro = bairro

