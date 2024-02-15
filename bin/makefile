
# Makefile for running codan.py

# Paths
TRANSCRIPTS_FA = /home/ariel/bioinfoCodan/bin/transcripts/transcripts.fa
DROSOPHILA_CHROMOSOMES_FA = /home/ariel/bioinfoCodan/bin/transcripts/drosophilaChromosomesINV.fa
CORDYCEPS_GENOME_FA = /home/ariel/bioinfoCodan/bin/transcripts/cordycepsGenomeMapping.fa
DROSERA_GENOME_FA = /home/ariel/bioinfoCodan/bin/transcripts/droseraCompleteGenomePLANT.fasta
HUMAN_CHROMOSES_FA = /home/ariel/bioinfoCodan/bin/transcripts/humanChromosomeVERT.fa

#partial_models

MODEL_PATH_VERTEBRATES_PARTIAL = /home/ariel/bioinfoCodan/bin/models/VERT_partial
MODEL_PATH_INVERTEBRATES_PARTIAL = /home/ariel/bioinfoCodan/bin/models/INV_partial
MODEL_PATH_FUNGI_PARTIAL = /home/ariel/bioinfoCodan/bin/models/FUNGI_partial
MODEL_PATH_PLANTS_PARTIAL = /home/ariel/bioinfoCodan/bin/models/PLANTS_partial

#full_models

MODEL_PATH_VERTEBRATES_FULL = /home/ariel/bioinfoCodan/bin/models/VERT_full
MODEL_PATH_INVERTEBRATES_FULL = /home/ariel/bioinfoCodan/bin/models/INV_full
MODEL_PATH_FUNGI_FULL = /home/ariel/bioinfoCodan/bin/models/FUNGI_full
MODEL_PATH_PLANTS_FULL = /home/ariel/bioinfoCodan/bin/models/PLANTS_full

###################

# categories


## invertebrates


## fungi


## vertebrates


## plants

# Command
CODAN_COMMAND = codan.py -t $(TRANSCRIPTS_FA) -m $(MODEL_PATH_VERTEBRATES)
DROSOPHILA_COMMAND = codan.py -t $(DROSOPHILA_CHROMOSOMES_FA) -m $(MODEL_PATH_INVERTEBRATES_FULL)
DROSERA_COMMAND = codan.py -t $(DROSERA_GENOME_FA) -m $(MODEL_PATH_PLANTS_FULL)


run_drosophila:
	$(DROSOPHILA_COMMAND)
	$(DROSERA_COMMAND)
	
all:
	$(DROSERA_COMMAND)
	
	
	
	
	
