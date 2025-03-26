import flet as ft
import random

def main (page: ft.Page):
    page.title = "Pasword Generator"
    page.window.icon = "assets/icon.png"
    page.adaptative = True
    page.window.height = 700
    page.window.width = 500

    #design 
    colors = {
        "darkBlue": "#143CCA",
        "blue": "#0179E8",
        "green": "#38E7C5"
    }

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
        if(qntdElements.value == ""):
            page.open(ft.SnackBar(ft.Text("Por favor, informe o tamanho da senha!"), duration=2500))
            qntdElements.focus()
        else:
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
    divider = ft.Divider(color= colors["blue"], thickness= 3) #Terminar o divider

    textPage = ft.Text("Informe os parâmetros para gerar a senha", size=18, color="white", width= 480, text_align= ft.TextAlign.CENTER)
    qntdElements = ft.TextField(label="Digite o tamaho da senha", width=500, border_color="white", focused_border_color= colors["green"])
    cSymbols = ft.Checkbox(label="Deve conter símbolos", active_color=colors["green"])
    cNumbers = ft.Checkbox(label="Deve conter números", active_color=colors["green"])
    cLettersMa = ft.Checkbox(label="Deve conter letras maiúsculas", active_color=colors["green"])
    cLettersMi = ft.Checkbox(label="Deve conter letras minúsculas", active_color=colors["green"])
    btnSend = ft.ElevatedButton("Gerar Senha", on_click=updateProgram, style = ft.ButtonStyle(text_style= ft.TextStyle(size= 18)), width= 200, height= 50, color=colors["blue"])

    senha = ft.Text("", size=18, color="white")
    btnCopy = ft.IconButton(icon=ft.Icons.COPY_ALL_ROUNDED, on_click=copiarSenha) # REVER

    #variáveis de layout
    lineInicial = ft.Row(
        [logo,titulo],
        vertical_alignment= ft.CrossAxisAlignment.CENTER
    )

    textoPagina = ft.Column(
        [textPage, divider],
        horizontal_alignment= ft.CrossAxisAlignment.CENTER
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
    page.add(lineInicial, textoPagina, line2Base)

ft.app(main, assets_dir="assets")

#REVER O CASO DEFAULT  --> ALTA PRIORIDADE
#Organizar o layout
    #ajustar as "paginas"
#definir cores e fontes
#fazer a build
