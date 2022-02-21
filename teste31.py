import os
os.getcwd()
os.chdir(r"C:\Users\paulo\Desktop\pastazinha")
os.getcwd()

data = open('sketch.txt')

for each_line in data:
    try:
        (role,line_spoken) = each_line.split(":",1)
        print(role, end="")
        print('disse: ', end="")
        print(line_spoken,end="")

    except:
        pass

data.close()
