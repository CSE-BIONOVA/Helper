
file="/home/mbadmin/Documents/BashScripts/Helper/all_protozoa.csv"
count=0

while IFS= read -r line
do
  echo "Processing line: $line"
  datasets download genome accession $line
  unzip -o ncbi_dataset.zip 
  touch $line.fna
  mv ncbi_dataset/data/$line/*_genomic.fna $line.fna
  count=$((count+1))
  if [ $count -eq 4600 ]; then
    break
  fi
done < "$file"
