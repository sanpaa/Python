#Exemplo1

arquivo = open("relatorio.txt",'r')
linha = arquivo.readlines()

while (linha != ""):
    print (linha)   
    linha = arquivo.readlines()

arquivo = arquivo.close()


#Exemplo2

arquivo = open("relatorio.txt",'r')
linhas = arquivo.readlines()

cont = 0
while (cont<len(linhas)):
    print(linhas[cont])
    cont+=1