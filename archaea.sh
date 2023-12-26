referance='/home/mbadmin/Documents/Genome/Bacteria/shark/nanosim_bacteria.csv'


while IFS=',' read -r -a line
do 
    file_path=${line[0]}
    file_name=${line[1]}
    ../../../Simtools/NanoSim/src/simulator.py genome -rg $file_path -c ../../../Simtools/NanoSim/pre-trained_models/metagenome_ERR3152364_Even/training -dna_type linear -o reads/$file_name  -n  5
    
done < "$referance"
