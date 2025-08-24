
from app.repositories.atividade_repository import AtividadeRepository
from app.models.atividade import AtividadeSchema

class AtividadeService:
    def __init__(self, repository: AtividadeRepository):
        self.repository = repository

    async def create_activity(self, atividade: AtividadeSchema):
        return await self.repository.create_activity(atividade)

    async def get_all_activities(self):
        return await self.repository.get_all_activities()