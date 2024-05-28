# TODO
# Transformar os arquivos fasta em numpy arrays para que o TensorFlow consiga operar sobre eles
# One-hot vs

import tensorflow as tf
import numpy as np
from Bio import SeqIO

def fasta_to_list(file): # transforma os arquivos fasta em listas com as strings
    sequences = []
    headers = [] # temos interesse em manter os IDs?
    with open(file, 'r') as fasta_file:
        for record in SeqIO.parse(fasta_file, "fasta"):
            sequences.append(str(record.seq))
            headers.append(record.id)
    return sequences, headers

sequences, headers = fasta_to_list('./bin/models/VERT_full/dataset/train.fa') # exemplo qualquer para fins de teste


# Abordagem one-hot vector: utiliza vetores binarios de 4 dimensoes para classificar as bases
def one_hot_encoding(sequences):
    vectors = {'A': [1,0,0,0], 'G': [0,1,0,0], 'C': [0,0,1,0], 'T': [0,0,0,1]}
    onehot = []
    for seq in sequences:
        for base in seq:
            onehot.append(vectors[base])
    return np.array(onehot)

lens = [len(x) for x in sequences]
print(lens)





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
