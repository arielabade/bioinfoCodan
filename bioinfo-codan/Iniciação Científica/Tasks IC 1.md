


## Work


#### Prioridade 1

1. [ ] Fazer makefile do CodAn (evitar ficar gastanddo tempo escrevendo código, rever o vídeo dos makefile com as entradas, saídas etc)
2. [ ] Entender os formatos de entrada e sa´´iddas de dados
3. [ ] Fazer um git copy no código do CodAn para entender como ele funciona e colocar meus comentários nele
4. [ ] Agregar o roadmap e aprendizado de máquina do cara que é engenherio de machine learning aqui nesse curso
#### Prioridade 2

1. [ ] Estudar todas as funções em python do Codan para entender entradas e saídas
#### Prioridade 3

1. [ ] Entender como funciona o aprendizado de máquina utilizando bioperl
2. [ ] Entender como funciona o processamento parelelo por trás do perl
3. [ ] Me familiarizar com a sintaxe do perl

Links úteis:


#### Processamento Paralelo e Concorrente

3. **Multitarefa:**
   - `MCE` (Many-Core Engine): [Documentação MCE](https://metacpan.org/pod/MCE)
   - `MCE::Mutex`: [Documentação MCE::Mutex](https://metacpan.org/pod/MCE::Mutex)

4. **Outras:**
   - `IPC::Open2`: [Documentação IPC::Open2](https://metacpan.org/pod/IPC::Open2)
   - `Time::HiRes qw(...)`: [Documentação Time::HiRes](https://perldoc.perl.org/Time/HiRes.html)

### Perl

https://perldoc.perl.org/

Certamente! Aqui estão os links para a documentação das bibliotecas Perl mencionadas no código:

1. **Básicas:**
   - `strict`: [Documentação strict](https://perldoc.perl.org/strict.html)
   - `warnings`: [Documentação warnings](https://perldoc.perl.org/warnings.html)
   - `Getopt::Long`: [Documentação Getopt::Long](https://perldoc.perl.org/Getopt/Long.html)
   - `Cwd 'abs_path'`: [Documentação Cwd](https://perldoc.perl.org/Cwd.html)
   - `File::Temp qw(tempfile)`: [Documentação File::Temp](https://perldoc.perl.org/File/Temp.html)
   - `File::Basename`: [Documentação File::Basename](https://perldoc.perl.org/File/Basename.html)
   - `Data::Dumper`: [Documentação Data::Dumper](https://perldoc.perl.org/Data/Dumper.html)

2. **Bioinformática:**
   - `Bio::SeqIO`: [Documentação Bio::SeqIO](https://metacpan.org/pod/Bio::SeqIO)
   - `Bio::DB::Fasta`: [Documentação Bio::DB::Fasta](https://metacpan.org/pod/Bio::DB::Fasta)


Você pode encontrar informações detalhadas sobre o uso de cada uma dessas bibliotecas nos links fornecidos.
### Python

Certamente! Aqui estão os links para a documentação das bibliotecas mencionadas na versão base do Python 3:

1. **Biopython:**
   - Documentação principal: [Biopython Documentation](https://biopython.org/wiki/Documentation)
   - SeqIO: [Biopython SeqIO Documentation](https://biopython.org/wiki/SeqIO)
   - Seq: [Biopython Seq Documentation](https://biopython.org/wiki/Seq)

2. **Bibliotecas Python padrão:**
   - argparse: [argparse - Parser for command-line options, arguments, and sub-commands](https://docs.python.org/3/library/argparse.html) - `argparse` é a versão moderna de `optparse` e é recomendada para versões mais recentes do Python.
   - datetime: [datetime - Basic date and time types](https://docs.python.org/3/library/datetime.html)
   - subprocess: [subprocess - Subprocess management](https://docs.python.org/3/library/subprocess.html)
   - os: [os - Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html)

Certifique-se de consultar a documentação apropriada, dependendo da versão específica do Python 3 que você está usando.
#### ChatGPT


Entender e melhorar códigos existentes, especialmente quando se trata de bioinformática e análise de sequências de DNA, é uma tarefa desafiadora, mas pode ser muito recompensadora. Aqui está um roadmap geral para ajudá-lo a entender e potencialmente melhorar esses códigos:

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


#### Codan



