import sqlite3

from geo_distance.models import Position


def create_connection():
    connection = sqlite3.connect("positions.db")
    return connection


def create_position(position: Position):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        """INSERT INTO positions (id, name, latitude, longitude)
            VALUES (?, ?, ?, ?)""",
        (position.id, position.name, position.latitude, position.longitude),
    )
    connection.commit()
    connection.close()


def get_position(position_id: str):
    connection = create_connection()
    cursor = connection.cursor()
    if position_id:
        cursor.execute(f"SELECT * FROM positions where id={position_id}")
        connection.commit()
        connection.close()


def get_positions():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM positions")


def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS positions (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    latitude TEXT NOT NULL,
    longitude TEXT NOT NULL
    )
    """
    )
    connection.commit()
    connection.close()
