import os
import sqlite3
os.chdir(r'C:\Users\paulo\Desktop\Exercicio faculdade PYTHON')

Soma = 0
cnt = 0
arq = open("Inteiros.txt","r")
I = arq.readline()



while I!="":
    Num = int(I)
    Soma = Soma + Num
    cnt = cnt + 1
    print ("Alguns Elementos {0} = {1}".format (cnt,Num))
    S = arq.readlines()

arq.close()
print("\n Soma={0}".format(Soma))