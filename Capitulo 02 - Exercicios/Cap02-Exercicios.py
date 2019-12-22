# Os enunciados:
# https://github.com/dsacademybr/PythonFundamentos/blob/master/Cap02/Notebooks/DSA-Python-Cap02-Exercicios.ipynb

print("Exercicio 1")
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for c in numeros:
  print(f'{c} ', end="")

print("\n")
print("Exercicio 2")
lista = [[1], [2], [3], [4], [5]]
for c in lista:
  print(f'{c} ', end="")

print("\n")
print("Exercicio 3")
string1 = "Ana "
string2 = "Beatriz"
string3 = string1 + string2
print(string3)

print("\n")
print("Exercicio 4")
tupla = (1, 2, 2, 3, 4, 4, 4, 5)
print(tupla.count(4))

print("\n")
print("Exercicio 5")
dicionario = {}
print(dicionario)

print("\n")
print("Exercicio 6")
dicionario2 = {
  "nome": "Ana",
  "idade": 18,
  "país": "Brasil"
}
for c, v in dicionario2.items():
  print(c, v)

print("\n")
print("Exercicio 7")
dicionario2['cor_preferida'] = 'vermelho'
for c, v in dicionario2.items():
  print(c, v)

print("\n")
print("Exercicio 8")
dicionario3 = {
  "endereço": "Rua Dos Bobos",
  "numero": 0,
  "pessoas": [2, 6]
}
for c, v in dicionario3.items():
  print(c, v)

print("\n")
print("Exercicio 9")
lista2 = ["Ana", [1, 2], {"objeto": "celular", "cor": "preto"}, 10.00]
for c in lista2:
  print(c)

print("\n")
print("Exercicio 10")
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
print(frase[1:18])
