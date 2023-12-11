coverage_list='coverage_list.csv'
abundance_list='../../BashScripts/Helper/accession/human_metagenome/temp_files/abundance.csv'

while IFS=',' read -r -a line <&3 && IFS=',' read -r -a line2 <&4
do 
    file_path=${line[0]}
    coverage=${line[1]}
    file_name=${line2[0]}

    if ($file_name == "GRCh38"); then
        continue
    fi

    simlord --read-reference $file_path --coverage $coverage --no-sam $file_name 

done 3< "$coverage_list" 4< "$abundance_list"

simlord --read-reference "../../Genome/Human/ncbi_dataset/data/GCF_000001405.40/GCF_000001405.40_GRCh38.p14_genomic.fna" --coverage 1466 --no-sam "GRCh38"
       