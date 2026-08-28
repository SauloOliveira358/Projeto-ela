from pydantic import BaseModel




class ServicosDto(BaseModel):
    nome : str
    descricao : str | None = None
    preco : float | None = None
    duracao_servico : int | None = None
    id_empresa : int
    id_categoria : int
    
    
    