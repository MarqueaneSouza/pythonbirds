class Pessoa:
    def __init__(self, nome=None, idade = 35): #ALT + ENTER inclui o parâmetro (atributo) na linha abaixo do método.
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__': #crio a 'main' para nossos testes
    p = Pessoa('Luciano')
    print(Pessoa.cumprimentar(p)) #para executar o método eu peço o cumprimentar e passo o 'p'.
    print(id(p))
    print(p.cumprimentar()) #executo o método utilizando o próprio objeto. E nesse caso, eu não preciso passar o objeto novamente.
    print(p.nome)
    p.nome = "Renzo" #alterando o nome
    print(p.nome)

