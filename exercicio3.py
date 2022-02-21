num = int(input("Qual termo quer encontrar? "))
ul=1
pe=1

if (num<=1):
    print("Numero invalido.")
else:
    for count in range(11,num):
        termo = ul + pe
        pe = ul
        ul = termo
        count += 1
    print(termo)
