"""
Imprima uma Transposta do dataset (transforme linhas e colunas e colunas em linhas)

Utilize a função Info do dataset para obter um resumo sobre o dataset

Faça um resumo estatístico do dataset

Verifique se existem valores nulos no dataset

Faça uma contagem de valores de sepal length
"""

import time
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

print(df.T)
print(df.info())
print(df.describe())
print(pd.isnull(df))
print(len(df["sepal length (cm)"]))