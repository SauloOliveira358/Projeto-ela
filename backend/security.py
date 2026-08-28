
from repositories.usuario_repository import UsuarioRepository
from jose import jwt
from database import ACESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from datetime import timedelta,timezone,datetime
from fastapi.security import OAuth2PasswordBearer
import bcrypt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

def gerar_hash_senha(senha: str) -> str:
    """Gera o hash da senha usando bcrypt com salt."""
    senha_bytes = senha.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_bytes = bcrypt.hashpw(senha_bytes, salt)
    return hash_bytes.decode('utf-8')




def verificar_senha(senha_plana: str, senha_hash: str) -> bool:
    """Verifica se a senha enviada corresponde ao hash gravado."""
    return bcrypt.checkpw(
        senha_plana.encode('utf-8'),
        senha_hash.encode('utf-8')
    )

def criar_token(id_usuario,tipo = "usuario",duracao_token = timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)):
    data_expiracao = datetime.now(timezone.utc) + duracao_token
    dic_info = {
        "sub" : str(id_usuario),
        "tipo" : tipo,
        "exp" : data_expiracao}

    jwt_codificado = jwt.encode(dic_info,SECRET_KEY,ALGORITHM)
    
    return jwt_codificado

