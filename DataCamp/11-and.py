# Import the and function needed
from sqlalchemy import and_

# Retrieve all sales transactions for January 2021
result = session.query(PprCleanAll).filter(and_(PprCleanAll.date_of_sale >= "2021-01-01", PprCleanAll.date_of_sale <= "2021-01-31")).all()

print("First row address:", result[0].address)