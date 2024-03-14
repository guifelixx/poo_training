#Mantendo estados dentro da classe
class Entrada:
    def __init__(self, nome, entrando=False):
        self.nome = nome
        self.entrando = entrando

    def entrar(self):
        if self.entrando:
            print(f'{self.nome} já está logado...')

        print(f'{self.nome} está logado...')
        self.entrando = True

    def sair(self):
        if not self.entrando:
            print(f'{self.nome} está deslogado...')
            return
#continuaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa