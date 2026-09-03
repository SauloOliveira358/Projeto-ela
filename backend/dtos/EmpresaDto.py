from pydantic import BaseModel, Field

class EmpresaDto(BaseModel):
    """
    DTO (Data Transfer Object) para Empresa.
    Define e valida os campos esperados na requisição de cadastro.
    """
    razao_social: str
    cnpj_cpf: str
    nome_fantasia: str
    email: str
    senha_hash: str
    telefone: str | None = None
    descricao_perfil: str | None = None
    endereco_rua: str | None = None
    endereco_numero: str | None = None
    cidade: str | None = None

    estado: str | None = None     #Atenção este é apeans 2 campos ex: MG 
    
    cep: str | None = None
    foto_perfil_url: str | None = None
    latitude: float | None = None
    longitude: float | None = None
    bairro: str | None = None

    class Config:
        from_attributes = True


class EmpresaLoginDto(BaseModel):
    email : str
    senha : str

    class Config:
        from_attributes = True