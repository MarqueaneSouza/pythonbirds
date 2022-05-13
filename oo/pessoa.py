class Pessoa:
    def __init__(self, *filhos, nome=None, idade = 35): #ALT + ENTER inclui o parâmetro (atributo) na linha abaixo do método.
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__': #crio a 'main' para nossos testes
    marqueane = Pessoa(nome='Marqueane')
    luciano = Pessoa(marqueane, nome='Luciano')
    print(Pessoa.cumprimentar(luciano)) #para executar o método eu peço o cumprimentar e passo o 'p'.
    print(id(luciano))
    print(luciano.cumprimentar()) #executo o método utilizando o próprio objeto. E nesse caso, eu não preciso passar o objeto novamente.
    print(luciano.nome)
    print(luciano.idade)

    for filho in luciano.filhos:
        print(filho.nome)



