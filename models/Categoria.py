from sqlalchemy import Column, Integer, String, Text

from database import Base


class Categoria(Base):
    __tablename__ = "categoria"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)


    def __init__(self, nome):
        self.nome = nome
    
