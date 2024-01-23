python ../../BashScripts/Helper/create_dataset.py
cat *.fasta > human_train.fasta
mkdir human_train
mv human_train.fasta human_train
rm *.fasta
cp ../../BashScripts/Helper/datasets/human_train_labels.csv human_train
