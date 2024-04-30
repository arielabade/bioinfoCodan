Tuesday, 26 March 2024

Notas CodAn
Conceitos básicos de biologia: genes, genoma, etc.
Gene: o conceito Mendeliano de gene é a unidade básica de hereditariedade. O gene molecular é uma sequência de nucleotídeos em DNA que é transcrita para produzir um RNA funcional. Existem os genes codificadores de proteínas e os não codificadores.
Genoma: é toda a informação genética de um organismo, que consiste de sequências de nucleotídeos de DNA (ou RNA, em vírus de RNA). O genoma nuclear consiste em genes codificadores e não-codificadores de proteínas.
Região codificadora (Coding region - CDS): é a porção do DNA ou RNA de um gene que codifica uma proteína. Estudar a região codificadora e seus atributos é essencial para a compreensão da organização dos genes e da evolução de eucariontes e procariontes. Isso pode auxiliar no mapeamento do genoma humano e no desenvolvimento da terapia genética.
Anotação de DNA/RNA
É o processo de descrever a estrutura e função dos componentes de um genoma, analisando e interpretando para extrair sua significância biológica e entender os processos biológicos dos quais participam;
Identifica a localização de genes e todas as regiões codificadoras de um genoma e determina o que cada um desses genes faz.
Arquivos FASTA (https://pt.wikipedia.org/wiki/Formato_FASTA)
Em bioinformática, o formato FASTA é um formato baseado em texto para representar tanto sequencias de nucleótidos quanto sequencias de peptídeos, no qual os nucleotídeos ou aminoácidos são representados usando códigos de uma única letra
Modelos Markov (https://en.wikipedia.org/wiki/Markov_model)
Modelo aleatório usado para modelar sistemas que mudam de maneira pseudoaleatória. Assume que estados futuros dependem apenas do estado atual e não de eventos que aconteceram antes. Na área de modelagem de previsão, é interessante que os modelos tenham a propriedade Markov.
Cadeia de Markov: Modela o estado de um sistema com uma variável aleatória que muda com o tempo. A distribuição para essa variável depende apenas da distribuição do estado anterior.
Hidden Markov Model (HMM): é uma Cadeia de Markov na qual o estado é apenas parcialmente observável ou contém ruído. As observações estão relacionadas ao estado do sistema, mas são insuficientes para determinar com precisão o estado. Algoritmos para HMMs: Viterbi - computa a sequência de estados mais provável; Forward - computa a probabilidade da sequência de observações. Exemplo: em reconhecimento de voz, os dados observados são as ondas de áudio e o estado escondido (Hidden state) é o texto que se fala. Nesse contexto, o algoritmo Viterbi encontra a sequência de palavras mais provável.
Algoritmo Viterbi (https://en.wikipedia.org/wiki/Viterbi_algorithm)
Usado em HMMs (Hidden Markov Models)
ToPS (https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003234)
Framework para manipular modelos probabilísticos de sequências de dados;
Inclui modelos probabilísticos como cadeias de Markov de comprimento variável, HMMs, Profile Hidden Markov Models, GHMM (generalizada), entre outros. Não vi nada falando sobre RNN (Recurring Neural Network). Porém é importante sanar essa dúvida: Por que estamos utilizando HMM e RNN como coisas distintas? Qual é precisamente a diferença entre essas duas coisas?
ToPS é utilizado, entre outros, para anotação de transcritos, caracterização de pequeno RNA e previsões de genes;
ToPS possui as classes ProbabilisticModel para representar as implementações dos modelos; ProbabilisticModelCreator para especificar a criação de modelos baseado em arquivos de configuração; e ProbabilisticModelParameterValue para habilitar o parsing de arquivos de configuração.
Será que seria possível implementar o modelo RNN dentro do ToPS para que a utilização e a implementação sejam padronizadas?
Funcionalidades: bayes_classifier, evaluate, posterior_decoding, simulate, train, viterbi_decoding 
“Implementing new models as a subclass of ProbabilisticModel will ensure integration with the facilities for training, simulating, decoding, integration in GHMMs and construction of Bayesian classifiers”;
Guia do Usuário: http://tops.sourceforge.net/tops-doc.pdf
Escolher os parâmetros para os algoritmos de treinamento pode ser muito difícil e tedioso. Por isso, ToPS oferece dois critérios de seleção de modelos, Bayesian Information Criteria (BIC) e Akaike Information Criteria (AIC). O objetivo de ambos é selecionar os parâmetros para os quais o modelo correspondente tem o menor valor para fórmulas determinadas nos dois.
Biopython - SeqIO (https://biopython.org/wiki/SeqIO)
=========LER ARQUIVOS===========
Interface uniforme para tratar formatos de arquivos de sequências. Apenas trata objetos do tipo SeqRecord;
Inspirado na biblioteca Perl Bioperl, módulo SeqIO;
Suporte a vários formatos, incluindo FASTA. Cada registro começa com uma linha >. 
Função principal: Bio.SeqIO.parse(nome_arquivo/caminho_arquivo, formato) - retorna um iterado do tipo SeqRecord:
	from Bio import SeqIO
	for record in SeqIO.parse(“exemplo.fasta", “fasta”):
		print(record.id)

	from Bio import SeqIO
	with open(“exemplo.fasta”) as handle:
		for record in SeqIO.parse(handle, “fasta”):
			print(record.id)
Obs.: Quando usar o comando “open”, utilizar antes o comando “with" para que o arquivo feche corretamente após os comandos. Ao usar do primeiro jeito, isso é feito automaticamente.
Iteradores são bons quando você precisa dos registros um por um, naquela ordem. Você também pode convertê-los em uma lista comum do Python usando o comando list(): x = list(SeqIO.parse(“exemplo.fasta”, “fasta"))
Para arquivos pequenos, existe o comando SeqIO.to_dict(<SeqRecordIterator>), que usa o ID do registro como chave para um dicionário normal Python. Porém, você pode especificar um mapeamento customizado usando o parâmetro key_function;
Para arquivos grandes, existe o comando SeqIO.index(<SeqRecordIterator>) a partir do Biopython 1.52. Você pode considerar também usar BioSQL;
O comando SeqIO.read(nome_arquivo, formato) é usado quando o arquivo contém apenas um registro. Retorna uma instância SeqRecord. Se tiver mais de um registro (ou nenhum), dá erro;
==========ESCREVER ARQUIVOS==============
SeqIO.write(<SeqRecordIterator>, nome_arquivo, formato);
	from Bio import SeqIO
	sequences = xxx
	with open(“exemplo.fasta”, “w") as output_handle:
		SeqIO.write(sequences, output_handle, “fasta")

	from Bio import SeqIO
	sequences = xxx
	SeqIO.write(sequences, “exemplo.fasta”, “fasta")
Obs.: se a entrada for um iterador SeqRecord, para arquivos FASTA os registros serão escritos um por um. Isso requer muito pouca memória.
OptParse
É uma biblioteca usada para colocar os parâmetros na linha de comando na hora de executar o programa (coda.py -t, coda.py -o, etc.)
mRNN - Deep Learning article
Deep learning methods can independently discover complex biological rules in the data de novo.
Deep learning avoids biases introduced by human-engineered features
RNNs are better suited for learning sequential patterns due to their serialized structure and ability to handle variable-length inputs.
Some studies show that gated recurrent unit RNNs (GRU RNNs) have better performance in bioinformatics tasks than long short-term memory RNNs (LSTMs)
While the usual implementation of RNNs for this purpose involves vectors such as (0,0,1,0), where each position represents A, C, G and U, the authors used a different approach, using an embedding layer.
State-of-the-art lncRNA classification tool: FEELnc.
Difficulties in protein-coding assessment involve the lack of a start or stop codons in the annotated CDS.
Two datasets: a normal dataset containing 500 mRNA and 500 lncRNA from human transcripts; and a challenge dataset, 500 mRNA with short CDS (<= 50 codons) and 500 lncRNA with long (untranslated) ORFs (>=50 codons).
Other classification tools: longest - SVM, and CPAT
Despite mRNN’s featureless architecture, which precluded it from integrating human knowledge of mRNA structure into its learning process, mRNN was able to learn true defining features of mRNAs, including trinucleotide patterns and depletion of in-frame stop codons after the start of an open-reading frame.
RefSeq database
O projeto RefSeq no Centro Nacional de Informação em Biotecnologia (NCBI) mantém um banco de dados público que contém registros de sequências de proteínas, transcritos e genomas anotados de diversos tipos de organismos (eucariontes, procariontes e vírus);
O banco RefSeq fornece um sistema de coordenadas estável e consistente, que serve como base para informar dados específicos a genes, variação clínica, e comparações entre espécies;
