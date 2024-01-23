python ../../BashScripts/Helper/create_dataset.py
cat host.fasta bacteria.fasta virus.fasta fungi.fasta archaea.fasta protozoa.fasta  > shark_train.fasta
mkdir shark_train
mv shark_train.fasta shark_train
rm host.fasta bacteria.fasta virus.fasta fungi.fasta archaea.fasta protozoa.fasta
cp ../../BashScripts/Helper/datasets/shark_train_labels.csv shark_train
