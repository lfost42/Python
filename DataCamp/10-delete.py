# Import the delete module
from sqlalchemy import delete

# Get all the ppr_raw_all transaction ids
raw_transaction_ids = session.query(PprRawAll.transaction_id)

# Filter all the ppr_clean_all table transactions that are not present in the ppr_raw_all table
transactions_to_delete = session.query(PprCleanAll).filter(~PprCleanAll.transaction_id.in_(raw_transaction_ids))

# Print transactions to delete
print("Transactions to delete:", transactions_to_delete.count())

# Delete the selected transactions
# (Please note: the param "synchronize_session=False" has been inserted
# to avoid inconsistent results if a session expires)
transactions_to_delete.delete(synchronize_session=False)

# Commit the session to make the changes in the database
session.commit()