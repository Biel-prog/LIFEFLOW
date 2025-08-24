
from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

class Database:
    client: AsyncIOMotorClient = None

db = Database()

async def get_database() -> AsyncIOMotorClient:
    return db.client[settings.MONGODB_DATABASE]

async def connect_to_mongo():
    print("Conectando ao MongoDB...")
    db.client = AsyncIOMotorClient(settings.MONGODB_URL)
    print("Conexão com o MongoDB estabelecida com sucesso!")

async def close_mongo_connection():
    print("Fechando a conexão com o MongoDB...")
    db.client.close()
    print("Conexão com o MongoDB fechada.")