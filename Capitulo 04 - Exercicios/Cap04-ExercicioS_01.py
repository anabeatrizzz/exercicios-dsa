# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.

def Potencia(numero):
  return numero ** 3

numeros = [2, 4, 6]
print(list(map(Potencia, numeros)))
