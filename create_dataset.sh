python ../../BashScripts/Helper/create_dataset.py
cat host.fasta bateria.fasta virus.fasta fungi.fasta archaea.fasta protozoa.fasta  > human_train.fasta
mkdir human_train
mv human_train.fasta human_train
rm host.fasta bateria.fasta virus.fasta fungi.fasta archaea.fasta protozoa.fasta
cp ../../BashScripts/Helper/datasets/human_train_labels.csv human_train
