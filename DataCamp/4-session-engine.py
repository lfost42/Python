# Import the function needed
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# Create the engine
engine = create_engine("postgresql+psycopg2://dcstudent:S3cretPassw0rd@localhost:5432/campdata-prod")

# Create the session
session = Session(engine)
