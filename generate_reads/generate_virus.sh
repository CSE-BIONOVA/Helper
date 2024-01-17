referance='/home/mbadmin/Documents/BashScripts/Helper/accession/shark_metagenome/test/virus_files.csv'


while IFS=',' read -r -a line
do 
    file_name=${line[0]}
    file_path=${line[1]}
    ../../../../Simtools/NanoSim/src/simulator.py genome -rg $file_path -c ../../../../Simtools/NanoSim/pre-trained_models/metagenome_ERR3152364_Even/training -dna_type linear -o reads/$file_name  -n 9
    
done < "$referance"
