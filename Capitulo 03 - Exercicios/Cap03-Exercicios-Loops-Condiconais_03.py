# Exercício 3 - Crie uma tupla de 4 elementos, multiplique cada elemento da tupla por 2 e guarde os resultados em uma lista
numeros = (2, 4, 6, 8)
lista = []
for c in numeros:
  mult = c * 2
  lista.append(mult)

print(lista)