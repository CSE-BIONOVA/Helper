coverage_list='coverage_list.csv'
abundance_list='../../BashScripts/Helper/accession/human_metagenome/temp_files/abundance.csv'

while IFS=',' read -r -a line <&3 && IFS=',' read -r -a line2 <&4
do 
    file_path=${line[0]}
    coverage=${line[1]}
    file_name=${line2[0]}
    simlord --read-reference $file_path --coverage $coverage --no-sam $file_name 

done 3< "$coverage_list" 4< "$abundance_list"

