import csv

lines = []

with open('genome_filenames/og_fungi.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        lines.append(','.join(line))

for i in range(0, len(lines), 500):
    with open('genome_filenames/og_fungi_' + str(i//500) + '.csv', 'w') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(lines[i:i+500])