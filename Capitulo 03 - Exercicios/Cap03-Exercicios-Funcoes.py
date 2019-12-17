# Os enunciados: https://github.com/dsacademybr/PythonFundamentos/blob/master/Cap03/Notebooks/DSA-Python-Cap03-Exercicios-Funcoes.ipynb

import pandas as pd

print("Exercicio 1")
def Pares():
  for c in range(1, 20+1):
    if c % 2 == 0:
      print(f'{c} ', end="")

Pares()

print("\n")
print("Exercicio 2")
def Maiusculo(texto):
  print(texto.upper())

Maiusculo("Ana")

print("\n")
print("Exercicio 3")
def Adicionando(lista):
  lista.append(1)
  lista.append(2)
  print(lista)

lista1 = [3, 4]
Adicionando(lista1)

print("\n")
print("Exercicio 4")
def Teste(p=1, s=1, t=1, q=1, qu=1):
  print(p + s + t + q + qu / 5)

Teste(2)
Teste(2, 3, 4, 5)

print("\n")
print("Exercicio 5")
anonima = lambda x, y: x + y
print(anonima(1, 2))

print("\n")
print("Exercicio 6")
total = 0
def soma(arg1, arg2):
    total = arg1 + arg2; 
    print("Dentro da função o total é: ", total)
    return total;


soma(10, 20);
print("Fora da função o total é: ", total)
print("Pois, não foi passado nenhum numero como parametro.")

print("\n")
print("Exercicio 7")
Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda x: (9.0 / 5) * (x + 32), Celsius)
print(list(Fahrenheit))

print("\n")
print("Exercicio 8")
dicio = {"Nome":"Ana", "Idade":18}
print(dir(dicio))

print("\n")
print("Exercicio 9")
print("pd.Series\nUma série é como se fosse uma tabela contendo indices e valores.\n\npd.isnull\nPara saber se há algum valor nulo em uma serie.\n\npd.notnull\nPara saber se há algum valor não-nulo em uma serie.\n\npd.DataFrame\nUm dataframe é algo semelhante a uma planilha excel.\n\npd.read_csv\nPara ler um arquivo csv.\n\npd.date_range\nPara criar uma quantidade de datas especifica.\n\npd.merge\nPara juntar DataFrames que contem colunas que se relacionam.")

print("\n")
print("Exercicio 10")
abrindo = pd.read_csv("binary.csv")
print(abrindo.describe())
