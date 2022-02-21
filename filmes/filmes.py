""" Este é um módulo 'Filmes.py' e fornece uma função chamada print_filmes() que imprime listas que podem ou não incluir listas aninhadas """

def print_filmes(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_filmes(each_item)

        else:
            print(each_item)
