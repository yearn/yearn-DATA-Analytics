from typing import Optional

from sqlmodel import JSON, Column, Field, SQLModel


class Vault(SQLModel, table=True):
    id: str = Field(primary_key=True)
    address: str = Field(index=True)
    network: int
    name: str
    info: Optional[str]


class Strategy(SQLModel, table=True):
    id: str = Field(primary_key=True)
    address: str = Field(index=True)
    network: int
    name: str
    info: Optional[str]


def create_id(address: str, network: int) -> str:
    return str(int(network)) + '_' + address.lower()


class RiskGroup(SQLModel, table=True):
    id: str = Field(primary_key=True)
    network: int
    label: str
    auditScore: float
    codeReviewScore: float
    testingScore: float
    protocolSafetyScore: float
    complexityScore: float
    teamKnowledgeScore: float
    criteria: dict = Field(default={}, sa_column=Column(JSON))
