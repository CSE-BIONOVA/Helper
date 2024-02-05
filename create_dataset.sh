python ../../BashScripts/Helper/create_dataset.py
cat host.fasta bacteria.fasta virus.fasta fungi.fasta archaea.fasta protozoa.fasta  > human_train.fasta
mkdir human_train
mv *.fasta human_train
cp ../../BashScripts/Helper/datasets/final/human_train_labels.csv human_train
