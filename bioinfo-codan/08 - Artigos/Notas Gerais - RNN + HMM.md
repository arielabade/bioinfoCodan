


# A deep recurrent neural network discovers complex biological rules to decipher RNA protein-coding potential

**Uma coisa a se preocupar com LSTM "vanishing gradient problem"**

Embedding Layer:

Uma camada de embedding (embedding layer) é um componente importante em muitos modelos de aprendizado de máquina, especialmente aqueles usados em tarefas de processamento de linguagem natural (PLN) como classificação de texto, análise de sentimento e tradução de idiomas. Sua função principal é converter dados categóricos, como palavras ou caracteres, em vetores numéricos que podem ser processados por algoritmos de aprendizado de máquina.

Aqui está como ela funciona:

Mapeamento de Categorias para Vetores: Na PLN, palavras ou caracteres são considerados dados categóricos. Cada palavra ou caractere único é atribuído a um índice numérico único. A camada de embedding mapeia cada índice para um vetor correspondente de números reais, que representa a "incorporação" dessa categoria em um espaço vetorial contínuo.

Aprendizado de Representações Semânticas: Durante o processo de treinamento, a camada de embedding aprende as representações numéricas (embeddings) ideais para cada categoria com base nos dados em que é treinada. Esses embeddings capturam relacionamentos semânticos entre palavras ou caracteres. Por exemplo, palavras semelhantes podem ter representações vetoriais semelhantes no espaço de embedding.

Integração com Redes Neurais: A saída da camada de embedding, que é uma representação vetorial dos dados de entrada, é então alimentada nas camadas subsequentes da rede neural para processamento adicional. Isso permite que a rede neural aprenda padrões e relacionamentos complexos nos dados.

As camadas de embedding são poderosas porque permitem que modelos de aprendizado de máquina trabalhem de maneira eficaz com dados categóricos, especialmente em domínios como PLN, onde palavras e caracteres são componentes-chave dos dados de entrada.

---

FeelLNC: Wucher,V., Legeai,F., Hedan,B., Rizk,G., Lagoutte,L., Leeb,T.,
Jagannathan,V., Cadieu,E., David,A. and Lohi,H. (2017) FEELnc: a
tool for long non-coding RNA annotation and its application to the
dog transcriptome. Nucleic Acids Res., 45, e57.

---

#  Recurrrent Neural Network Based Model for Autism Spectrum Disorder Prediction using Codon Encoding

The work comprises the following phases: creating datasets, model building and evaluation.

# ToPS: A Framework to Manipulate Probabilistic Models of Sequence Data

GHMMs are very flexible probabilistic models that can be integrated with other models to describe a complex architecture. A wide majority of successful gene predictors use GHMMs as a base to recognize particular gene structures [13]–[16], [25]–[27]. However, for an unrestricted GHMM architecture that contains  states and a sequence with length , the complexity of the decoding algorithm is  [15], [28]. This is too inefficient when we are decoding large genomic sequences in systems with many states, which is typical with gene prediction. To circumvent this problem, gene predictors impose restrictions on the GHMM's architecture in order to provide a more efficient implementation. Decoding algorithms used in gene predictors require that GHMMs satisfy three important properties (adapted from [29]):

Limited connectivity: The number of transitions from a given state is less than a constant . This property limits the number of previous states searched by the Viterbi algorithm, resulting in an algorithm that is in .

Limited duration: The states have duration distributions limited by a constant . This property restricts the number of emission lengths that need to be analyzed by the Viterbi algorithm and, combined with the first restriction, results in an algorithm that is in .

Constant time lookup of the emission probabilities: The likelihood of a subsequence can be calculated in constant time after a linear time preprocessing of the sequence, resulting, when combined with the two previous optimizations, in a decoding algorithm that is in .

# Sobre RNNs

- Como criar um dataset pra treinar essa RNN?
- Como criar um protótió pra sair do zero?
- Existe alguma forma de pegar os dados de treino utilizados no Codan e usar para RNN?
- Como escolher uma função de ativação para RNNs?
- Keras, Torch, PyTorch, Tensorflow? Qual ferramenta?
- O que é backpropagation?

  Backpropagation, ou retropropagação, é um algoritmo fundamental usado em redes neurais artificiais para treinamento supervisionado. Ele é responsável por ajustar os pesos das conexões entre os neurônios para que a rede neural possa aprender a mapear entradas para saídas desejadas.

A ideia por trás do backpropagation é calcular o gradiente da função de erro em relação aos pesos da rede neural, utilizando o algoritmo de gradiente descendente para minimizar esse erro. O processo é dividido em duas fases:

1. **Forward Pass (Passagem Direta):** Durante esta fase, os dados de entrada são propagados pela rede neural camada por camada, gerando uma saída. Essa saída é comparada com a saída desejada (rótulo) para calcular o erro da rede.

2. **Backward Pass (Passagem Reversa):** Nesta fase, o gradiente do erro em relação aos pesos da rede é calculado usando a regra da cadeia (chain rule). O gradiente é então usado para atualizar os pesos da rede, de forma a reduzir o erro na próxima iteração do treinamento.

O processo de backpropagation é iterativo e geralmente é executado em lotes de dados (batch), onde várias entradas são processadas ao mesmo tempo para melhorar a eficiência computacional. Este algoritmo é essencial para o sucesso do treinamento de redes neurais profundas, pois permite ajustar uma grande quantidade de parâmetros de maneira eficiente.

---

Perguntas e Pontuações gerais:

- Pegar a imagem que fala sobre os tipos de RNN do artigo do karpathy e ver em qual caso o nosso se classifica
- È possível usar o tops e o karpathy + o de autismo como referência pra construir essa classificação?
- Começar do zero ou montar o ensemble em cima do que já tem?
- Como a gente consegue pegar os dados de treino das classificações mencionadas pelo autor do Codan e treinar a RNN? seria necessário/possível fazer isso baseado no ToPS?
- Qual o melhor modelo de RNN? LSTM, DNN ou o outro lá? (O Karpathy fala que o LSTM é melhor, outros artigos também mostram que LSTM é melhor)

Alguns links úteis:

http://karpathy.github.io/2015/05/21/rnn-effectiveness/

https://academic.oup.com/bib/article/22/3/bbaa045/5847603

https://academic.oup.com/nar/article/46/16/8105/5050624

https://link.springer.com/article/10.1007/s40031-021-00669-4

https://academic.oup.com/nar/article/44/D1/D733/2502674

https://academic.oup.com/nar/article/43/12/e78/2902598

https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003234

https://gist.github.com/karpathy/d4dee566867f8291f086

https://github.com/karpathy/char-rnn

https://torch.ch/

https://karpathy.github.io/2019/04/25/recipe/

https://openreview.net/pdf?id=rJxEso0osm

https://arxiv.org/pdf/2006.03151.pdf

https://github.com/hendrixlab/mRNN -> implementação de identtificação de codons com RNN

