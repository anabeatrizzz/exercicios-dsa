# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. Imprima o dicionário na tela.
dicionario3 = {
  "endereço": "Rua Dos Bobos",
  "numero": 0,
  "pessoas": [2, 6]
}
for c, v in dicionario3.items():
  print(c, v)