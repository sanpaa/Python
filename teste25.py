class Pessoa:
    nome = None
    idade = None

    def __init__ (self,n,i):
        self.nome = n
        self.idade = i

    def imprimirNome(self):
        print(self.nome)

    def imprimiridade(self):
        print(self.idade)

    def colocaridade(self,num):
        self.idade = num

    def colocarnome(self,nom):
        self.nome = nom

emerson = Pessoa("Emerson Ferrovia Costa",30)

emerson.imprimirNome()
emerson.imprimiridade()