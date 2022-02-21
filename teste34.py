
mfixo=float(input("Digite um valor de venda:"))
comissao = 6/100
fmes = 12398.00

# Faturamento mensal + comissao

resultado = (fmes * comissao) 
print ("faturamento do mes = {0:.2f}".format(resultado+mfixo))
# Faturamento + comissao anual

print (resultado*12)