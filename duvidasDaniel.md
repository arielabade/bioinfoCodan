# Codan

# Github
- [x] Por que nas minhas pastas de base de dados aparece uma seta -> e eu não consigo configurar elas depois? R = por que as pastas da base de dados sao muito grandes

# Databases
- [ ] Quais são as melhores práticas montando uma base de daods utilizada no codan? R = elucidado na reunião  20/02

# Machine Learning
- [ ] Você acha que é viável mexer no HMM, caso ninguém pegue o plano de trabalho?
- [ ] Pensei em usar a saída do HMM como possíveis entradas no RNN e ver quais são os resultados, o que o senhor acha? Ou talvez replicar o executável do CodAn em forma de RNN para juntar ambos os resultados e conseguir uma melhor acurácia seja uma opção melhor

# Scientific Writing
- [ ] Existe alguma diferença de reconhecimento da IC departamental pra IC do Copes?
# Sistema Operacional

- [x] Por que o sistema operacional não está reconhecendo os executáveis do Codan? R = por que está no caminho absoluto, e não no relativo
- [x] Por que o sistema operacional não está reconhecendo os downloads necessários das bases de dados? R = por que é necessário montar uma base de dados blast antes de rodar o CodAN
- [x] Como definir os caminhos absolutos para que a execução do CodAn seja mais fácil?
R:


pegar uma pasta e separar

.../transcripts # isso sobre pra raiz
transcripts/drosophila -> absolut path
evite caminho absoluto -> use apenas relativo

pra n bagunçar a estrutura, usar .. para ir pra pasta anterior

criar constante do makefile = caminho do transcripts.


- [ ] 
