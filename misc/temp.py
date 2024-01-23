import csv

# Open the virus_files.csv file all content
with open('all_reads\\virus.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

# Read the content from temp.txt and store it in an array used content
with open('all_reads\\used\\virus.csv', 'r') as file:
    content = file.readlines()
    array = list(set([line.strip() for line in content]))

# Delete rows where the first column value is in the array
rows = [row for row in rows if row[0] not in array]

# Write the updated rows back to the virus_files.csv file rest of the content
with open('all_reads\\rest\\virus.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)
