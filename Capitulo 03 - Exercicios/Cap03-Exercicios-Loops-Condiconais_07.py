# Exercício 7 - Crie uma lista vazia e uma variável com valor 4. Enquanto o valor da variável for menor ou igual a 20, adicione à lista, apenas os valores pares e imprima a lista
lista2 = []
numeroo = 4
for e in range(numeroo, 20+1):
  if e % 2 == 0:
    lista2.append(e)

print(lista2)