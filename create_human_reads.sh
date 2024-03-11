python3 ../../Simtools/NanoSim/src/simulator.py genome -rg GCF_000001405.40_GRCh38.p14_genomic.fna -c ../../Simtools/NanoSim/pre-trained_models/metagenome_ERR3152364_Even/training -dna_type linear -o human_1 -n  300
grep ">" human_1_aligned_reads.fasta | wc -l
python3 ../../Simtools/NanoSim/src/simulator.py genome -rg GCF_000001405.40_GRCh38.p14_genomic.fna -c ../../Simtools/NanoSim/pre-trained_models/metagenome_ERR3152364_Even/training -dna_type linear -o human_25 -n  8000
grep ">" human_25_aligned_reads.fasta | wc -l
python3 ../../Simtools/NanoSim/src/simulator.py genome -rg GCF_000001405.40_GRCh38.p14_genomic.fna -c ../../Simtools/NanoSim/pre-trained_models/metagenome_ERR3152364_Even/training -dna_type linear -o human_50 -n  14500
grep ">" human_50_aligned_reads.fasta | wc -l
python3 ../../Simtools/NanoSim/src/simulator.py genome -rg GCF_000001405.40_GRCh38.p14_genomic.fna -c ../../Simtools/NanoSim/pre-trained_models/metagenome_ERR3152364_Even/training -dna_type linear -o human_75 -n  25000
grep ">" human_75_aligned_reads.fasta | wc -l
python3 ../../Simtools/NanoSim/src/simulator.py genome -rg GCF_000001405.40_GRCh38.p14_genomic.fna -c ../../Simtools/NanoSim/pre-trained_models/metagenome_ERR3152364_Even/training -dna_type linear -o human_99 -n  55000
grep ">" human_99_aligned_reads.fasta | wc -l