import csv 

#downloaded microbial accessions
fungi = 'Fungi.csv'
archaea = 'Archaea.csv'
protozoa = 'Protozoa.csv'
bactria = 'Bacteria.csv'    

assembly_fungi = 'assembly_summary_fungi.txt'
assembly_archaea = 'assembly_summary_archaea.txt'
assembly_protozoa = 'assembly_summary_protozoa.txt'
assembly_bacteria = 'assembly_summary_bacteria.csv'

accession_fungi = 'accession_fungi.txt'
accession_archaea = 'accession_archaea.txt'
accession_protozoa = 'accession_protozoa.txt'
accession_bacteria = 'accession_bacteria.txt'

def get_accession(file, assembly_file, accession_file):
    accession = []
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            accession.append(row[0])

    count = len(accession)
    with open(assembly_file) as assembly:
        with open(accession_file, 'w') as accession_file:
            for line in assembly:
                if line.startswith('#'):
                    continue
                else:
                    line = line.split('\t')
                    if line[0] in accession:
                        count -= 1
                        accession_file.write(line[3] + '\n')
                if (count <= 0): 
                    break

def get_accession_from_csv(file, summary_file, accessioon_file):
    accession = []
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            accession.append(row[0])
    
    count = len(accession)
    with open(summary_file) as summary:
        with open(accessioon_file, 'w') as accession_file:
            for line in summary:
                if line.startswith('#'):
                    continue
                else:
                    line = line.split(',')
                    if line[5][1:-1] in accession:
                        count -= 1
                        accession_file.write(line[3] + '\n')
                if (count <= 0): 
                    break


if __name__ == '__main__':
    # get_accession(protozoa, assembly_protozoa, accession_protozoa)
    # get_accession(archaea, assembly_archaea, accession_archaea)
    # get_accession(fungi, assembly_fungi, accession_fungi)
    get_accession_from_csv(bactria, assembly_bacteria, accession_bacteria)