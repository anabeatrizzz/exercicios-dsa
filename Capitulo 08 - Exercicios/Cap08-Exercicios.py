# Os enunciados:
# https://github.com/dsacademybr/PythonFundamentos/blob/master/Cap08/Notebooks/DSA-Python-Cap08-Exercicios.ipynb

import numpy as np
import timeit
import pandas as pd
import requests
import sqlite3

print("Exercicio 1")
array = np.array([1000000])
print(timeit.timeit(f'{array[0]} * 2', number=100)/100)
lista = [1000000]
print(timeit.timeit(f'{lista[0]} * 2', number=100)/100)
print("\nArray numpy demora 2,4s\nLista python demora 2,1s\nLista python é mais rapida.")

print("\n")
print("Exercicio 2")
array2 = np.array([2, 4, 6, 8, 1, 3, 5, 7, 9, 10])
for c in range(5, 8+1):
	array2[c] = 0;
print(array2)

print("\n")
print("Exercicio 3")
matriz = np.array([[1,2,4],[5,6,8],[9,10,12]])
print(matriz[0])

print("\n")
print("Exercicio 4")
matriz2 = np.array([[2,4,6],[8,10,12]])
print(matriz2.shape)

print("\n")
print("Exercicio 5")
arr = np.arange(15).reshape((3, 5))
print(arr)
print("\nMatriz composta:")
C = np.array([[0, 5, 10],[1,6,11],[2,7,12],[3,8,13],[4,9,14]])
print(C)

print("\n")
print("Exercicio 6")
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
lista = []
for c in range(0, len(cond)):
	if cond[c] == True:
		lista.append(xarr[c])
print()
for c in range(0, len(cond)):
	if cond[c] == False:
		lista.append(yarr[c])
print(lista)

print("\n")
print("Exercicio 7")
A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
with open("teste.npy", "w") as arquivo:
	for c in A:
		arquivo.write(str(f"{c} "))
arquivo = open("teste.npy", "r")
B = arquivo.read()
arquivo.close()
lista2 = []
for c in B.split():
	lista2.append(int(c))
print(lista2)

print("\n")
print("Exercicio 8")
obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'a', 'b'])
print(obj.unique())

print("\n")
print("Exercicio 9")
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
frame = pd.DataFrame(resp)
print(frame[0:30])
print("\nNão consegui fazer, verei a resolução")

print("\n")
print("Exercicio 10")
conexao = sqlite3.connect("ex_dez.db")
cursorr = conexao.cursor()
criar = "create table if not exists assuntos (id integer primary key, titulo varchar(100), qt_videos integer, qt_docs integer, qt_quiz integer)"
cursorr.execute(criar)
inserir = "insert into assuntos values (?, ?, ?, ?, ?)"
registrar = [
	(1, "Introducao", 36, 1, 0),
	(2, "Variaveis Tipos e Estruturas de Dados", 21, 2, 1),
	(3, "Loops Condicionais Metodos e Funcoes", 25, 4, 2)]
for c in registrar:
	cursorr.execute(inserir, c)
conexao.commit()
selecionar = "select * from assuntos"
cursorr.execute(selecionar)
dados = cursorr.fetchall()
frame = pd.DataFrame(dados, columns=["ID", "TITULO", "QT_VIDEOS", "QT_DOCS", "QT_QUIZ"], index=None)
print(frame)