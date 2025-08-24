
from pydantic import BaseModel, Field
from typing import Optional

class AtividadeSchema(BaseModel):
    nome: str = Field(..., max_length=50, description="Nome da atividade")
    descricao: str = Field(..., max_length=300, description="Descrição detalhada da atividade")
    status: str = Field("Pendente", description="Status da atividade (Ex: Pendente, Concluída)")

    class Config:
        json_schema_extra = {
            "example": {
                "nome": "Estudar FastAPI",
                "descricao": "Criar o projeto Lifeflow seguindo a arquitetura limpa.",
                "status": "Em Andamento"
            }
        }

class AtividadeInDB(AtividadeSchema):
    id: Optional[str] = Field(alias="_id")