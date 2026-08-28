from fastapi import APIRouter

agendamento_router = APIRouter(prefix="/agendamentos", tags=["agendamentos"])


@agendamento_router.get("/")
async def get_agendamentos():
    return {"message": "Agendamentos encontrados com sucesso!"}
