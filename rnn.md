https://www.youtube.com/watch?v=AsNTP8Kwu80

OBS: o estudo relacionado a autismo mostra que o uso de decisions tree com rnns quando se trata de avaliar cadeias de DNA é promissor
OBS2: e se usar as classificações dos pesos de entrada dos datasets que contém as HMMs como as funções recorrentes das RNNS?

## LSTM

LSTM (Long Short-Term Memory) é um tipo de rede neural recorrente (RNN) que foi projetado para superar algumas limitações das RNNs tradicionais, especialmente em lidar com problemas de longo prazo e dependências temporais. As LSTMs foram propostas por Sepp Hochreiter e Jürgen Schmidhuber em 1997.

A principal diferença entre uma LSTM e uma RNN convencional está na capacidade de lembrar informações de longo prazo. As LSTMs possuem unidades de memória (células de memória) que podem armazenar e acessar informações por longos períodos de tempo, evitando assim o problema do desaparecimento do gradiente, que é uma dificuldade comum em RNNs durante o treinamento.

As unidades de uma LSTM são projetadas para controlar o fluxo de informações usando três portas principais:

1. **Porta de Esquecimento (Forget Gate):** Controla a quantidade de informação que deve ser descartada da célula de memória.
   
2. **Porta de Entrada (Input Gate):** Regula a quantidade de nova informação que deve ser adicionada à célula de memória.

3. **Porta de Saída (Output Gate):** Controla a saída da informação da célula de memória para a camada de saída da rede.

Essas portas são ajustadas durante o treinamento da rede para aprender a manter ou descartar informações com base nos dados de entrada e nas tarefas específicas.

As LSTMs têm sido amplamente utilizadas em tarefas relacionadas ao processamento de linguagem natural (PLN), reconhecimento de fala, tradução automática e diversas outras aplicações onde a modelagem de dependências temporais de longo prazo é essencial.

## DNN

DNN (Deep Neural Network) refere-se a uma categoria de redes neurais artificiais que consistem em múltiplas camadas. Uma DNN é caracterizada por sua profundidade, o que significa que ela possui várias camadas de neurônios interconectados. As DNNs são frequentemente usadas para tarefas complexas de aprendizado de máquina, como reconhecimento de padrões, classificação, regressão e outras tarefas de modelagem.

Cada camada de uma DNN é composta por um conjunto de neurônios ou unidades, e cada neurônio em uma camada está conectado a todos os neurônios na camada seguinte. As camadas em uma DNN podem ser divididas em três tipos principais:

1. **Camada de Entrada (Input Layer):** Recebe os dados de entrada e transmite para a camada seguinte.

2. **Camadas Ocultas (Hidden Layers):** São as camadas intermédias entre a camada de entrada e a camada de saída. Estas camadas realizam transformações complexas nos dados de entrada.

3. **Camada de Saída (Output Layer):** Produz a saída final da rede após processar os dados através das camadas ocultas.

O termo "profundo" em DNN se refere à presença de várias camadas ocultas, permitindo que o modelo aprenda representações hierárquicas e complexas dos dados de entrada.

As DNNs têm sido aplicadas com sucesso em diversas áreas, incluindo visão computacional, processamento de linguagem natural, reconhecimento de voz, entre outros. Quando uma DNN possui muitas camadas (um grande número de neurônios), pode ser referida como uma "rede neural profunda" ou "deep learning". O treinamento de DNNs geralmente envolve técnicas como retropropagação (backpropagation) para ajustar os pesos das conexões entre os neurônios e otimizar o desempenho da rede em uma tarefa específica.

## BRNN

BRNN geralmente se refere a Bidirectional Recurrent Neural Network, ou Redes Neurais Recorrentes Bidirecionais em português. É um tipo de arquitetura de rede neural recorrente (RNN) que processa a entrada nos dois sentidos: do passado para o futuro (normalmente chamado de "forward") e do futuro para o passado (normalmente chamado de "backward").

Em uma BRNN, a informação é passada através da rede em ambas as direções, resultando em representações mais ricas e contextuais para cada ponto no tempo. Isso pode ser particularmente útil em tarefas onde a compreensão do contexto global é importante, como no processamento de linguagem natural.

A estrutura básica de uma BRNN consiste em duas partes principais:

1. **Camada Forward (ou "Forward RNN"):** Processa a sequência de entrada da esquerda para a direita.

2. **Camada Backward (ou "Backward RNN"):** Processa a sequência de entrada da direita para a esquerda.

As saídas dessas duas camadas são geralmente combinadas, por exemplo, concatenando-as ou tirando uma média, para formar a saída final da BRNN. Essa abordagem bidirecional ajuda a capturar padrões de dependências temporais em ambas as direções, melhorando a capacidade da rede de entender o contexto global.


---

## Dificuldades de cada um

Cada uma das arquiteturas mencionadas (LSTM, DNN e BRNN) possui desafios específicos associados ao seu uso em problemas de aprendizado de máquina. Abaixo estão alguns dos principais problemas relacionados a cada uma dessas arquiteturas:

### LSTM (Long Short-Term Memory):

1. **Dificuldade no Treinamento:**
   - LSTMs podem ser mais complexas e mais difíceis de treinar em comparação com redes neurais mais simples devido ao maior número de parâmetros e à necessidade de ajuste fino.

2. **Overfitting:**
   - Assim como em outras redes neurais, LSTMs podem estar suscetíveis ao overfitting, especialmente quando o conjunto de dados é pequeno ou quando os hiperparâmetros não são ajustados adequadamente.

3. **Ajuste de Hiperparâmetros:**
   - Encontrar os valores ideais para os hiperparâmetros, como taxas de aprendizado e tamanhos de lote, pode ser desafiador e exigir experimentação.

### DNN (Deep Neural Network):

1. **Vanishing/Exploding Gradient:**
   - Em DNNs profundas, o gradiente pode diminuir significativamente (vanishing gradient) ou aumentar exponencialmente (exploding gradient) à medida que se propaga para trás durante o treinamento, dificultando a aprendizagem eficaz.

2. **Complexidade Computacional:**
   - DNNs profundas podem exigir uma quantidade significativa de recursos computacionais para treinamento, tornando-as caras em termos de tempo e hardware.

3. **Interpretabilidade:**
   - Modelos DNNs podem ser considerados "caixas-pretas" devido à sua complexidade, o que torna difícil entender como e por que uma decisão específica é tomada.

### BRNN (Bidirectional Recurrent Neural Network):

1. **Complexidade Computacional Adicional:**
   - A bidirecionalidade aumenta a complexidade computacional e pode tornar o treinamento mais demorado.

2. **Ajuste do Número de Camadas e Unidades:**
   - Determinar o número ideal de camadas e unidades em cada direção pode ser desafiador e requer ajuste fino.

3. **Necessidade de Dados Bidirecionais:**
   - Em alguns casos, pode ser difícil obter dados bidirecionais para treinamento eficaz.

Lembre-se de que a escolha entre essas arquiteturas depende da natureza específica do problema e dos dados disponíveis. Para lidar com esses problemas, é comum realizar experimentação, ajuste de hiperparâmetros e, em alguns casos, considerar arquiteturas mais recentes ou modificações específicas para abordar desafios particulares.
