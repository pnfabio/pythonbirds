class Pessoa:
    def __init__(self, *filhos, nome=None, idade=40):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    heitor = Pessoa(nome='Heitor')
    fran = Pessoa(heitor, nome='Fran')
    print(Pessoa.cumprimentar(fran))
    print(fran.cumprimentar())
    print(id(fran))
    print(fran.nome)
    print(fran.idade)
    for filho in fran.filhos:
        print(filho.nome)
