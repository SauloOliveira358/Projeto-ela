# Serviço de Empresa
import bcrypt
from fastapi import HTTPException
from repositories.empresa_repository import EmpresaRepository
from dtos.EmpresaDto import EmpresaDto
from models import Empresa


class EmpresaService:
    def __init__(self, empresa_repo : EmpresaRepository):
        self.empresa_repo = empresa_repo

    def criar_empresa(self, empresaDto: EmpresaDto):


        empresa = self.empresa_repo.buscar_por_email(empresaDto.email)
        if empresa:
            raise HTTPException(status_code=400, detail="Já existe uma empresa cadastrada com este email!")
        
        
        senha_bytes = empresaDto.senha_hash.encode('utf-8')
        salt = bcrypt.gensalt()
        hash_bytes = bcrypt.hashpw(senha_bytes, salt)
        senha_criptografada = hash_bytes.decode('utf-8')


        nova_empresa = Empresa(
            razao_social=empresaDto.razao_social,
            cnpj_cpf=empresaDto.cnpj_cpf,
            nome_fantasia=empresaDto.nome_fantasia,
            email=empresaDto.email,
            senha_hash=senha_criptografada,
            telefone=empresaDto.telefone,
            descricao_perfil=empresaDto.descricao_perfil,
            endereco_rua=empresaDto.endereco_rua,
            endereco_numero=empresaDto.endereco_numero,
            cidade=empresaDto.cidade,
            estado=empresaDto.estado,
            cep=empresaDto.cep,
            foto_perfil_url=empresaDto.foto_perfil_url,
            latitude=empresaDto.latitude,
            longitude=empresaDto.longitude,
            bairro=empresaDto.bairro
        )

        self.empresa_repo.salvar(nova_empresa)
        return {"message":f"Empresa cadastrada com sucesso! {empresaDto.email}"}


    