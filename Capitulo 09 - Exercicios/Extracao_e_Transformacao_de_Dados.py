"""
Imprima os valores numéricos da Variável target (o que queremos prever),
uma de 3 possíveis categorias de plantas: setosa, versicolor ou virginica

Imprima os valores numéricos da Variável target (o que queremos prever),
uma de 3 possíveis categorias de plantas: 0, 1 ou 2

Adicione ao dataset uma nova coluna com os nomes das espécies,
pois é isso que vamos tentar prever (variável target)

Inclua no dataset uma coluna com os valores numéricos da variável target

Extraia as features (atributos) do dataset e imprima

Calcule a média de cada feature para as 3 classes
"""

import time
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

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