from sqlalchemy import Column, BigInteger, String
from database import Base

class Categoria(Base):
    __tablename__ = "categoria"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    imagem_url = Column(String(255), nullable=True)

    def __init__(self, nome: str, imagem_url: str | None = None):
        self.nome = nome
        self.imagem_url = imagem_url
