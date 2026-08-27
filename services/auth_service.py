# Serviço de Autenticação
from dtos.EmpresaDto import EmpresaLoginDto
from datetime import timedelta
from security import criar_token
from database import ACESS_TOKEN_EXPIRE_MINUTES
from security import verificar_senha
from dtos.UsuarioDto import LoginDTO
from repositories.usuario_repository import UsuarioRepository
from repositories.empresa_repository import EmpresaRepository
from fastapi import HTTPException






def autenticar_usuario(email,senha, usuario_repo :UsuarioRepository  ):
    usuario = usuario_repo.buscar_por_email(email)
    if not usuario or not verificar_senha(senha, usuario.senha_hash):
        return False
    return usuario
       
def autenticar_empresa(email, senha, empresa_repo: EmpresaRepository):
    empresa = empresa_repo.buscar_por_email(email)
    if not empresa or not verificar_senha(senha, empresa.senha_hash):
        return False
    return empresa
    
        
class AuthService:
    def __init__(self, usuario_repo : UsuarioRepository = None, empresa_repo: EmpresaRepository = None):
        self.usuario_repo = usuario_repo
        self.empresa_repo = empresa_repo
    
    def login(self , loginDTO : LoginDTO):
        usuario = autenticar_usuario(loginDTO.email, loginDTO.senha, self.usuario_repo)
        if not usuario:
            raise HTTPException(status_code=404, detail="Usuário não encontrado ou senha incorreta")
        else:

            acesso_token = criar_token(usuario.id, tipo= "usuario")
            refresh_token = criar_token(usuario.id, tipo= "usuario" ,duracao_token =timedelta(days=7))


            return {
                "access_token" : acesso_token,
                "refresh_token" : refresh_token,
                "token_type" : "Bearer"
                    }


    def login_empresa(self , empresaLoginDto :EmpresaLoginDto ):
        empresa = autenticar_empresa(empresaLoginDto.email, empresaLoginDto.senha, self.empresa_repo)
        if not empresa:
            raise HTTPException(status_code=404, detail="Empresa não encontrada ou senha incorreta")
        else:

            acesso_token = criar_token(empresa.id, tipo= "empresa")
            refresh_token = criar_token(empresa.id, tipo= "empresa" ,duracao_token =timedelta(days=7))


            return {
                "access_token" : acesso_token,
                "refresh_token" : refresh_token,
                "token_type" : "Bearer"
                    }

           # JWT Bearer

           # headers = {"Access-Token" : "Bearer  token"}
            
