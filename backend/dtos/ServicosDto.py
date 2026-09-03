from pydantic import BaseModel
from dtos.CategoriaDto import CategoriaResponseDto

class ServicosDto(BaseModel):
    nome: str
    descricao: str | None = None
    preco: float | None = None
    duracao_servico: int | None = None
    id_categoria: int
    status: str | None = None

    class Config:
        from_attributes = True


class ServicoResponseDto(BaseModel):
    id: int
    nome: str
    descricao: str | None = None
    preco: float
    duracao_servico: int
    status: str
    id_empresa: int
    id_categoria: int
    categoria: CategoriaResponseDto | None = None

    class Config:
        from_attributes = True