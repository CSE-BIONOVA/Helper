import os
import csv
import requests

species = "Protozoa"
assembly_summary_file = f"../../Genome/{species}/assembly_summary.txt"
genome_dir = f"../../Genome/{species}/"
downloaded_accession_file = "downloaded_archaea.csv"
downloaded_accessions = []

# read already downloaded accessions
if os.path.isfile(downloaded_accession_file):
	with open(downloaded_accession_file, "r") as f:
		reader = csv.reader(f)
		for row in reader:
			downloaded_accessions.append(row[0])

# Download genome files for new species
with open(assembly_summary_file, "r") as f:
	for line in f:
		if line.startswith("#"):
			continue
		fields = line.strip().split("\t")
		species_name=fields[7]
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
            with open(accession_species_file, "a") as f:
                writer = csv.writer(f)
                writer.writerow([accession, species_name])
