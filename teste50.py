import sqlite3
import os
os.chdir(r'C:\Users\paulo\Desktop\Faculdade\Lab.Desenvolv')

print("Criação da chave primária na tabela cadastro:")
conector = sqlite3.connect("academia.db")
cursor = conector.cursor()
sql = " create table temp1 as select * from cadastro" #clona tabela
cursor.execute(sql)
sql = 'drop table cadastro' #exclui
cursor.execute(sql)

sql = """
    create table cadastro(
        codigo integer NOT NULL PRIMARY KEY, 
        nome text,
        idade integer,
        curso integer,
        dtingr date,
        peso double,
        altura double)
"""

cursor.execute(sql)

sql = """
    insert into cadastro
    (codigo,nome,idade,curso,dtingr,peso,altura)
    select codigo, nome, idade, curso, dtingr, peso, altura from temp1
"""
cursor.execute(sql)
conector.commit()
sql = "drop table temp1"
cursor.execute(sql)
cursor.close()
conector.close()
print("Banco de dados atualizado com sucesso!")
print("Fim do programa.")