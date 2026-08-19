from fastapi import APIRouter, Depends

ordem_router = APIRouter(prefix ="/servicos", tags = ["serviços"])

@ordem_router.get("/")
async def get_ordens():
    return {"message": "Serviços encontrados com sucesso!"}


    