from fastapi import APIRouter

categoria_router = APIRouter(prefix="/categorias", tags=["categorias"])


@categoria_router.get("/")
async def get_categorias():
    return {"message": "Categorias encontradas com sucesso!"}
