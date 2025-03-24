import random

letrasMa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letrasMi = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"
simbolos = "!@#$%&*()_+"

senha = ""

qntCaracter = int(input("Informe a quantidade de caracteres desejadas na senha: "))

print(qntCaracter)

for i in range(qntCaracter):
  senha += random.choice(letrasMa + letrasMi + numeros + simbolos)

print(senha)
