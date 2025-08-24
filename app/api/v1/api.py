
from fastapi import APIRouter
# Importar endpoint de atividades!
from app.api.v1.endpoints import atividades 


api_router = APIRouter()

api_router.include_router(atividades.router, prefix="/atividades", tags=["Atividades"])
