from base import Base, engine
# Import the class corresponding to the clean table
from tables import PprRawAll, PprCleanAll

if __name__ == "__main__":
    Base.metadata.create_all(engine)