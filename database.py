import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")  
SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")
ALGORITHM = os.getenv("ALGORITHM")
ACESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACESS_TOKEN_EXPIRE_MINUTES"))

# Cria o motor de conexão com o Supabase
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Cria a fábrica de sessões do banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para criar os nossos Models (Entidades)
Base = declarative_base()

# Função para injetar o banco de dados nas rotas (Dependency Injection)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()