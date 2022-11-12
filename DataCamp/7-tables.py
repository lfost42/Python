# Import the class you need
from sqlalchemy import Column, Integer, String, Date

from base import Base


class PprRawAll(Base):
    __tablename__ = "ppr_raw_all"

    id = Column(Integer, primary_key=True)
    date_of_sale = Column(String(55))
    address = Column(String(255))
    postal_code = Column(String(55))
    county = Column(String(55))
    price = Column(String(55))
    description = Column(String(255))

class PprCleanAll(Base):
    __tablename__ = "ppr_clean_all"

    id = Column(Integer, primary_key=True)
    # Create a new column of type Date
    date_of_sale = Column(Date)
    address = Column(String(255))
    postal_code = Column(String(55))
    county = Column(String(55))
    price = Column(Integer)
    description = Column(String(255))