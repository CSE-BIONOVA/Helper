referance='/home/mbadmin/Documents/BashScripts/Helper/genome_filenames/temp_virus.csv'


while IFS=',' read -r -a line
do 
    file_name=${line[1]}
    file_path=${line[0]}
    ../../Simtools/NanoSim/src/simulator.py genome -rg $file_path -c ../../Simtools/NanoSim/pre-trained_models/metagenome_ERR3152364_Even/training -dna_type linear -o reads/$file_name  -n 3
    
done < "$referance"
