from Bio import SeqIO
import csv

def get_chromosome_name(fasta_file):	
    for record in SeqIO.parse(fasta_file, "fasta"):
        return record.description    

if __name__ == "__main__":
    dna_list_file = "temp_files/dna_list.csv"
    dna_type_file = "temp_files/dna_type.csv"

    dna_list = csv.reader(open(dna_list_file))	
    dna_type = csv.writer(open(dna_type_file, "w"))

    for i in range(len(dna_list)):
        line = dna_list[i]
        index = line[0]
        dna_file = line[1]
        chromosome_name = get_chromosome_name(dna_file)
        dna_type.writerow([index, chromosome_name])
        print(f"{i} : {chromosome_name}")

    dna_type.close()
    dna_list.close()