import csv
import os

# Assign a variable for the file to load and a variable for text output.
file_to_load = os.path.join("Analysis", "election_results.csv")
print(file_to_load)
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results.
with open(file_to_load) as election_data:
    # Print the file object.
     print(election_data)

# Write text to a file
with open(file_to_save, "w") as txt_file:
    txt_file.write("Arapahoe\nDenver\nJefferson")

# Use reader to read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Print just the header row
    header = next(file_reader)
    print(header)
    # Print all rows 
    for row in file_reader:
        print(row)