from ctypes import sizeof
from tkinter import Button
from PySimpleGUI  import PySimpleGUI as sg

#layout

sg.theme("Reddit")
tela = [
    [sg.Text("Usuario:"), sg.Input(key='usuario', size =(20,1))],
    [sg.Text("Senha:"),sg.Input(key='senha',password_char="*", size =(20,1))],
    [sg.Checkbox("Salvar seu login?")],
    [sg.Button("Entrar", button_color = "Green", expand_x = True)],
    [sg.Button("Sair", button_color = "Red", expand_x = True)]

]

#janela

janela=sg.Window('Tela de login', tela)


#ler os eventos

while True:
    eventos,valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == "Entrar":               #Entrar
        if valores['usuario'] == "Jhonathan" and valores['senha'] == "123456":
            tela = [],
            sg.theme("Reddit")
            tela = [
                [sg.Checkbox("Salvar seu login?")],
            ]

            print("Bem vindo Dev!")
    if eventos == "Sair":                 #Fechar
        break
    
