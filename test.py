import flet as ft 

def main (page: ft.Page):
    page.title = "Pasword Generator"
    page.adaptative = True
    page.window.height = 600
    page.window.width = 400

    #funções

    def gerarSenha(e):
        print("Função funcionando!", campoEntrada.value)

        page.update()


    # criação dos elementos
    titulo = ft.Text("Password Generator", size=20, color="black")
    campoEntrada = ft.TextField("Digite o tamanho da senha")
    botao = ft.Button("Gerar Senha", on_click=gerarSenha)
    senha = ft.Text("")


    #adiciona os elementos na página
    page.add(titulo, campoEntrada, botao, senha)






ft.app(main)