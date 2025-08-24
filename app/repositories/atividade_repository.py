
from motor.motor_asyncio import AsyncIOMotorClient
from app.models.atividade import AtividadeSchema

COLLECTION_NAME = "atividades"

class AtividadeRepository:
    def __init__(self, db: AsyncIOMotorClient):
        self.db = db

    async def create_activity(self, atividade: AtividadeSchema) -> dict:
        document = atividade.dict()
        result = await self.db[COLLECTION_NAME].insert_one(document)
        created_document = await self.db[COLLECTION_NAME].find_one({"_id": result.inserted_id})
        return created_document

    async def get_all_activities(self) -> list:
        activities = []
        cursor = self.db[COLLECTION_NAME].find()
        async for document in cursor:
            activities.append(document)
        return activities