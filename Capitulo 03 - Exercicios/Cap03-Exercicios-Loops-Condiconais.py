# Os enunciados: https://github.com/dsacademybr/PythonFundamentos/blob/master/Cap03/Notebooks/DSA-Python-Cap03-Exercicios-Loops-Condiconais.ipynb

print("Exercicio 1")
dia = str(input("Qual o dia da semana? "))
if dia == "domingo" or dia == "sabado":
  print("Hoje é dia de descanso")
else:
  print("Você precisa trabalhar!")

print("\n")
print("Exercicio 2")
frutas = ["Maça", "Banana", "Pêssego", "Mamão", "Melancia"]
print("Morango" in frutas)

print("\n")
print("Exercicio 3")
numeros = (2, 4, 6, 8)
lista = []
for c in numeros:
  mult = c * 2
  lista.append(mult)

print(lista)

print("\n")
print("Exercicio 4")
for c in range(100, 150+1, 2):
  print(c)

print("\n")
print("Exercicio 5")
temperatura = 40
for c in range(35+1, temperatura+1):
  print(c)

print("\n")
print("Exercicio 6")
contador = 0
for d in range(contador, 100+1):
  print(d)
  if d == 23:
    break

print("\n")
print("Exercicio 7")
lista2 = []
numeroo = 4
for e in range(numeroo, 20+1):
  if e % 2 == 0:
    lista2.append(e)

print(lista2)

print("\n")
print("Exercicio 8")
nums = range(5, 45, 2)
print(list(nums))

print("\n")
print("Exercicio 9")
print("Apenas faltava dois dois pontos e uma indentação.")
temperatura = float(input('Qual a temperatura? '))
if temperatura > 30:
  print('Vista roupas leves.')
else:
    print('Busque seus casacos.')

print("\n")
print("Exercicio 10")
frase = "É melhor, muito melhor, contentar-se com a realidade; se ela não é tão brilhante como os sonhos, tem pelo menos a vantagem de existir."
somando2 = 0
for i in frase:
  if i == 'r':
    somando2 += 1
print(f'A quantidade de r\'s é: {somando2}')