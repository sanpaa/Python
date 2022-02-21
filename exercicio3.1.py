termos = int(input('Digite o número de termos Fibonatti: '))
anterior, proximo = 0,1
temp = 0

for i in range(termos):{
print (anterior, end=', ')
}
temp = anterior
anterior = proximo
proximo = temp + anterior


print('Fim')