import os

os.chdir(r'C:\Users\paulo\Desktop\Exercicio faculdade PYTHON')

data = open("documentobd.txt","w")

write1 = (input("Tudo bem? "))

if write1 == ("Sim"):  
    data.write("Beleza, Bom dia!\n")
    data = open ("documentobd.txt","r")
    linha = data.readline()
    print(linha)
    data.close


else:
    data.write ("Acontece, bola pra frente e bora!\n")
    data.close()
    data = open ("documentobd.txt","r")
    linha = data.readline()
    print(linha)
    data.close




