# Os enunciados:
# https://github.com/dsacademybr/PythonFundamentos/blob/master/Cap09/Notebooks/DSA-Python-Cap09-Exercicio.ipynb

import time
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df.head()

# Extração e Transformação de Dados
print(iris.target_names)
print(iris.target)
lista = []
lista2 = []
for c in range(0, 150):
    if iris.target[c] == 0:
        lista.append(iris.target_names[0])
    elif iris.target[c] == 1:
        lista.append(iris.target_names[1])
    elif iris.target[c] == 2:
        lista.append(iris.target_names[2])
for c in iris.data:
    lista2.append(c)
df["ESPECIES"] = lista
df["TARGET"] = iris.target
df["MEDIA"] = df.mean(1)
print(lista2)
print(df.head())

# Exploração de Dados
print(df.T)
print(df.info())
print(df.describe())
print(pd.isnull(df))
print(len(df["sepal length (cm)"]))

# Plot
plt.hist(df["sepal length (cm)"], rwidth=0.9)
plt.show()

x = range(0, 150)
plt.scatter(x, lista3, c=iris.target)
plt.show()

plt.scatter(x, df["petal length (cm)"])
plt.scatter(x, df["petal width (cm)"])
plt.show()

matriz = pd.plotting.scatter_matrix(df)
print(matriz)

plt.hist(df)
plt.show()