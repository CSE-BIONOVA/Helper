file = 'viruses (1).csv'
new_file = 'viruses.csv'

with open(file, 'r') as f:
    lines = f.readlines()

lines = [line.replace('"', '') for line in lines if line.strip()]

with open(new_file, 'w') as f:
    f.writelines(lines)
