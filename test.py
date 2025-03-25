import flet as ft
import funcoesBrutas as fb

def main (page: ft.Page):
    page.title = "Pasword Generator"
    page.adaptative = True
    page.window.height = 650
    page.window.width = 450

    #funções

    def gerarSenha(e):
        
        senha.value = fb.criadorSenhas(int(qntdElements.value))
        print("Função funcionando!", senha) # test no terminal

        page.remove(qntdElements, cSymbols, cNumbers, cAllLetters, btnSend)
        page.add(senha)
        textPage.value = "Senha gerada:"


        page.update()
        
    # criação dos elementos
    titulo = ft.Text("Password Generator", size=35, color="white")

    textPage = ft.Text("Informe os parâmetrs para gerar a senha", size=18, color="white")
    qntdElements = ft.TextField(label="Digite o tamaho da senha")
    cSymbols = ft.Checkbox(label="Deve conter símbolos")
    cNumbers = ft.Checkbox(label="Deve conter números")
    cAllLetters = ft.Checkbox(label="Deve conter todas as letras, maiúsculas e minúsculas")
    btnSend = ft.Button("Gerar Senha", on_click=gerarSenha)

    senha = ft.Text("", size=18, color="white")
    btnCopy = ft.Button() # REVER


    #adiciona os elementos na página
    page.add(titulo,textPage, qntdElements, cSymbols, cNumbers, cAllLetters, btnSend)

ft.app(main)