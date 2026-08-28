from pydantic import BaseModel

class CategoriaDto(BaseModel):
    nome: str
   

    class Config:
        from_attributes = True

        