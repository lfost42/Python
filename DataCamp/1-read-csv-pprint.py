import csv
from pprint import pprint

# Open the csv file in read mode
with open(path, mode="r", encoding="windows-1252") as csv_file:
    # Open csv_file so that each row is a dictionary
    reader = csv.DictReader(csv_file)
    
    # Print the first row
    row = next(reader)
    print(type(row))
    pprint(row)


""" OUTPUT: 
<class 'dict'>
{'Address': '16 BURLEIGH COURT, BURLINGTON ROAD, DUBLIN 4',
 'County': 'Dublin',
 'Date of Sale (dd/mm/yyyy)': '03/01/2021',
 'Description of Property': 'Second-Hand Dwelling house /Apartment',
 'Postal Code': 'Dublin 4',
 'Price (€)': '€450,000.00'}
"""