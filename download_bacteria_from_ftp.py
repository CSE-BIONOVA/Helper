import os
import csv
import requests

species = "Bacteria"
assembly_summary_file = f"../../Genome/{species}/assembly_summary.txt"
genome_dir = f"../../Genome/{species}/"
downloaded_species_file = "all_bacteria_species.csv"
downloaded_species = []
downloaded_accessions = []
		
if os.path.isfile(downloaded_species_file):
	with open(downloaded_species_file, "r") as f:
		reader = csv.reader(f)
		for row in reader:
			downloaded_accessions.append(row[0])
			downloaded_species.append(row[1])

print(len(downloaded_species))	
print(len(downloaded_accessions))

# Download genome files for new species
with open(assembly_summary_file, "r") as f:
	for line in f:
		if line.startswith("#"):
			continue
		fields = line.strip().split("\t")
		species_name=fields[7]
		if species_name not in downloaded_species:
			accession = fields[0]
			if accession not in downloaded_accessions:
				url = fields[19]
				filename = url.split("/")[-1] + "_genomic.fna.gz"
				print(url)
				link = f"{url}/{filename}"
				downloaded_species.append(species_name)
				print(link)
				response = requests.get(link)
				with open(os.path.join(genome_dir, filename), "wb") as f:
					f.write(response.content)
				with open(downloaded_species_file, "a") as f:
					writer = csv.writer(f)
					writer.writerow([accession, species_name])
