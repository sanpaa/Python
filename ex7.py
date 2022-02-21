import os


os.chdir(r'C:\Users\paulo\Desktop\Exercicio faculdade PYTHON')

data = open("documentoreal.txt","a")
write1 = 1
while (write1 != 0):
    write1 = input("Digite um numero com 3 casas decimais:")
    if write1 == "0":
        break
    elif len(write1) == 5:
        float(write1)
        if float(write1):
            data.writelines(write1+"\n")
            data.close


#dar 0 pra escrever.