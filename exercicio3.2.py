n = int(input('A sequência de Fibonacci de: '))
a, b = 0, 1
while a < n:
print(a, end=', ')
a, b = b, a+b

print('FIM')