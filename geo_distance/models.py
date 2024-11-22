from uuid import uuid4

from sqlalchemy import Column, Float, String

from geo_distance.config.database import Base


class Position(Base):
    __tablename__ = "positions"

    id = Column(String, unique=True, primary_key=True, default=str(uuid4()))

    name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
