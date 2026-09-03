# Serviço de Serviço/Atendimento
from fastapi import HTTPException
from repositories.servico_repository import ServicoRepository
from dtos.ServicosDto import ServicosDto
from models import Servico


class ServicoService:
    def __init__(self, servico_repo: ServicoRepository):
        self.servico_repo = servico_repo

    def criar_servico(self, servicoDto: ServicosDto, id_empresa: int):
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

        servico_salvo = self.servico_repo.salvar(novo_servico)
        return {
            "message": f"Serviço criado com sucesso! {servicoDto.nome}",
            "servico": {
                "id": servico_salvo.id,
                "nome": servico_salvo.nome,
                "descricao": servico_salvo.descricao,
                "preco": float(servico_salvo.preco) if servico_salvo.preco is not None else None,
                "duracao_servico": servico_salvo.duracao_servico,
                "status": servico_salvo.status.value if hasattr(servico_salvo.status, 'value') else str(servico_salvo.status),
                "id_empresa": servico_salvo.id_empresa,
                "id_categoria": servico_salvo.id_categoria,
                "categoria": {
                    "id": servico_salvo.categoria.id,
                    "nome": servico_salvo.categoria.nome,
                    "imagem_url": servico_salvo.categoria.imagem_url
                } if servico_salvo.categoria else None
            }
        }

    def cancelar_servico(self, id_servico: int, id_empresa: int):
        servico = self.servico_repo.buscar_por_id(id_servico)
        if not servico:
            raise HTTPException(status_code=404, detail="Serviço não encontrado!")
        
        if servico.id_empresa != id_empresa:
            raise HTTPException(status_code=403, detail="Não é permitido cancelar o serviço de outra empresa!")
        
        servico.status = "EXCLUIDO"
        self.servico_repo.salvar(servico)
        return {
            "message": f"Serviço {servico.id} cancelado com sucesso!",
            "id_servico": servico.id
        }

    def listar_servicos(self, id_empresa: int):
        servicos = self.servico_repo.listar_por_id_empresa(id_empresa)
        return {
            "servicos": [
                {
                    "id": s.id,
                    "nome": s.nome,
                    "descricao": s.descricao,
                    "preco": float(s.preco) if s.preco is not None else None,
                    "duracao_servico": s.duracao_servico,
                    "status": s.status.value if hasattr(s.status, 'value') else str(s.status),
                    "id_empresa": s.id_empresa,
                    "id_categoria": s.id_categoria,
                    "categoria": {
                        "id": s.categoria.id,
                        "nome": s.categoria.nome,
                        "imagem_url": s.categoria.imagem_url
                    } if s.categoria else None
                }
                for s in servicos
            ]
        }

        
    def listar_todos_servicos(self):
        servicos = self.servico_repo.filtrar_servicos()
        return {
            "servicos": [
                {
                    "id": s.id,
                    "nome": s.nome,
                    "descricao": s.descricao,
                    "preco": float(s.preco) if s.preco is not None else None,
                    "duracao_servico": s.duracao_servico,
                    "status": s.status.value if hasattr(s.status, 'value') else str(s.status),
                    "id_empresa": s.id_empresa,
                    "id_categoria": s.id_categoria,
                    "categoria": {
                        "id": s.categoria.id,
                        "nome": s.categoria.nome,
                        "imagem_url": s.categoria.imagem_url
                    } if s.categoria else None
                }
                for s in servicos
            ]
        }