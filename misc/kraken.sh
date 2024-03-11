while IFS= read -r line; do
    kraken2-build --add-to-library ../../../Genome/Archaea/$line  --threads 24 --db ../../customKraken/sharkDB
done < ../../Helper/genome_filenames/og_archaea.csv

while IFS= read -r line; do
    kraken2-build --add-to-library ../../../Genome/Bacteria/$line  --threads 24 --db ../../customKraken/sharkDB
done < ../../Helper/genome_filenames/og_bacteria.csv

while IFS= read -r line; do
    kraken2-build --add-to-library ../../../Genome/Fungi/$line  --threads 24 --db ../../customKraken/sharkDB
done < ../../Helper/genome_filenames/og_fungi.csv

while IFS= read -r line; do
    kraken2-build --add-to-library ../../../Genome/Protozoa/$line  --threads 24 --db ../../customKraken/sharkDB
done < ../../Helper/genome_filenames/og_protozoa.csv

while IFS= read -r line; do
    kraken2-build --add-to-library ../../../Genome/Virus/$line  --threads 24 --db ../../customKraken/sharkDB
done < ../../Helper/genome_filenames/og_virus.csv
 
kraken2-build --add-to-library ../../../Genome/Human/GCF_000001405.40_GRCh38.p14_genomic.fna  --threads 24 --db ../../customKraken/sharkDB
kraken2-build --add-to-library ../../../Genome/Shark/GCF_018977255.1_IMCB_Cmil_1.0_genomic.fna  --threads 24 --db ../../customKraken/sharkDB
kraken2-build --add-to-library ../../../Genome/plant/GCF_000001735.4_TAIR10.1_genomic.fna --threads 24 --db ../../customKraken/sharkDB
