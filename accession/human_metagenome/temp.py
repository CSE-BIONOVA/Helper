import csv

# Open the bacteria_files.csv file all content
with open('rest_of_bacteria_after_human.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = list(reader)

# Read the content from temp.txt and store it in an array used content
with open('accession\human_metagenome\\temp.txt', 'r') as file:
    content = file.readlines()
    array = [line.strip() for line in content]

# Delete rows where the first column value is in the array
rows = [row for row in rows if row[0] not in array]

# Write the updated rows back to the bacteria_files.csv file rest of the content
with open('rest_of_bacteria.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)
