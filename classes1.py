#Just a some examples of classes (POO) in Python for me

class Carro: #Iniciando a classe Carro
    def __init__(self, nome): 
        # Método especial de inicialização (construtor)
        self.nome = nome  # Atributo da classe Carro

    def acelerar(self): 
        # Método para acelerar o carro
        print(f'{self.nome} está acelerando...')

# Instanciando objetos da classe Carro
fusca = Carro('Fusca')  # Objeto do tipo Carro com nome 'Fusca'
fusca.acelerar()  # Chamada do método acelerar para o fusca

celta = Carro(nome='Celta')  # Outro objeto do tipo Carro com nome 'Celta'
celta.acelerar()  # Chamada do método acelerar para o celta


class Roupa: #Iniciando a classe Roupa
    def __init__(self, nome, cor, tamanho):
        # Método especial de inicialização (construtor)
        self.nome = nome  # Atributo da classe Roupa
        self.cor = cor  # Outro atributo da classe Roupa
        self.tamanho = tamanho  # Mais um atributo da classe Roupa

    def imprimir_dados(self):
        # Método para imprimir os dados da roupa
        print(f'Nome: {self.nome}')
        print(f'Cor: {self.cor}')
        print(f'Tamanho: {self.tamanho}')

# Instanciando objetos da classe Roupa
camiseta = Roupa(nome='Camiseta', cor='amarelo', tamanho= 'GG')  # Objeto do tipo Roupa
camiseta.imprimir_dados()  # Chamada do método imprimir_dados para a camiseta

calca = Roupa(nome='Calça',cor='preta', tamanho= '38')  # Outro objeto do tipo Roupa
calca.imprimir_dados()  # Chamada do método imprimir_dados para a calça

cueca = Roupa(nome='Cueca', cor='rosa', tamanho= 'M')  # Mais um objeto do tipo Roupa
cueca.imprimir_dados()  # Chamada do método imprimir_dados para a cueca
