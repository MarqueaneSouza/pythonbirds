class Pessoa:
    def __init__(self, *filhos, nome=None, idade = 35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__':
    marqueane = Pessoa(nome='Marqueane')
    luciano = Pessoa(marqueane, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)

    luciano.sobrenome = 'Ramalho'
    del luciano.filhos
    print(luciano.sobrenome)
    print(luciano.__dict__)
    print(marqueane.__dict__)