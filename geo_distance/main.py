from fastapi import FastAPI

from geo_distance.models import Position

app = FastAPI()

positions = []


@app.get("/positions", response_model=list[Position])
async def get_positions():
    return positions


@app.post("/positions", response_model=Position)
async def post_position(position: Position):
    positions.append(position)
    return position


@app.put("/positions/{position_id}", response_model=Position)
async def update_position(position_id: str, position: Position):
    positions[position_id] = position
    return position


@app.delete("/positions/{position_id}")
async def delete_position(position_id: str):
    del positions[position_id]
    return {"message": f"Position: {position_id} deleted"}
