# Serviço de Serviço/Atendimento
import security
from fastapi import HTTPException
from repositories.servico_repository import ServicoRepository
from dtos.ServicosDto import ServicosDto
from models import Servico


class ServicoService:
    def __init__(self, servico_repo : ServicoRepository):
        self.servico_repo = servico_repo

    def criar_servico(self, servicoDto : ServicosDto, id_empresa : int):
        servico = self.servico_repo.buscar_por_nome_e_empresa(servicoDto.nome, id_empresa)
        if servico:
            raise HTTPException(status_code=400, detail="Já existe um serviço cadastrado com este nome!")

        novo_servico = Servico(
            nome=servicoDto.nome,
            descricao=servicoDto.descricao,
            preco=servicoDto.preco,
            duracao_servico=servicoDto.duracao_servico,
            id_empresa=id_empresa,
            id_categoria=servicoDto.id_categoria
        )   


        self.servico_repo.salvar(novo_servico)
        return {"message": f"Serviço criado com sucesso! {servicoDto.nome}"}

    def cancelar_servico(self, id_servico: int,id_empresa:int):
        servico = self.servico_repo.buscar_por_id(id_servico)
        if not servico:
            raise HTTPException(status_code=404, detail="Serviço não encontrado!")
        
        if not servico.id_empresa == id_empresa:
            raise HTTPException(status_code=403, detail="Não é permitido cancelar o serviço de outra empresa!")
        
        servico.status = "EXCLUIDO"
        self.servico_repo.salvar(servico)
        return {"message": f"Serviço {servico.id} cancelado com sucesso!",
                "servico": servico
        
        }

    def listar_servicos(self,id_empresa : int):
        servicos = self.servico_repo.listar_por_id_empresa(id_empresa)
        return {
            "servicos" : servicos
        }
        