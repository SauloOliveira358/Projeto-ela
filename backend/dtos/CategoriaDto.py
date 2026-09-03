from pydantic import BaseModel

class CategoriaDto(BaseModel):
    nome: str
    imagem_url: str | None = None

    class Config:
        from_attributes = True


class CategoriaResponseDto(BaseModel):
    id: int
    nome: str
    imagem_url: str | None = None

    class Config:
        from_attributes = True