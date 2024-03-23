x="virus"
csv_file="/home/mbadmin/Documents/BashScripts/Helper/all_reads/simlord/${x}_reads_new.csv"
genome_files="/home/mbadmin/Documents/BashScripts/Helper/genome_filenames/temp_${x}.csv"
min_length=15000

while IFS= read -r line; do
    echo $line
    arr=(${line//./ })
    genome_accession=${arr[0]}
    
    long=true
    while IFS= read -r genome; do 
        if [[ $genome =~ ^\> ]]; then
            header="$genome"
        else
            sequence="$genome"
            sequence_length="${#sequence}"
            
            if (( sequence_length < min_length )); then
                long=false     
            fi
        fi
    done < "$line"
    if $long; then 
            echo "15000"
            simlord --read-reference "$line" -fl 15000 -c 30 --no-sam "sim-reads-new/${genome_accession}"    
        else  
            simlord --read-reference "$line" -c 30 --no-sam "sim-reads-new/${genome_accession}" 
        fi

        no_of_lines=$(wc -l < "sim-reads-new/${genome_accession}.fastq")
        no_of_reads=$((no_of_lines / 4))
        seqkit fq2fa "sim-reads-new/${genome_accession}.fastq" -o "sim-reads-new/${genome_accession}.fasta"
        rm "sim-reads-new/${genome_accession}.fastq"
        echo "${genome_accession}.fasta,${no_of_reads},${long}" >> "$csv_file"
done < "$genome_files"
