
file="./home/mbadmin/Documents/Genome/Virus/virus_accession.txt"
# count=0

while IFS= read -r line
do
  echo "Processing line: $line"
  datasets download virus genome accession $line
  unzip -o ncbi_dataset.zip 
  touch $line.fna
  mv ncbi_dataset/data/genomic.fna $line.fna
  # count=$((count+1))
  # if [ $count -eq 3000 ]; then
  #   break
  # fi
done < "$file"
