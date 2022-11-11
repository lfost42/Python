import csv

with open(path, mode="r", encoding="windows-1252") as reader_csv_file:
    reader = csv.DictReader(reader_csv_file)
    # The new file is called "PPR-2021-Dublin-new-headers.csv"
    # and will be saved inside the "tmp" folder    
    with open("/tmp/PPR-2021-Dublin-new-headers.csv",
                    mode="w",
                    encoding="windows-1252",
                ) as writer_csv_file:
        writer = csv.DictWriter(writer_csv_file, fieldnames=new_column_names)
        # Write header as first line
        writer.writerow(new_column_names)
        for row in reader:
	        # Write all rows in file
	        writer.writerow(row)

