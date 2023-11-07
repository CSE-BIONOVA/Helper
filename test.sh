species=$1
A="../../Genome/$species/assembly_summary.txt"
B="../../Genome/$species"
array=()
a_file="$species.csv"
echo "accession,species" >> a_file
while IFS=$'\t' read -r -a line 
do 
	s=${line[7]} 
	if [[ " ${array[*]} " = *" $s "* ]] ; then 
		: 
	else
		accession=${line[0]}
		url=${line[19]}
		a=$(basename "$url") 
		new_a="${a}_genomic.fna.gz"
		echo $new_a
		link="$url/$new_a"
		echo "$link"
		array+=($s)
		echo "Species: $s"
		wget "$link" -P $B
		echo "$accession,$s" >> $a_file
	fi
done < $A
