def fatorial(numero):
    if numero ==1:
        return 1
    if numero ==0:
        return 1
    return numero * fatorial(numero -1)