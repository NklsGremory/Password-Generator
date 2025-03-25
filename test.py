import flet as ft 

def main (page: ft.Page):
    page.title = "Pasword Generator"
    page.adaptative = True
    page.window.height = 600
    page.window.width = 400

    #funções

    def gerarSenha(e):
        print("Função funcionando!", qntdElements.value)

        page.update()

    def atualizarPag(e):

        page.update()


    # criação dos elementos
    titulo = ft.Text("Password Generator", size=35, color="white")

    textPage = ft.Text("Informe os parâmetrs para gerar a senha", size=18, color="white")
    qntdElements = ft.TextField(label="Digite o tamaho da senha")
    cSymbols = ft.Checkbox(label="Deve conter símbolos")
    cNumbers = ft.Checkbox(label="Deve conter números")
    cAllLetters = ft.Checkbox(label="Deve conter todas as letras, maiúsculas e minúsculas")
    btnSend = ft.Button("Gerar Senha", on_click=gerarSenha)

    senha = ft.Text("")
    btnCopy = ft.Button(icon= ft.icons.COPY_ROUNDED)


    #adiciona os elementos na página
    page.add(titulo,textPage, qntdElements, cSymbols, cNumbers, cAllLetters, botao, senha)






ft.app(main)