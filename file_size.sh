genome_list='../../BashScripts/Helper/accession/human_metagenome/temp_files/dna_list.csv'
abundance_list='../../BashScripts/Helper/accession/human_metagenome/temp_files/abundance.csv'
# genome_list='accession/human_metagenome/temp_files/dna_list.csv'
# abundance_list='accession/human_metagenome/temp_files/abundance.csv'
coverage_list='coverage_list.csv'

full_size=0
while IFS=',' read -r -a line
do
    file_path=${line[1]}
    file_size=$(stat -c%s "$file_path")
    full_size=$((full_size+file_size))
done < "$genome_list"

echo "total file size: $full_size"

while IFS=',' read -r -a line <&3 && IFS=',' read -r -a line2 <&4
do 
    file_path=${line[1]}
    real_file_size=$(stat -c%s "$file_path")
    abundance=$((line2[1]))
    simlated_read_size=$((full_size*abundance))
    coverage=$((simlated_read_size/real_file_size))
    echo "$file_path,$coverage" >> "$coverage_list"

done 3< "$genome_list" 4< "$abundance_list"
       

