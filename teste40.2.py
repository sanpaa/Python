s = input ("Digite um numero inteiro: ")

if s.isnumeric():
    N = int(s)
    print("O numero digitado foi {0}".format (N))
else:
    print("Erro: digite apenas números.") 