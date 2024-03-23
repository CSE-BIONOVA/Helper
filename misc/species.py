user_input = input("Organism: ")
filename = "C:/Users/samadhi/Desktop/FYP/code/Helper/Summary/assembly_summary_" + str(user_input) + ".txt"

species_dict = {}
with open(filename, 'r', encoding="utf8") as file:
    lines = file.readlines()
    for line in lines:
        if line.startswith('#'):
            continue
        species = line.strip().split('\t')[7]
        accession = line.strip().split('\t')[0].split('.')[0]
        if species in species_dict:
            species_dict[species].append(accession)
        else:
            species_dict[species] = [accession]

print(species_dict)
print(len(species_dict))
