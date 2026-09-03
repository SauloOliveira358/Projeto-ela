import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes.usuario_routes import usuario_router
from routes.empresa_routes import empresa_router
from routes.servico_routes import servico_router
from routes.categoria_routes import categoria_router
from routes.agendamento_routes import agendamento_router
from routes.auth_routes import auth_router

app = FastAPI(title="Projeto Ela API", version="1.0.0")

# Garante que a pasta uploads exista e monta os arquivos estáticos
UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(os.path.join(UPLOAD_DIR, "empresas"), exist_ok=True)
os.makedirs(os.path.join(UPLOAD_DIR, "categorias"), exist_ok=True)

app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

app.include_router(usuario_router)
app.include_router(empresa_router)
app.include_router(servico_router)
app.include_router(categoria_router)
app.include_router(agendamento_router)
app.include_router(auth_router)

# para rodar o codigo basta rodar este codigo no terminal py -m uvicorn main:app --reload