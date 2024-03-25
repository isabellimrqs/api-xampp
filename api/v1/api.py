from fastapi import APIRouter

from api.v1.endpoints import profissao

api_router = APIRouter()
api_router.include_router(profissao.router, prefix="/profissao", tags=["profissoes"])