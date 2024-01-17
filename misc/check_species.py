import csv

csv_file = 'Nanosim\\assembly_summary_bacteria.csv'
species_file = 'bactria_accession.csv'

# Open the CSV file


with open(csv_file, 'r') as file:
    # Read the lines from the file
    lines = file.readlines()

# Get the 8th field into an array
column_8 = [line.split()[7] for line in lines]

# Remove duplicates from the array
column_8 = list(set(column_8))

# Print the result into the species file
with open(species_file, 'w') as file:
    file.write('\n'.join(column_8))
