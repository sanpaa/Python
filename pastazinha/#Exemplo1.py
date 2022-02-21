import os
os.getcwd()
os.chdir(r"C:\Users\paulo\Desktop\pastazinha")
os.getcwd()

data = open('sketch.txt')
print(data.readline(), end='')

print(data.readline(),end='')