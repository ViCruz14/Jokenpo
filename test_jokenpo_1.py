from jokenpo_1 import *
import unittest


class TestJokenpo(unittest.TestCase):
    def test_definir_jogador(self):
        self.assertEqual(definir_vencedor(Pedra, Pedra), '\nEmpate, ninguém pontuou')
        self.assertEqual(definir_vencedor(Papel, Papel), '\nEmpate, ninguém pontuou')
        self.assertEqual(definir_vencedor(Tesoura, Tesoura), '\nEmpate, ninguém pontuou')
        self.assertEqual(definir_vencedor(Pedra, Tesoura), '\nO Computador venceu! Mais sorte na próxima')
        self.assertEqual(definir_vencedor(Papel, Pedra), '\nO Computador venceu! Mais sorte na próxima')
        self.assertEqual(definir_vencedor(Tesoura, Papel), '\nO Computador venceu! Mais sorte na próxima')
        self.assertEqual(definir_vencedor(Pedra, Papel), '\nParabéns! Você ganhou!!')
        self.assertEqual(definir_vencedor(Papel, Tesoura), '\nParabéns! Você ganhou!!')
        self.assertEqual(definir_vencedor(Tesoura, Pedra), '\nParabéns! Você ganhou!!')


if __name__ == '__main__':
    unittest.main()
