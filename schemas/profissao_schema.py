from typing import Optional
from pydantic import BaseModel as SCBaseModel

class ProfissaoSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    salario: int
    area_conhecimento: str

    class Config:
        orm_mode = True