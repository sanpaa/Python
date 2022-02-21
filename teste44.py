Alunos = {}
print ("Leitura de dados: ")
while True:
    matr = int(input("     Digite a matricula:  "))
    if matr == 0:
        break
    elif matr in Alunos:
        print ("A matricula {} já existe no cadastro".format (matr))
        continue
    dicItem={}
    dicItem['nome'] = input("Nome: ")
    dicItem['idade'] = int(input("Idade: "))
    dicItem['curso']= input("Curso: ")
    Alunos[matr] = dicItem

print ("Fim da leitura de dados ")

print ("Cadastro de alunos")


for matricula,dados in Alunos.items():
    print ("  Aluno {}".format(dados[0]))
    print ("  Nr.Matricula {}".format(matricula))
    print ("  Idade {}".format(dados[1]))
    print ("  Curs {}".format(dados[2]))
print ("Fim do programa")
