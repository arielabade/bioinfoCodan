## Prompts

- Quais ferramentas das bibliotecas específicas foram usadas na função x?
- Nesse pedaço de código, de ondde que veio o argumento?
- Existe alguma relação na organização do arquivo com a predição em si?

----
### O que são ORF's?

R:

ORFs (Open Reading Frames) são regiões em uma sequência de DNA ou RNA que têm o potencial de serem traduzidas em proteínas. Uma ORF é definida como uma sequência contígua de nucleotídeos que começa com um códon de iniciação (geralmente AUG, que codifica para o aminoácido metionina) e termina com um códon de terminação (UAA, UAG ou UGA). Entre esses códons de iniciação e terminação, a sequência de nucleotídeos é lida em grupos de três (tripletos), chamados códons, e cada códon codifica um aminoácido específico.

Durante a transcrição do DNA para RNA e subsequente tradução do RNA para proteína, uma ORF funcional pode ser identificada e utilizada para produzir uma proteína específica. No entanto, nem todas as ORFs em um genoma são necessariamente traduzidas em proteínas funcionais. Algumas ORFs podem representar sequências não codificantes, enquanto outras podem ter funções regulatórias ou desconhecidas.

A identificação e análise de ORFs são comuns em estudos de genômica e bioinformática, onde os pesquisadores buscam entender a estrutura genômica e a função potencial de diferentes regiões de DNA ou RNA. Essas análises muitas vezes envolvem o uso de ferramentas computacionais para identificar ORFs em sequências genômicas e predizer as possíveis proteínas que podem ser traduzidas a partir dessas sequências.

------

### Sobre os formatos de saída e entrada:

- What are CDS and UTR?

1) CDS (Coding DNA Sequence):

The Coding DNA Sequence, or CDS, is the region of DNA that encodes the information necessary to build a functional protein. Proteins are essential molecules in cells that perform various functions, and their structure is determined by the sequence of amino acids, which is in turn specified by the sequence of nucleotides in the CDS.
The CDS is typically located between the start codon (initiation codon) and the stop codon in a gene. The start codon signals the beginning of the protein-coding sequence, and the stop codon marks the end.

2) UTR (Untranslated Region):

The Untranslated Region, or UTR, refers to the portions of a messenger RNA (mRNA) molecule that are not translated into protein. These regions are found at both the 5' (5 prime) and 3' (3 prime) ends of the mRNA.
The 5' UTR is located upstream of the start codon and is involved in the regulation of translation initiation. It contains elements that interact with cellular machinery to control when and how often translation of the mRNA into protein occurs.
The 3' UTR is located downstream of the stop codon and contains sequences that are important for mRNA stability, localization, and post-transcriptional regulation. It also plays a role in the regulation of mRNA degradation.
In summary, the CDS is the coding region of DNA that specifies the amino acid sequence of a protein, while the UTRs are non-coding regions found at the ends of mRNA molecules that play roles in the regulation of gene expression.


#### Sobre a avaliação de éxons e íntrons no DNA:

3utr_sequences.fasta e 5utr_sequences.fasta:

Esses arquivos provavelmente contêm sequências das regiões 3'UTR (região não traduzida do 3') e 5'UTR (região não traduzida do 5') de mRNA, respectivamente.
Sequências nessas regiões geralmente não codificam proteínas, mas são importantes para a regulação da expressão gênica.
Você pode usar ferramentas de bioinformática para predizer ORFs (open reading frames) nessas sequências e determinar se elas têm o potencial de codificar proteínas.
ORF_sequences.fasta:

Este arquivo provavelmente contém sequências de open reading frames (ORFs), que são regiões de DNA com o potencial de codificar proteínas.
Você pode usar ferramentas como BLAST ou GeneMark para analisar essas sequências e identificar regiões codificadoras.
PEP_sequences.fa:

Este arquivo provavelmente contém sequências de aminoácidos, que são as sequências de proteínas traduzidas a partir das sequências codificadoras de DNA (CDS).
Pode ser útil comparar essas sequências de proteínas com bancos de dados de proteínas conhecidas usando ferramentas como BLAST para validar se são codificadoras.
annotation.gtf:

Arquivos de anotação GTF (Gene Transfer Format) geralmente contêm informações sobre a estrutura gênica, incluindo a localização de exons, introns e outras características.
Pode conter informações sobre regiões codificadoras e não codificadoras.
Analise as entradas desse arquivo para obter informações sobre a estrutura dos genes, incluindo as regiões codificadoras.


#### Tools

- Gene Data Viz: https://www.sanger.ac.uk/tool/artemis//

### Sobre o passo a passo do GPT

### Roadmap:

#### 1. **Compreensão do Problema:**

   - Leia a documentação (se existir) e o código para obter uma compreensão geral do problema que os códigos estão tentando resolver.
   - Pesquise sobre a identificação de ORFs e a predição de características genéticas usando modelos HMM.

#### 2. **Compreensão do Código Python:**
   - Analise o código Python linha por linha para entender como ele identifica ORFs.
   - Faça anotações sobre a lógica do algoritmo, estruturas de dados usadas e qualquer outra informação relevante.
   - Execute o código em algumas sequências de teste para observar seu comportamento.

#### 3. **Compreensão do Código Perl:**
   - Faça o mesmo para o código Perl. Analise linha por linha, entenda as dependências e estruturas do código.
   - Compreenda como os modelos HMM são utilizados para fazer previsões nas sequências de DNA.

#### 4. **Avaliação de Desempenho Atual:**
   - Identifique as métricas de desempenho utilizadas nos códigos existentes.
   - Execute os códigos em conjuntos de dados de teste e avalie as métricas de desempenho.
   - Compreenda os pontos fortes e fracos dos códigos em termos de eficácia e eficiência.

#### 5. **Pesquisa sobre Melhorias com Aprendizado de Máquina:**
   - Pesquise sobre abordagens de aprendizado de máquina aplicadas à bioinformática, especialmente na identificação de características genéticas.
   - Considere técnicas como redes neurais, modelos de sequência, ou outras abordagens ML/DL para análise de sequências de DNA.

#### 6. **Identificação de Possíveis Pontos de Melhoria:**
   - Identifique áreas nos códigos onde técnicas de aprendizado de máquina podem ser incorporadas para melhorar as métricas de desempenho.
   - Considere como modelos mais avançados podem ser integrados ou adaptados para resolver o problema de maneira mais eficaz.

#### 7. **Implementação de Melhorias:**
   - Implemente pequenas melhorias incrementalmente para evitar grandes alterações simultâneas.
   - Utilize bibliotecas e frameworks de aprendizado de máquina, como scikit-learn para Python, se necessário.

#### 8. **Avaliação de Desempenho Melhorado:**
   - Execute os códigos aprimorados em conjuntos de dados de teste.
   - Compare as métricas de desempenho com as versões originais.
   - Certifique-se de que as alterações não introduzem novos problemas e são estatisticamente significativas.

#### 9. **Documentação e Compartilhamento:**
   - Documente claramente as alterações feitas nos códigos.
   - Compartilhe os resultados, métricas de desempenho e abordagens utilizadas.

#### 10. **Iteração e Feedback:**
   - Este é um processo iterativo. Esteja preparado para ajustar sua abordagem com base nos resultados e feedbacks obtidos.
   - Consulte colegas ou comunidades relevantes para obter insights adicionais.

Lembre-se, a aplicação de aprendizado de máquina a problemas específicos pode exigir ajustes cuidadosos para garantir que os modelos sejam treinados e avaliados corretamente. O entendimento profundo do domínio biológico é fundamental.


