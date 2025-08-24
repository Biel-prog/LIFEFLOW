
from fastapi import APIRouter, Depends
from typing import List

from app.models.atividade import AtividadeSchema
from app.services.atividade_service import AtividadeService
from app.repositories.atividade_repository import AtividadeRepository
from app.db.database import get_database

router = APIRouter()

def get_atividade_repository(db = Depends(get_database)):
    return AtividadeRepository(db)

def get_atividade_service(repo: AtividadeRepository = Depends(get_atividade_repository)):
    return AtividadeService(repo)

@router.post("/", response_model=AtividadeSchema, status_code=201)
async def create_activity(
    atividade: AtividadeSchema, 
    service: AtividadeService = Depends(get_atividade_service)
):
    return await service.create_activity(atividade)

@router.get("/", response_model=List[AtividadeSchema])
async def get_all_activities(
    service: AtividadeService = Depends(get_atividade_service)
):
    return await service.get_all_activities()