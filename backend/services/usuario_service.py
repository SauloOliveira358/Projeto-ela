from security import gerar_hash_senha
import bcrypt
from fastapi import HTTPException
from repositories.usuario_repository import UsuarioRepository
from dtos.UsuarioDto import UsuarioDto
from models import Usuario


class UsuarioService:
    """
    Camada de Serviço (Regras de Negócio).
    Responsabilidade: Orquestrar e aplicar toda a lógica da aplicação
    (validações, hashing de senha com bcrypt e chamadas ao repositório).
    """

    def __init__(self, usuario_repo: UsuarioRepository):
        self.usuario_repo = usuario_repo

    def criar_conta(self, usuarioDto: UsuarioDto):
        """
        Regra de criação de conta:
        1. Verifica se já existe um usuário com o mesmo e-mail.
        2. Criptografa a senha com bcrypt e salt.
        3. Instancia a entidade Usuario.
        4. Solicita a persistência ao UsuarioRepository.
        """
        # 1. Validação de negócio: e-mail duplicado
        usuario = self.usuario_repo.buscar_por_email(usuarioDto.email)
        if usuario:
            raise HTTPException(status_code=400, detail="Já existe um usuario com este email!")

        # 2. Criptografia segura da senha (hashing)
        senha_criptografada = gerar_hash_senha(usuarioDto.senha)

        # 3. Criação do objeto de banco de dados (Model)
        novo_usuario = Usuario(
            nome=usuarioDto.nome,
            email=usuarioDto.email,
            senha_hash=senha_criptografada,
            telefone=usuarioDto.telefone
        )

        # 4. Salvar no banco via Repositório
        self.usuario_repo.salvar(novo_usuario)
        return {"message": f"Usuario criado com sucesso! {usuarioDto.email}"}
