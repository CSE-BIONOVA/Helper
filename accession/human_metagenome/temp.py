import csv

# Open the bacteria_files.csv file
with open('accession\human_metagenome\\reads\\protozoa_reads.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

# Read the content from temp.txt and store it in an array
with open('accession\human_metagenome\\reads\\protozoa_used_reads.csv', 'r') as file:
    content = file.readlines()
    array = [line.strip() for line in content]

# Delete rows where the first column value is in the array
rows = [row for row in rows if row[0] not in array]

# Write the updated rows back to the bacteria_files.csv file
with open('accession\shark_metagenome\\reads\\protozoa_reads.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)
