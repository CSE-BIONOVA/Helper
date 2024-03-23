read input
read i
csv_file="/home/mbadmin/Documents/BashScripts/Helper/all_reads/simlord/fungi_reads_${i}.csv"
genome_files="/home/mbadmin/Documents/BashScripts/Helper/genome_filenames/temp_fungi_${i}.csv"
while read line
do
    echo $line
    arr=(${line//./ })
    genome_accession=${arr[0]}
    simlord --read-reference "$line" -fl 15000 -c 1 --no-sam "sim-reads/${genome_accession}"
    no_of_lines=$(wc -l < "sim-reads/${genome_accession}.fastq")
    no_of_reads=$((no_of_lines / 4))
    seqkit fq2fa "sim-reads/${genome_accession}.fastq" -o "sim-reads/${genome_accession}.fasta"
    rm "sim-reads/${genome_accession}.fastq"
    rm $line
    echo "${genome_accession}.fasta,${no_of_reads}" >> "$csv_file"
    
done < "$genome_files"
