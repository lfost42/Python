import csv
from pprint import pprint

# Open the csv file in read mode
with open(path, mode="r", encoding="windows-1252") as csv_file:
    # Open csv_file so that each row is a dictionary
    reader = csv.reader(csv_file)
    
    # Print the first row
    row = next(reader)
    print(type(row))
    pprint(row)


""" OUTPUT: 
<class 'list'>
['Date of Sale (dd/mm/yyyy)',
 'Address',
 'Postal Code',
 'County',
 'Price (€)',
 'Description of Property']
"""