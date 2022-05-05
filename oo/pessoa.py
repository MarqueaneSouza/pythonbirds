class Pessoa:
    def cumprimentar(self):
        return f'Olá {id(self)}'
if __name__ == '__main__': #crio a 'main' para nossos testes
    p = Pessoa()
    print(Pessoa.cumprimentar(p)) #para executar o método eu peço o cumprimentar e passo o 'p'.
    print(id(p))
    print(p.cumprimentar()) #executo o método utilizando o próprio objeto. E nesse caso, eu não preciso passar o objeto novamente.

