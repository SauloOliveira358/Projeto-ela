from sqlalchemy import Column, BigInteger, String
from database import Base

class Categoria(Base):
    __tablename__ = "categoria"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)


    def __init__(self, nome):
        self.nome = nome
        
    
