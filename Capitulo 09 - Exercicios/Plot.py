"""
Crie um Histograma de sepal length

Crie um Gráficos de Dispersão (scatter Plot) da variável sepal length
versus número da linha, colorido por marcadores da variável target

Crie um Scatter Plot de 2 Features (atributos)

Crie um Scatter Matrix das Features (atributos)

Crie um Histograma de todas as features
"""

import time
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

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