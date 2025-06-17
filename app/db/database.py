from sqlalchemy import create_engine
from app.db.models import metadata


DATABASE_URL = "postgresql://mattheworga:Zeus_3245@localhost/ecommerce"

engine = create_engine(DATABASE_URL)

def create_tables():
    metadata.create_all(engine)
    print("Tables created successfully!")

def get_engine():
    return engine