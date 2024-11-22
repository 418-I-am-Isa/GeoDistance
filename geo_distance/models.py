from uuid import uuid4

from pydantic import BaseModel


class PositionBase(BaseModel):
    name: str
    latitude: float
    longitude: float


class Position(PositionBase):
    id: str = str(uuid4())

    class Config:
        orm_mode = True
