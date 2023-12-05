# Makefile for running codan.py

# Paths
TRANSCRIPTS_FA = /home/ariel-bioinfo-codan/Downloads/transcripts.fa
MODEL_PATH = /home/ariel-bioinfo-codan/CodAn/models/FUNGI_full

# Command
CODAN_COMMAND = codan.py -t $(TRANSCRIPTS_FA) -m $(MODEL_PATH)

all:
	$(CODAN_COMMAND)

