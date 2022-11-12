# Import the function required
from sqlalchemy.dialects.postgresql import insert
  
values = [{"date_of_sale": "2021-01-01",
           "address": "14 bow street",
           "postal_code": "dublin 7",
           "county": "dublin",
           "price": 350000,
           "description":"second-hand"}]

# Insert values in PprCleanAll
stmt = insert(PprCleanAll).values(values)

# Execute and commit
session.execute(stmt)
session.commit()