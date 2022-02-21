entrada = input ("Digite um numero de 0 a 100 ")
numero = int(entrada)

if numero <0 or numero >100 :
    print ("O numero digitado foi invalido. ")

if numero % 2 == 0:
    print ("O numero digitado foi par. ")

if not numero % 2 == 0:
    print ("O numero digitado foi impar")
    