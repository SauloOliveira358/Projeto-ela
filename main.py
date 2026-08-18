
from fastapi import FastAPI

app = FastAPI()

from routes.auth_routes import auth_router
from routes.ordem_routes import ordem_router


app.include_router(auth_router)
app.include_router(ordem_router)




# para rodar o codigo basta rodar este codigo no terminal py -m uvicorn main:app --reload