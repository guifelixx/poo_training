class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
fusca.acelerar()

celta = Carro(nome='Celta')
celta.acelerar()


class Roupa:
    def __init__(self, nome, cor, tamanho):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho

    def imprimir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Cor: {self.cor}')
        print(f'Tamanho: {self.tamanho}')

camiseta = Roupa(nome='Camiseta', cor='amarelo', tamanho= 'GG')
camiseta.imprimir_dados()
calca = Roupa(nome='Calça',cor='preta', tamanho= '38')
calca.imprimir_dados()
cueca = Roupa(nome='Cueca', cor='rosa', tamanho= 'M')
cueca.imprimir_dados()
