import sqlite3
import os
os.chdir(r'C:\Users\paulo\Desktop\Faculdade\Lab.Desenvolv')

print(" Cria e carrega tabela cursos:")
conector = sqlite3.connect("academia.db")
cursor = conector.cursor()
sql = """ 
    create table cursos
    (codcurso integer not NULL Primary Key,
    nomecurso text,valores double)
""" 

cursor.execute(sql)
print ("...tabela cursos criada!")
#carrega com dados do curso
sql = """
    insert into cursos(codcurso,nomecurso,valores
    )values(?,?,?)
"""

DadosCurso = [
    (10, "Musculação", 110.00),
    (11, "Treino aeróbico", 110.00),
    (12, "Combo 1: Musculação + Aeróbico", 180.00),
    (15, "Natação", 180.00),
    (22, "Pilates", 165.00),
    (25, "Combo 2: Pilates +Aeróbico", 240.00),
    (30, "Crossfit", 180.00),
    (41, "Muay Thai", 140.00),
    (42, "Jiu Jitsu", 140.00),
    (43, "Boxe", 140.00)
]

print ("...dados a serem carregados")
for dados in DadosCurso:
    print("  ", dados)


cursor.executemany(sql,DadosCurso)
conector.commit()
cursor.close()
conector.close()

print("Tabela cursos criada com sucesso")
print("Fim do programa.")