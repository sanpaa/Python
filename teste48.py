import sqlite3
conector = sqlite3.connect("academia.db")
cursor = conector.cursor()
sql = "alter table cadastro add curso integer"
cursor.execute(sql)
sql = "alter table cadastro add dtingr date"
cursor.execute(sql)
sql = "alter table cadastro add peso double"
cursor.execute(sql)
sql = "alter table cadastro add altura double"
cursor.execute(sql)
sql = "update cadastro set curso =10,dtingr ='01/02/2021'"
cursor.execute(sql)
conector.commit()
cursor.close()
conector.close()
print("Banco de dados atualizado com sucesso! ")
print("Fim do programa")
