referance='/home/mbadmin/Documents/BashScripts/Helper/genome_filenames/archaea.csv'


while IFS=',' read -r -a line
do 
    file_name=$(cut -c 1-15 <<< $line)
    ../../Simtools/NanoSim/src/simulator.py genome -rg $line -c ../../Simtools/NanoSim/pre-trained_models/metagenome_ERR3152364_Even/training -dna_type linear -o reads/$file_name  -n 5 
    
done < "$referance"
