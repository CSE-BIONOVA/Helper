coverage='coverage_list.csv'

while IFS=',' read -r -a line
do 
    file_path=${line[0]}
    coverage=${line[1]}
    badread simulate --reference $file_path --quantity $coverage 
done < "$coverage"