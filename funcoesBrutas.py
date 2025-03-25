import random
def criadorSenhas(num):
  letrasMa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  letrasMi = "abcdefghijklmnopqrstuvwxyz"
  numeros = "0123456789"
  simbolos = "!@#$%&*()_+"
  
  senha = ""

  for i in range(num):
    senha += random.choice(letrasMa + letrasMi + numeros + simbolos)

  return senha











