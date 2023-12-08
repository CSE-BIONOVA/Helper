file = 'accession_bacteria.txt'
new_file = 'accession_bacteria_new.txt'

with open(file, 'r') as f:
    lines = f.readlines()

lines = [line.replace('"', '') for line in lines if line.strip()]

with open(new_file, 'w') as f:
    f.writelines(lines)
