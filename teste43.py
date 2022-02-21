peças = {}
print ("Leitura de dados: ")
while True:
    cod = int(input("     Digite o codigo:  "))
    if cod == 0:
        break
    elif cod in peças:
        print ("A peça {} já existe no cadastro".format (cod))
        continue
    qtde = int(input("Digite a quantidade: "))
    peças[cod] = qtde

print ("Fim da leitura de dados ")

print ("Estoque de peças")

for c in peças:
    print("{1:4} unidades de peça {0}".format (c, peças[c]))
print("Fim do programa.")