## How hidden markov models works?

HMM's são muito utilizadas quando se trata de processamento de linguagem natural, devido ao fato de que elas podem prever letras "ocultas" em palavras.

Da mesma forma ocorre com o CodAn. Ele consegue prever zonas codificadoras, que são "ocultas" baseadas nas trincas de DNA.

"Vamos supor que um lugar vende 3 lanches: hamburger, pizza e cachorro quente. Mas todos os dias da semana, ele vende apenas UM tipo de lanche. A venda desse tipo de lanche é baseado APENAS no lanche do dia anterior."

"The future state depends only of the state BEFORE. Not the complete sequence before the end state."

Ex: Existe uma chance de 60% de amanhã ser dia de pizza. Portanto, hoje é dia de hamburger.  **É baseado em um sistema de pesos.**

Ex: Existe uma chance de 20% de que amanhã eles vão servir hamburger, tendo em vista que hoje eles já serviram hamburger.


## Recurrence, Irreducibility, Classes

Irreducible chains are the ones that you can get to any state on the chain by passing through other states.

Reducebles chains are the opposite of reducible chains. So, you can divide the reducible chain is smaller pieces and turn them into irreducible.

Classes are the isolated states after they are irreducible.

### Higher Order Transition Matrix and Equilibrium State

https://www.youtube.com/watch?v=Zo3ieESzr4E&list=PLM8wYQRetTxBkdvBtz-gw8b9lcVkdXQKV&index=3

## Passo a passo para o algoritmo

1) Rode ele em uma sequência aleatória
2) Qual a equação estacionária de ocorrência? (É possível obter isso através de um cálculo com a matriz de transição. Você vai descobrir o resultado correto quando as entradas forem iguais as saídas.) -> precisa aprender as melhores formas de calcular a matriz de transição

OBS: vídeo que ensina a calcular = https://www.youtube.com/watch?v=i3AkTO9HLXo&list=PLM8wYQRetTxBkdvBtz-gw8b9lcVkdXQKV

3) Se os valores da equação estacionária forem 0.35, 0.21, e 0.43, qual a chance de ser dia de hamburger, pizza ou cachorro quente baseado apenas no dia anterior?

## How TOPS works?



### What are HMMs 

Hidden Markov Models (HMMs) não se enquadram diretamente nas categorias tradicionais de classificação ou regressão. Eles são mais frequentemente usados para modelar sequências de dados, onde o objetivo é entender a estrutura subjacente da sequência.

Em um HMM, você tem estados ocultos que evoluem ao longo do tempo, e esses estados emitem observações. A tarefa principal em um HMM é inferir a sequência de estados ocultos que é mais provável, dadas as observações. Portanto, HMMs são comumente usados para problemas de modelagem de sequências, como reconhecimento de padrões em sequências temporais.

Se você precisar rotular ou classificar sequências com base em padrões subjacentes, um HMM pode ser apropriado, mas é uma abordagem diferente da classificação ou regressão tradicionais. O HMM é mais adequado para problemas em que a relação entre os dados pode ser modelada como uma cadeia de estados ocultos.
