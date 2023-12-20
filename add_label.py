from Bio import SeqIO
import csv

        
def read_csv_file(file_path):
    data = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.update({row[0].split(".")[0]: row[1].split("/")[3]})
    return data
       
    
if __name__ == "__main__":
    dna_file="accession/human_metagenome/no_of_reads1.csv"
    read_label_file="label.csv"
    read_info_file="read_info.csv"
    fasta_file = "../../Metagenome/human/aligned/final.fasta"

    dna = read_csv_file(dna_file)   
    read_label = csv.writer(open(read_label_file, "w"))
    read_info = csv.writer(open(read_info_file, "w"))

    read_label.writerow(["id", "y_true"])
    read_info.writerow(["id", "genome_type", "length", "accession"])

    records = list(SeqIO.parse(fasta_file, "fasta"))
    labels = {
        "Human": 1,
        "Bacteria": 2,
        "Virus": 3,
        "Fungi": 4,
        "Archaea": 5,
        "Protozoa": 6
    }
    for read in records:
        read_id = read.id
        accession = read_id.split("_")[0]
        genome_type = dna[accession] 
        read_length = int(read_id.split("_")[-2])  
        read_label.writerow([read_id, genome_type])
        read_info.writerow([read_id, genome_type, read_length])
        label = labels[genome_type]
        read_label.writerow([read_id, label])
        read_info.writerow([read_id, genome_type, read_length, accession])

    read_label.close()
    read_info.close()
    