# TODO
# Transformar os arquivos fasta em numpy arrays para que o TensorFlow consiga operar sobre eles
# One-hot vs

import tensorflow as tf
import numpy as np
from Bio import SeqIO
import pandas as pd
import matplotlib.pyplot as plt

def fasta_to_list(file): # transforma os arquivos fasta em listas com as strings
    sequences = []
    headers = [] # temos interesse em manter os IDs?
    with open(file, 'r') as fasta_file:
        for record in SeqIO.parse(fasta_file, "fasta"):
            sequences.append(str(record.seq))
            headers.append(record.id)
    return sequences, headers

#sequences, headers = fasta_to_list('./bin/models/VERT_full/dataset/train.fa') # exemplo qualquer para fins de teste


# Abordagem one-hot vector: utiliza vetores binarios de 4 dimensoes para classificar as bases
def one_hot_encoding(sequences):
    vectors = {'A': [1,0,0,0], 'G': [0,1,0,0], 'C': [0,0,1,0], 'T': [0,0,0,1]}
    onehot = []
    for seq in sequences:
        for base in seq:
            onehot.append(vectors[base])
    return np.array(onehot)

def binary_annotated_fasta(fasta_file, annotation_file):
    #fasta_list = fasta_to_list(fasta_file)
    annotation = pd.read_csv(annotation_file, sep='\t', header=None)
    start_indexes = annotation[3].to_list()
    end_indexes = annotation[4].to_list()

    cds_regions = list(zip(start_indexes, end_indexes))
        
    fasta_binary = []

    with open(fasta_file, 'r') as file:
        genome = ''.join(line.strip() for line in file.readlines()[1:])

    for i in range(len(genome)):
        is_cds = any(start-1 <= i < end-1 for start, end in cds_regions)
        fasta_binary.append('1' if is_cds else '0')
    
    binary_fasta_string = ''.join(fasta_binary)


    return binary_fasta_string

print(binary_annotated_fasta('genome.fasta', 'annotation.gtf'))





# Modelo de RNN utilizando TensorFlow e Keras (falta instanciar/parametrizar)
class CodanRNN(tf.keras.Model):
    def __init__(self, input_shape, hidden_units, output_units):
        super(CodanRNN, self).__init__()
        self.rnn = tf.keras.layers.SimpleRNN(hidden_units, return_sequences=True)
        self.fc = tf.keras.layers.Dense(output_units)
    
    def call(self, inputs):
        x = self.rnn(inputs)
        x = self.fc(x[:, -1, :])  # Use only the last time step's output
        return x
