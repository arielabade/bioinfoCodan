
- Existe alguma forma de transformar as HMMs em RNNs?
- Existe alguma forma de reaproveitar os datasets?
- Como você imagine a modelagem das RNNs nesse contexto? O que eu pensei foi codificar cada trinca de 3 códons como uma sequência de binários, como acontece em um artigo, e prever a próxima sequência de 3 códons a partir disso. No caso, precisariam de duas "implementações" uma que identificasse as trincas inicias de começo e de fim, e outra implementação que previsse os códons no meio.

![[codons.jpg]]

![image][bioinfo-codan/codons.jpg]
![Texto alternativo da imagem](caminho/para/a/imagem.jpg)
- Existe alguma forma de pegar os pesos relacionados as HMMs e alocar nas RNNs?
- Existe algum framework para implementar isso? (torch, pythorch, tensorflw)
- Como seria a melhor aboordagem desse problema utilizando RNNs?
- Como criar uma função de mapeamento que lide com o problema de duplicação?

### Critérios de Classificação

Os critérios utilizados para classificar exons e introns são baseados principalmente na sua estrutura e função dentro de um gene. Aqui estão os principais critérios:

1. **Localização no Gene:** Exons são as partes do gene que codificam proteínas, enquanto os introns são sequências não codificadoras. Exons estão presentes na sequência final de mRNA funcional, enquanto os introns são removidos durante o processamento do RNA.

2. **Tamanho e Estrutura:** Exons tendem a ser menores e mais uniformes em tamanho, enquanto introns podem variar em comprimento significativamente e geralmente contêm sequências repetitivas.

3. **Conservação Evolutiva:** Exons são frequentemente altamente conservados ao longo da evolução, especialmente em regiões que codificam partes importantes de proteínas. Introns, por outro lado, podem ser menos conservados e podem conter sequências regulatórias ou elementos móveis.

4. **Sequências de Sinais:** Existem sequências específicas de sinais que marcam os limites entre exons e introns durante o processamento do RNA. Por exemplo, há sequências de splicing que indicam onde o RNA deve ser cortado para remover os introns.

5. **Função Biológica:** Exons codificam partes das proteínas que desempenham funções específicas no organismo, enquanto os introns podem ter papéis regulatórios no processamento do RNA ou conter sequências que são transcritas, mas não traduzidas em proteínas.

Esses critérios são fundamentais para entender a estrutura e a função dos genes e são essenciais para processos como a transcrição e a tradução da informação genética em proteínas funcionais.