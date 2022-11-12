# Import the function required
from sqlalchemy import delete

# Delete rows lacking a description value
stmt = delete(PprCleanAll).filter(PprCleanAll.description=="")

# Execute and commit
session.execute(stmt)
session.commit()