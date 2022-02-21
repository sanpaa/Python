# -*- coding: utf-8 -*- 
import sys
import os
from typing import IO
os.chdir(r"C:\Users\paulo\Desktop\Exercicio faculdade PYTHON") #usei o R pois não estou conseguindo executar sem transformar em RAW
os.getcwd()


entrevistador = []
CM = []


try:
    data=open("entrevista.txt")
    for each_line in data:
            try:
                (role,line_spoken) = each_line.split(":",1)
                line_spoken = line_spoken.strip()
                if role=='Entrevistador':
                 entrevistador.append(line_spoken)
                elif role == 'CM':
                    CM.append(line_spoken)

            except ValueError:
                pass

    data.close()    

except IOError:
    print("o arquivo de dados não está na pasta")

try:
    with open('Entrevistador_data.txt','w') as entrevistador_file:
        print(entrevistador,file = entrevistador_file)
    with open('CM_data.txt','w') as cm_file:
        print(CM,file=cm_file)


except IOError:
    print("File error")
