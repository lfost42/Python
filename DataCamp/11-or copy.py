# Import the operator you need
from sqlalchemy import or_

# Query the clean table to retrieve the total number of
# transactions for the Dublin or Cork counties
result = session.query(PprCleanAll) \
                .filter(or_(PprCleanAll.county == "dublin", PprCleanAll.county == "cork")) \
                .all()

print("First row address:", result[0].address)