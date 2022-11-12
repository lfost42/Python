from sqlalchemy import cast
from sqlalchemy.dialects.postgresql import insert

# Select the transaction ids
clean_transaction_ids = session.query(PprCleanAll.transaction_id)

# Select the columns and cast the appropriate types if needed
transactions_to_insert = session.query(
    cast(PprRawAll.date_of_sale, Date),
    PprRawAll.address,
    PprRawAll.postal_code,
    PprRawAll.county,
    cast(PprRawAll.price, Integer),
    PprRawAll.description,
  # Filter for the new rows
).filter(~PprRawAll.transaction_id.in_(clean_transaction_ids))

# Print total number of transactions to insert
# it should be 3154 if the transactions need to be inserted
# 0, if all transactions have been inserted
print("Transactions to insert:", transactions_to_insert.count())

# Insert the rows from the previously selected transactions
columns = ["date_of_sale", "address", "postal_code",
          "county", "price","description"]
stm = insert(PprCleanAll).from_select(columns, transactions_to_insert)

# Execute and commit the statement to make changes in the database.
session.execute(stm)
session.commit()