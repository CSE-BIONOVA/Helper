read input
csv_file="/home/mbadmin/Documents/BashScripts/Helper/all_reads/simlord/${input}_reads.csv"
genome_files="/home/mbadmin/Documents/BashScripts/Helper/genome_filenames/og_${input}.csv"
while IFS='.' read -r -a line
do
    file_name="/home/mbadmin/Documents/${input^}/${line}"
    genome_accession=${line[0]}
    simlord --read-reference "$file_name" -fl 15000 --c 1 --no-sam "sim-reads/${genome_accession}"
    no_of_lines=$(wc -l < "${genome_accession}.fastq")
    no_of_reads=$((no_of_lines / 4))
    seqkit fq2fa "${genome_accession}.fastq" -o "${genome_accession}.fasta"
    rm "${genome_accession}.fastq"
    echo "${genome_accession}.fasta,${no_of_reads}" >> "$csv_file"
    
done < "$genome_files"

