from fastapi import APIRouter

empresa_router = APIRouter(prefix="/empresas", tags=["empresas"])


@empresa_router.get("/")
async def get_empresas():
    return {"message": "Empresas encontradas com sucesso!"}
