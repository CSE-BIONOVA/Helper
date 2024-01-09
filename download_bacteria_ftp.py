import csv
import urllib.request

csv_file = '../../BashScripts/Helper/bacteria_human.csv'
new_csv_file = 'bactria_accession.csv'

with open(new_csv_file, 'r') as file:
    new_reader = csv.reader(file)
    accession_array = [row[0] for row in new_reader]	

with open(csv_file, 'r') as file:
    with open(new_csv_file, 'a', newline='') as new_file:
        reader = csv.DictReader(file)
        writer = csv.writer(new_file)
        counter = 0

        for row in reader:
            ftp_link = row['GenBank FTP']
            if ftp_link:
                accession = row['Assembly']
                if accession in accession_array:
                    continue
                new_file_name = f"{accession}.fna.gz"
                file_name = ftp_link.split("/")[-1] + "_genomic.fna.gz"
                saved_file_name=file_name[:-3]
                url = f"https://{ftp_link[6:]}/{file_name}"
                urllib.request.urlretrieve(url, new_file_name)  # Save the downloaded file
                writer.writerow([accession, new_file_name])  # Write data row
                print(counter)
                counter += 1
                if counter == 4000:
                    break

