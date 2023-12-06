import csv
import urllib.request

# csv_file = '../../BashScripts/Helper/bacteria_human.csv'
csv_file = 'bacteria_human.csv'
new_csv_file = 'bactria_accession.csv'

accession_array = []
with open(new_csv_file, 'r') as file:
    lines = file.readlines()
    for line in lines:
        accession = line.split(',')[0]
        accession_array.append(accession)	
        
print(accession_array)
new_file = open(new_csv_file, "a")
writer = csv.writer(new_file)

with open(csv_file, 'r') as file:
    lines = file.readlines()[2500:]
    reader = csv.DictReader(file)
    counter = 2350
    for line in lines:
        ftp_link = line.split(',')[3][1:-1	] 
        print(ftp_link)
        if ftp_link:
            accession = line.split(',')[1][1:-1]
            if accession in accession_array:
                continue
            new_file_name = f"{accession}.fna.gz"
            file_name = ftp_link.split("/")[-1] + "_genomic.fna.gz"
            saved_file_name=file_name[:-3]
            url = f"https://{ftp_link[6:]}/{file_name}"
            print(url)
            urllib.request.urlretrieve(url, new_file_name)  # Save the downloaded file
            writer.writerow([accession, new_file_name])  # Write data row
            print(counter)
            counter += 1
            if counter == 4000:
                break

new_file.close()	