import random
class Minha_excecao(Exception): pass

class JogoAdivinhacao:
    def __init__(self):
        self.numero_secreto = None

    def gerar_numero(self):
        self.numero_secreto = random.randint(0, 10)

    def jogar(self):
        self.gerar_numero()

        while True:
            try:
                palpite = int(input("Adivinhe o número (entre 0 e 10): "))
                if palpite == self.numero_secreto:
                    if random.random() < 0.1:
                        self.gerar_numero()
                        raise Minha_excecao("Você tem poderes psíquicos!")
                    else:
                        print("Parabéns, você acertou!")
                        break
            except ValueError:
                print("Digite um número inteiro válido.")



if __name__ == "__main__":
    jogo = JogoAdivinhacao()
    jogo.jogar()