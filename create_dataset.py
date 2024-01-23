from Bio import SeqIO
import csv


def get_files_array(filename, file_path_prefix):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        files = []
        for row in reader:
            files.append(file_path_prefix + row[0])
        return files


def create_dataset(reads_array, l_file, out_fasta, organism, used_reads):
    used_reads_file = open(used_reads, "w")

    with open(l_file, "a") as file:
        label_writer = csv.writer(file)
        with open(out_fasta, "w") as out_file:
            count = 0
            for row in reads_array:
                used_reads_file.write(row + "\n")
                for record in SeqIO.parse(row, "fasta"):
                    count += 1
                    SeqIO.write(record, out_file, "fasta")
                    label_writer.writerow([record.id, organism, len(record.seq)])
                    if count == 100000:
                        out_file.close()
                        used_reads_file.close()
                        return


def create_dataset_from_end(reads_array, l_file, out_fasta, organism, used_reads):
    used_reads_file = open(used_reads, "w")

    with open(l_file, "a") as file:
        label_writer = csv.writer(file)
        with open(out_fasta, "w") as out_file:
            count = 0
            for row in reads_array:
                used_reads_file.write(row + "\n")
                records = list(SeqIO.parse(row, "fasta"))
                for i in range(len(records) - 1, -1, -1):
                    record = records[i]
                    count += 1
                    SeqIO.write(record, out_file, "fasta")
                    label_writer.writerow([record.id, organism, len(record.seq)])
                    if count == 3500:
                        out_file.close()
                        used_reads_file.close()
                        return


if __name__ == "__main__":
    bacteria_reads = "../../BashScripts/Helper/all_reads/bacteria.csv"
    archaea_reads = "../../BashScripts/Helper/all_reads/archaea.csv"
    fungi_reads = "../../BashScripts/Helper/all_reads/fungi.csv"
    protozoa_reads = "../../BashScripts/Helper/all_reads/protozoa.csv"
    virus_reads = "../../BashScripts/Helper/all_reads/virus.csv"

    bacteria_used_reads = "../../BashScripts/Helper/all_reads/used/bacteria.csv"
    archaea_used_reads = "../../BashScripts/Helper/all_reads/used/archaea.csv"
    fungi_used_reads = "../../BashScripts/Helper/all_reads/used/fungi.csv"
    protozoa_used_reads = "../../BashScripts/Helper/all_reads/used/protozoa.csv"
    virus_used_reads = "../../BashScripts/Helper/all_reads/used/virus.csv"
    host_used_reads = "../../BashScripts/Helper/all_reads/used/host.csv"

    label_file = "../../BashScripts/Helper/datasets/human_train_labels.csv"

    bacteria = get_files_array(bacteria_reads, "../../Genome/Bacteria/")
    archaea = get_files_array(archaea_reads, "../../Genome/Archaea/")
    fungi = get_files_array(fungi_reads, "../../Genome/Fungi/")
    protozoa = get_files_array(protozoa_reads, "../../Genome/Protozoa/")
    virus = get_files_array(virus_reads, "../../Genome/Virus/")
    host = ["../../Genome/Human/human_01_aligned_reads.fasta"]

    with open(label_file, "w") as label_file:
        label_writer = csv.writer(label_file)
        label_writer.writerow(["id", "y_true", " length"])

    create_dataset(host, "../../BashScripts/Helper/datasets/human_train_labels.csv", "host.fasta", 1, host_used_reads)
    create_dataset(bacteria, "../../BashScripts/Helper/datasets/human_train_labels.csv", "bacteria.fasta", 2,
                   bacteria_used_reads)
    create_dataset(virus, "../../BashScripts/Helper/datasets/human_train_labels.csv", "virus.fasta", 3,
                   virus_used_reads)
    create_dataset(fungi, "../../BashScripts/Helper/datasets/human_train_labels.csv", "fungi.fasta", 4,
                   fungi_used_reads)
    create_dataset(archaea, "../../BashScripts/Helper/datasets/human_train_labels.csv", "archaea.fasta", 5,
                   archaea_used_reads)
    create_dataset(protozoa, "../../BashScripts/Helper/datasets/human_train_labels.csv", "protozoa.fasta", 6,
                   protozoa_used_reads)
