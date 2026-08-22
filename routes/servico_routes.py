from fastapi import APIRouter

servico_router = APIRouter(prefix="/servicos", tags=["servicos"])


@servico_router.get("/")
async def get_servicos():
    return {"message": "Serviços encontrados com sucesso!"}
