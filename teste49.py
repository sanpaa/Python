import sqlite3
import os
os.chdir(r'C:\Users\paulo\Desktop\Faculdade\Lab.Desenvolv')

arq = open ("PesoAltura.txt","r")
L = arq.readlines()
arq.close()
print("Linhas do arquivo")
sql = """update cadastro set peso = ?,altura = ?
        where codigo = ?"""
conector = sqlite3.connect("academia.db")
cursor = conector.cursor()
for s in L:
    d = s.rstrip()
    d = s.split(";")
    cursor.execute(sql,(d[1],d[2],d[0]))
    conector.commit()
    print(d,"...processado")
cursor.close()
conector.close()
print("Banco de dados atualizado com sucesso! ")
print("Fim do programa")
