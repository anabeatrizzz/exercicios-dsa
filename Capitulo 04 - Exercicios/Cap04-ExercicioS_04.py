# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
# lista = [0, 1, 2, 3, 4]

def Quadrado(numero):
  return numero ** 2

def Cubo(numero):
  return numero ** 3

lista = [0, 1, 2, 3, 4]
print(list(map(Quadrado, lista)))
print(list(map(Cubo, lista)))