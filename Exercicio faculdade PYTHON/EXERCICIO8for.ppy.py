import os
import sqlite3
os.chdir(r'C:\Users\paulo\Desktop\Exercicio faculdade PYTHON')

Soma = 0
cnt = 0
arq = open("Inteiros.txt","r")
I = arq.readlines()



for O in I:
    Num = int(O)
    Soma = Soma + Num
    cnt = cnt + 1
    print ("Alguns Elementos {0} = {1}".format (cnt,Num))
    S = arq.readlines()

arq.close()
print("\nSoma={0}".format(Soma))