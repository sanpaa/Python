movies = (["Exterminador do futuro","Rambo","Star Wars","Tropa de Elite"])

print (movies[1])

print (len(movies))

movies.append("Os caçadores da Arca Perdida")
print(movies)
movies.pop()
print(movies)
movies.extend (["O poderoso Chefão", "O Mágico de Oz", "Tubarão"])
print (movies)

movies.remove("Rambo")
print(movies)

movies.insert(0,"Rambo")
print(movies)

for each_flick in movies:
    print(each_flick)

for i in range (len(movies)):
    print(movies[i])

print (""" """)

cont = 0
while cont < len(movies):
    print(movies[cont])
    cont = cont+1
