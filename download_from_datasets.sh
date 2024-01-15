
file="/home/mbadmin/Documents/BashScripts/Helper/all_archaea.csv"

while IFS= read -r line
do
  echo "Processing line: $line"
  datasets download genome accession $line
  unzip -o ncbi_dataset.zip 
  touch $line.fna
  mv ncbi_dataset/data/$line/*_genomic.fna $line.fna
done < "$file"
