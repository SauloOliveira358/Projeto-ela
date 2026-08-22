from database import engine
from sqlalchemy.orm import sessionmaker
def pegar_session():
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        yield session
    finally:
        session.close()

