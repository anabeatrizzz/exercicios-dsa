# Exercício 10 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for c in range(0, 7+1):
  if c > 5:
    print(lista[c], end=" ")