from database import SessionLocal


def get_session():
    sesion = SessionLocal()
    try:
        yield sesion
    finally:
        sesion.close()
