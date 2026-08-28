from fastapi import FastAPI

from routes.usuario_routes import usuario_router
from routes.empresa_routes import empresa_router
from routes.servico_routes import servico_router
from routes.categoria_routes import categoria_router
from routes.agendamento_routes import agendamento_router
from routes.auth_routes import auth_router

app = FastAPI()

app.include_router(usuario_router)
app.include_router(empresa_router)
app.include_router(servico_router)
app.include_router(categoria_router)
app.include_router(agendamento_router)
app.include_router(auth_router)

# para rodar o codigo basta rodar este codigo no terminal py -m uvicorn main:app --reload