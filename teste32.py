import os
os.chdir(r"C:\Users\paulo\Desktop\pastazinha")


man = []
other = []



try:
    data=open("sketch.txt")
    for each_line in data:
        (role,line_spoken) = each_line.split(":",1)
        print(role, end="")
        print('disse: ', end="")
        print(line_spoken,end="")

    data.close()    

except:
    print("o arquivo de dados não está na pasta")
