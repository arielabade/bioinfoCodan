
- Existe alguma forma de transformar as HMMs em RNNs?
- Existe alguma forma de reaproveitar os datasets?
- Como você imagine a modelagem das RNNs nesse contexto? O que eu pensei foi codificar cada trinca de 3 códons como uma sequência de binários, como acontece em um artigo, e prever a próxima sequência de 3 códons a partir disso. No caso, precisariam de duas "implementações" uma que identificasse as trincas inicias de começo e de fim, e outra implementação que previsse os códons no meio.

![[codons.jpg]]

![image][https://github.com/arielabade/bioinfoCodan/blob/main/bioinfo-codan/codons.jpg]
![Texto alternativo da imagem](caminho/para/a/imagem.jpg)
- Existe alguma forma de pegar os pesos relacionados as HMMs e alocar nas RNNs?
- Existe algum framework para implementar isso? (torch, pythorch, tensorflw)
- Como seria a melhor aboordagem desse problema utilizando RNNs?
- Como criar uma função de mapeamento que lide com o problema de duplicação?

