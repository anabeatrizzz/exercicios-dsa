# Os enunciados: https://github.com/dsacademybr/PythonFundamentos/blob/master/Cap04/Notebooks/DSA-Python-Cap04-ExercicioS.ipynb

print("Exercicio 1")
def Potencia(numero):
  return numero ** 3

numeros = [2, 4, 6]
print(list(map(Potencia, numeros)))

print("\n")
print("Exercicio 2")
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
def Retorno(palavra):
  resultado = [[palavra.upper(), palavra.lower(), len(palavra)]]
  for c in resultado:
    print(c)
print(list(map(Retorno, palavras)))
print("\033[36mNão ficou igual, ficou aparecendo None na ultima linha, verei a resolução.\033[m")

print("\n")
print("Exercicio 3")
matrix = [[1, 2],[3,4],[5,6],[7,8]]
for c in matrix:
  print(c)

print("\n")
print("Matriz transposta:")
T = [[1, 3, 5, 7], [2, 4, 6, 8]]
for c in T:
  print(c)

print("\n")
print("Exercicio 4")
def Quadrado(numero):
  return numero ** 2

def Cubo(numero):
  return numero ** 3

lista = [0, 1, 2, 3, 4]
print(list(map(Quadrado, lista)))
print(list(map(Cubo, lista)))

print("\n")
print("Exercicio 5")
listaA = [2, 3, 4]
listaB = [10, 11, 12]
for a in range(0, 2+1):
  print(listaA[a] ** listaB[a])

print("\n")
print("Exercicio 6")
tupla = range(-5, 5)
print(list(filter(lambda x: x < 0, tupla)))

print("\n")
print("Exercicio 7")
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
for d in a:
  for f in b:
    if d == f:
      print(d, end=" ")
print("\n\033[36mNão consegui fazer uma função pois, sempre aparecia o erro \033[4;36m'int' object is not subscriptable\033[m\033[36m, \033[36mverei a resolução.\033[m")

print("\n")
print("Exercicio 8")
import time
print(time.strftime("%d/%m/%Y %H:%M"))

print("\n")
print("Exercicio 9")
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}
dict3 = {'a':4, 'b':5}
print(dict3)
print("\033[36mNão consegui fazer com for, verei a resolução.\033[m")
"""for c in dict1.keys():
  for v in dict2.values():
    dict3[c] = v
print(dict3)"""

print("\n")
print("Exercicio 10")
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for c in range(0, 7+1):
  if c > 5:
    print(lista[c], end=" ")