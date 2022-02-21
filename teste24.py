class Pessoa:
    nome = None
    idade = 20

    def imprimirNome(self):
        print(self.nome)

    def imprimiridade(self):
        print(self.idade)

    def colocaridade(self,num):
        self.idade = num

    def colocarnome(self,nom):
        self.nome = nom

emerson = Pessoa()
emerson.colocaridade(30)
emerson.colocarnome("Emerson Ferrovia Costa")

emerson.imprimirNome()
emerson.imprimiridade()