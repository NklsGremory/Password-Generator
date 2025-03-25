import flet as ft
import random

def main (page: ft.Page):
    page.title = "Pasword Generator"
    page.window.icon = "assets/icon.png"
    page.adaptative = True
    page.window.height = 700
    page.window.width = 500

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

    def updateProgram(e): 
        
        senha.value = criadorSenhas(int(qntdElements.value))

        page.remove(line2Base)
        page.add(line2Updated)
        textPage.value = "Senha Gerada:"

        page.update()

    def voltarInicio(e):
        page.remove(line2Updated)
        page.add(line2Base)
        textPage.value = "Informe os parâmetros para gerar a senha:"

        page.update()
        
    # criação dos elementos
    titulo = ft.Text("Password Generator", size=35, color="white")
    btnBack = ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=voltarInicio)
    logo = ft.Image("icon.png", width=60, height=60, fit= ft.ImageFit.CONTAIN)
    divider = ft.Divider() #Terminar o divider

    textPage = ft.Text("Informe os parâmetros para gerar a senha", size=18, color="white")
    qntdElements = ft.TextField(label="Digite o tamaho da senha")
    cSymbols = ft.Checkbox(label="Deve conter símbolos")
    cNumbers = ft.Checkbox(label="Deve conter números")
    cLettersMa = ft.Checkbox(label="Deve conter letras maiúsculas")
    cLettersMi = ft.Checkbox(label="Deve conter letras minúsculas")
    btnSend = ft.Button("Gerar Senha", on_click=updateProgram)

    senha = ft.Text("", size=18, color="white")
    btnCopy = ft.IconButton(icon=ft.Icons.COPY_ALL_ROUNDED, on_click=copiarSenha) # REVER

    #variáveis de layout
    lineInicial = ft.Row(
        [logo,titulo],
        vertical_alignment= ft.CrossAxisAlignment.CENTER
    )

    line2Base = ft.Column(
        [qntdElements, cSymbols, cNumbers, cLettersMa, cLettersMi, btnSend],
        horizontal_alignment= ft.CrossAxisAlignment.CENTER
    )

    line2Updated = ft.Column(
        [ ft.Row([senha, btnCopy], vertical_alignment= ft.CrossAxisAlignment.CENTER), btnBack],
        horizontal_alignment= ft.CrossAxisAlignment.CENTER
    )

    #adiciona os elementos na página
    page.add(lineInicial, textPage, line2Base)

ft.app(main, assets_dir="assets")

#Organizar o layout
    #ajustar as "paginas"
#definir cores e fontes
#fazer a build
