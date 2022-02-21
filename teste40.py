import re #importar a biblioteca do regex no pyton

print("Digite um numero")
pp_str = (input())
x = re.search("[0-9]", pp_str) # procurar o regex [0-9](Qualquer número(ocorrência) de 0 a 9) na variável pp_str

if not x: #verifica se ele encontrou ou não alguma ocorrência. 
    print("Errado.")
else:
    print("Perfeito.")
