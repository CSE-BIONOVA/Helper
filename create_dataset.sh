python ../../BashScripts/Helper/create_dataset.py
cat host.fasta bacteria.fasta virus.fasta fungi.fasta archaea.fasta protozoa.fasta  > shark_test.fasta
mkdir shark_test
mv shark_test.fasta shark_test
rm host.fasta bacteria.fasta virus.fasta fungi.fasta archaea.fasta protozoa.fasta
cp ../../BashScripts/Helper/datasets/shark_test_labels.csv shark_test
