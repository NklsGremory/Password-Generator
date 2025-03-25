import flet as ft
import random

def main (page: ft.Page):
    page.title = "Pasword Generator"
    page.adaptative = True
    page.window.height = 650
    page.window.width = 450

    #funções

    def criadorSenhas(num):
        letrasMa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        letrasMi = "abcdefghijklmnopqrstuvwxyz"
        numeros = "0123456789"
        simbolos = "!@#$%&*()_+"
        param = numeros # default case
        senha = ""

        param = numeros if(cNumbers.value) else ""
        param += simbolos if(cSymbols.value) else ""
        param += letrasMa if(cLettersMa.value) else ""
        param += letrasMi if(cLettersMi.value) else ""
        
        for i in range(num):
            senha += random.choice(param)

        print("Senha Gerada!") # test no terminal
        return senha

    def copiarSenha(e):
        page.set_clipboard(senha.value)
        print("Senha copiada!") # test no terminal

        page.open(ft.SnackBar(ft.Text("Senha copiada com sucesso!"), duration=2500))

        page.update()

    def gerarSenha(e): # rever o nome da função
        
        senha.value = criadorSenhas(int(qntdElements.value))

        page.remove(qntdElements, cSymbols, cNumbers, cLettersMa, cLettersMi, btnSend)
        page.add(senha, btnCopy)
        textPage.value = "Senha gerada:"


        page.update()
        
    # criação dos elementos
    titulo = ft.Text("Password Generator", size=35, color="white")

    textPage = ft.Text("Informe os parâmetrs para gerar a senha", size=18, color="white")
    qntdElements = ft.TextField(label="Digite o tamaho da senha")
    cSymbols = ft.Checkbox(label="Deve conter símbolos")
    cNumbers = ft.Checkbox(label="Deve conter números")
    cLettersMa = ft.Checkbox(label="Deve conter letras maiúsculas")
    cLettersMi = ft.Checkbox(label="Deve conter letras minúsculas")
    btnSend = ft.Button("Gerar Senha", on_click=gerarSenha)

    senha = ft.Text("", size=18, color="white")
    btnCopy = ft.IconButton(icon=ft.Icons.COPY_ALL_ROUNDED, on_click=copiarSenha) # REVER


    #adiciona os elementos na página
    page.add(titulo,textPage, qntdElements, cSymbols, cNumbers, cLettersMa, cLettersMi, btnSend)

ft.app(main)