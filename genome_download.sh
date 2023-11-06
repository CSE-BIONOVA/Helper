# species type
SPECIES=$1
FILENAME=$2
ASSEMBLY_SUMMARY="../../Genome/$SPECIES/assembly_summary.txt"
while IFS= read -r line 
do 
	#LINK=$(grep $line $ASSEMBLY_SUMMARY | cut -f20) 
	#SPECIES_NAME=$(grep $line $ASSEMBLY_SUMMARY | cut -f7)
	LINK= cut -f20
	SPECIES= cut -f7
	echo $SPECIES
	wget $LINK
done < $ASSEMBLY_SUMMARY
