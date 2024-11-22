from fastapi import FastAPI, status

from geo_distance.config.database import Base, Session, engine
from geo_distance.models import Position as PositionModel
from geo_distance.schemas import Position

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def inicio():
    return "Welcome to GeoDistance App"


@app.post(
    "/positions/",
    status_code=status.HTTP_201_CREATED,
    response_model=Position,
    summary="This endpoint allows the creation of positions",
)
def post_position(position: Position):
    db = Session()
    new_position = PositionModel(**position.dict())
    db.add(new_position)
    db.commit()
    return position.dict()
