A="../../Genome/Archea/assembly_summary.txt"
array=()
while IFS=$'\t' read -r -a line 
do 
	s=${line[7]} 
	if [[ " ${array[*]} " = *" $s "* ]] ; then 
		: 
	else
		accession=${line[0]}
		echo "Acc: $accession"
		link=${line[19]}
		array+=($s)
		echo "Species: $s"
		wget $link
	fi
done < $A
filename="bacteria.txt"
for e in "${array[@]}"
do 
	echo "$e" >> "$filename"
done
