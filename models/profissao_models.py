from core.configs import settings
from sqlalchemy import Column, Integer, String

class ProfissaoModel(settings.DBBaseModel):
    __tablename__ = 'profissoes'

    id: int = Column(Integer(), primary_key=True, autoincrement=True)
    nome: str = Column(String(50))
    salario : int = Column(Integer())
    area_conhecimento: str = Column(String(100))