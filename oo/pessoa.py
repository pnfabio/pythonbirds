class Pessoa:
    olhos = 2 #atributos de Classe (default)

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
    fran.sobrenome = 'Nascimento'
    del fran.filhos
    fran.olhos = 1
    del fran.olhos
    Pessoa.olhos = 3
    print(fran.__dict__)
    print(heitor.__dict__)
    print(Pessoa.olhos)
    print(fran.olhos)
    print(id(fran.olhos), id(heitor.olhos), id(Pessoa.olhos))

