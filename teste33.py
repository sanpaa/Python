import os
from typing import IO
os.chdir(r"C:\Users\paulo\Desktop\pastazinha")


man = []
other = []



try:
    data=open("sketch.txt")
    for each_line in data:
            try:
                (role,line_spoken) = each_line.split(":",1)
                line_spoken = line_spoken.strip()
                if role=='Man':
                 man.append(line_spoken)
                elif role == 'Other Man':
                    other.append(line_spoken)

            except ValueError:
                pass

    data.close()    

except IOError:
    print("o arquivo de dados não está na pasta")

try:
    with open('man_data.txt1','w') as man_file:
        print(man,file = man_file)
    with open('other_data.txt1','w') as other_file:
        print(other,file=other_file)


except IOError:
    print("File error")
