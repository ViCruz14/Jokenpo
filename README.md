# Jokenpo
Jogo de Pedra, Papel, Tesoura modelo jogador x computador

As bibliotecas utilizadas são: random, time e emoji. Tenha certeza que elas já estão instaladas antes de rodar

O programa funciona pela seguinte lógica: 
os objetos Pedra, Papel e Tesoura tem, além de nome e emoji, o atributo 'ganha_de' que simboliza de qual objeto eles ganham. 
Uma vez que o computador escolheu sua jogada pelo método choice, e o jogador digitou sua opção no input (ambos pela função escolha) o programa automaticamente considera empate se os objetos forem iguais
.Caso não, o programa compara o atributo 'ganha_de'da jogada do jogador com a jogada do adiversário. Se forem iguais, isso significa que o jogador ganhou. Se não, o jogador perdeu (função definir_ganhador)

O placar é mostrado e o jogador tem a opção de continuar ou parar de jogar

O arquivo de teste, em que foi utilizado o framework unittest, verifica se em todas as possibilidades o programa principal está acertando o resultado

a função try e except evita que o jogador escolha alternativas erradas


