# Serviço de Serviço/Atendimento
from fastapi import HTTPException
from repositories.servico_repository import ServicoRepository
from dtos.ServicosDto import ServicosDto
from models import Servico


class ServicoService:
    def __init__(self, servico_repo : ServicoRepository):
        self.servico_repo = servico_repo

    def criar_servico(self, servicoDto : ServicosDto):
        servico = self.servico_repo.buscar_por_nome_e_empresa(servicoDto.nome, servicoDto.id_empresa)
        if servico:
            raise HTTPException(status_code=400, detail="Já existe um serviço cadastrado com este nome!")

        novo_servico = Servico(
            nome=servicoDto.nome,
            descricao=servicoDto.descricao,
            preco=servicoDto.preco,
            duracao_servico=servicoDto.duracao_servico,
            id_empresa=servicoDto.id_empresa,
            id_categoria=servicoDto.id_categoria
        )   

        self.servico_repo.salvar(novo_servico)
        return {"message": f"Serviço criado com sucesso! {servicoDto.nome}"}