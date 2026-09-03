from pydantic import BaseModel


class UsuarioDto(BaseModel):
    """
    DTO (Data Transfer Object) para Usuário.
    Define e valida os campos esperados na requisição de cadastro.
    """
    email: str
    senha: str
    nome: str
    telefone: str

    class Config:
        from_attributes = True

class LoginDTO(BaseModel):
    email : str
    senha : str

    class Config:
        from_attributes = True