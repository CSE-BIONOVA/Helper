import os
import csv
import requests

species = input("Enter species name: ")
assembly_summary_file = f"../../Genome/{species}/assembly_summary.txt"
genome_dir = f"../../Genome/{species}/"
accession_species_file = f"{species}.csv"
accession_species = []

# Read existing accession-species pairs from file
if os.path.isfile(accession_species_file):
	with open(accession_species_file, "r") as f:
		reader = csv.reader(f)
		for row in reader:
			accession_species.append(row[1])

# Add header to file if it's empty
if os.stat(accession_species_file).st_size == 0:
	with open(accession_species_file, "w") as f:
		writer = csv.writer(f)
		writer.writerow(["accession", "species"])

# Download genome files for new species
with open(assembly_summary_file, "r") as f:
	for line in f:
		if line.startswith("#"):
			continue
		fields = line.strip().split("\t")
		species_name=fields[7]
		print(species_name)
		if species_name not in accession_species:
			accession = fields[0]
			url = fields[19]
			filename = url.split("/")[-1] + "_genomic.fna.gz"
			link = f"{url}/{filename}"
			accession_species.append(species_name)
			print(link)
			response = requests.get(link)
			with open(os.path.join(genome_dir, filename), "wb") as f:
				f.write(response.content)
			with open(accession_species_file, "a") as f:
				writer = csv.writer(f)
				writer.writerow([accession, species_name])
