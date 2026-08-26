from sqlalchemy.orm import Session
from models import Usuario


class UsuarioRepository:
    """
    Camada de Repositório (Acesso a Dados).
    Responsabilidade: Executar comandos e consultas SQL no banco de dados.
    Não contém lógica de negócio nem regras de validação.
    """

    def __init__(self, session: Session):
        self.session = session

    def buscar_por_email(self, email: str):
        """Busca um usuário no banco através do e-mail."""
        return self.session.query(Usuario).filter(Usuario.email == email).first()



    def salvar(self, usuario: Usuario):
        """Salva e persiste um novo usuário no banco de dados."""
        self.session.add(usuario)
        self.session.commit()
        return usuario

    
