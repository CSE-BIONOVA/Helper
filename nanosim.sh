referance='/home/mbadmin/Documents/BashScripts/Helper/accession/human_metagenome/no_of_reads.csv'

while IFS=',' read -r -a line
do 
    file_path=${line[1]}
    file_name=${line[0]}
    dna_type=${line[2]}
    no_of_reads=${line[3]}
    ../../Simtools/NanoSim/src/simulator.py genome -rg $file_path -c ../../Simtools/NanoSim/pre-trained_models/metagenome_ERR3152364_Even/training -dna_type $dna_type -o $file_name  -n  $no_of_reads -t 32
    
done < "$referance"
