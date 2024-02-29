# Makefile for running codan.py

#standard
TRANSCRIPTS_FA = ../bin/transcripts/transcripts.fa


# partial_models
MODEL_PATH_VERTEBRATES_PARTIAL = ../bin/models/VERT_partial
MODEL_PATH_INVERTEBRATES_PARTIAL = ../bin/models/INV_partial
MODEL_PATH_FUNGI_PARTIAL = ../bin/models/FUNGI_partial
MODEL_PATH_PLANTS_PARTIAL = ../bin/models/PLANTS_partial

# full_models
MODEL_PATH_VERTEBRATES_FULL = ../bin/models/VERT_full
MODEL_PATH_INVERTEBRATES_FULL = ../bin/models/INV_full
MODEL_PATH_FUNGI_FULL = ../bin/models/FUNGI_full
MODEL_PATH_PLANTS_FULL = ../bin/models/PLANTS_full


##paths
## invertebrates
DROSOPHILA_CHROMOSOMES_FA = ../bin/transcripts/drosophilaChromosomesINV.fa

## fungi
CORDYCEPS_GENOME_FA = ../bin/transcripts/cordycepsGenomeMapping.fa

## vertebrates
HUMAN_CHROMOSES_FA = ../bin/transcripts/humanChromosomeVERT.fa

## plants
DROSERA_GENOME_FA = ../bin/transcripts/droseraCompleteGenomePLANT.fasta


## outputfolders



# command
CODAN_COMMAND = codan.py -t $(TRANSCRIPTS_FA) -m $(MODEL_PATH_VERTEBRATES)
DROSOPHILA_COMMAND = codan.py -t $(DROSOPHILA_CHROMOSOMES_FA) -m $(MODEL_PATH_INVERTEBRATES_FULL)
DROSERA_COMMAND = codan.py -t $(DROSERA_GENOME_FA) -m $(MODEL_PATH_PLANTS_FULL)
CORDYCEPS_COMMAND = codan.py -t $(CORDYCEPS_GENOME_FA) -m $(MODEL_PATH_FUNGI_FULL)
HUMAN_COMMAND = codan.py -t $(HUMAN_CHROMOSES_FA) -m $(MODEL_PATH_VERTEBRATES_FULL)

# run
run_drosophila:
	$(DROSOPHILA_COMMAND)
	$(DROSERA_COMMAND)
	$(DROSERA_COMMAND)
	$(CORDYCEPS_COMMAND)
	$(HUMAN_COMMAND)

all: run_drosophila

