#!/bin/bash

species="Protozoa"
assembly_summary_file="../../Genome/${species}/assembly_summary.txt"
genome_dir="../../Genome/${species}/"
downloaded_accession_file="downloaded_archaea.csv"
downloaded_accessions=()

# read already downloaded accessions
if [ -f "$downloaded_accession_file" ]; then
    while IFS= read -r row || [[ -n "$row" ]]; do
        downloaded_accessions+=("$row")
    done < "$downloaded_accession_file"
fi

# Download genome files for new species
while IFS=$'\t' read -r -a fields; do
    if [[ ${fields[0]} == "#"* ]]; then
        continue
    fi
    species_name="${fields[7]}"
    accession="${fields[0]}"
    if [[ ! " ${downloaded_accessions[@]} " =~ " ${accession} " ]]; then
        url="${fields[19]}"
        filename=$(basename "$url")"_genomic.fna.gz"
        echo "$url"
        link="${url}/${filename}"
        echo "$link"
        response=$(curl -s "$link")
        echo "$response" > "$genome_dir/$filename"
    fi
done < "$assembly_summary_file"
