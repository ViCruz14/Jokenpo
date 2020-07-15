import random
from time import sleep
import emoji


class Jokenpo:
    def __init__(self, nome, emoticon, ganha_de):
        self.nome = nome
        self.emoticon = emoticon
        self.ganha_de = ganha_de


def escolhas():
    epc = random.choice(opcoes)
    ej = opcoes[int(input(f"{'=' * 30}\n"    
                          "Bem vindo ao famoso Jokenpô!\n"
                          "Por favor, escolha sua jogada:\n"
                          "\n"
                          "      | 1 - Pedra   |\n"  
                          "      | 2 - Papel   |\n" 
                          "      | 3 - Tesoura |\n"
                          f"{'~' * 30}\n")) - 1]
    return epc, ej


def definir_vencedor(epc, ej):
    if epc == ej:
        return '\nEmpate, ninguém pontuou'
    elif epc.nome != ej.ganha_de:
        placar['Computador'] += 1
        return '\nO Computador venceu! Mais sorte na próxima'
    else:
        placar['Jogador'] += 1
        return '\nParabéns! Você ganhou!!'


Pedra = Jokenpo('Pedra', emoji.emojize(':mountain:'), 'Tesoura')
Papel = Jokenpo('Papel', emoji.emojize(':page_facing_up:'), 'Pedra')
Tesoura = Jokenpo('Tesoura', emoji.emojize(':scissors:'), 'Papel')
opcoes = [Pedra, Papel, Tesoura]
continuar = ''
placar = {'Jogador': 0, 'Computador': 0}

while continuar != 'I':
    try:
        escolha_pc, escolha_jogador = escolhas()

    except ValueError:
        print('Por favor, digite apenas o número da opção desejada')
        pass

    except IndexError:
        print('Escolha uma opção de 1 a 3')
        pass

    else:
        print("JO")
        sleep(1)
        print('KEN')
        sleep(1)
        print('PÔ!!!')

        print(f"Você escolheu: {escolha_jogador.nome}\n" 
              f"O computador escolheu... {escolha_pc.nome}!\n"
              f"          {escolha_jogador.emoticon} x {escolha_pc.emoticon}")

        sleep(1.5)

        print(definir_vencedor(escolha_pc, escolha_jogador))

        print(f"{'-' * 30}\n" 
              f"{'PLACAR':^30}\n"
              f"Jogador{placar['Jogador']:>23}\n"
              f"Computador{placar['Computador']:>20}\n"
              f"{'-' * 30}\n")

        continuar = str(input("Vamo jogar mais uma?\n"
                              "Se quiser interromper digite I.\n"
                              "Se não, é só apertar outra tecla\n")).upper().strip()
