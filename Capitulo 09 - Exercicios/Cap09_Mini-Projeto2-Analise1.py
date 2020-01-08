import os
import subprocess
import stat
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
sns.set(style="white")

clean_data_path = "../input/autos.csv"
df = pd.read_csv(clean_data_path,encoding="latin-1")

# Crie um Plot com a Distribuição de Veículos com base no Ano de Registro
sns.distplot(df.yearOfRegistration, axlabel="Ano de registro")

# Crie um Boxplot para avaliar os outliers
"""
limousine     84077
kleinwagen    69334
kombi         60195
bus           26833
cabrio        20388
Other         19447
coupe         16920
suv           13585
andere         2908
"""
# df.price.mean() = 3903
#print(listaVeiculos[0])
#df.shape = (313687, 27)
listaVeiculos = df.vehicleType.value_counts().index
limousine = []
kleinwagen = []
kombi = []
bus = []
cabrio = []
Other = []
coupe = []
suv = []
andere = []
for c in range(0, 84077+1):
    if df.vehicleType[c] == "limousine" and df.price[c] > df.price.mean():
        limousine.append(df.price[c])

for c in range(0, 69334+1):
    if df.vehicleType[c] == "kleinwagen" and df.price[c] > df.price.mean():
        kleinwagen.append(df.price[c])

for c in range(0, 60195+1):
    if df.vehicleType[c] == "kombi" and df.price[c] > df.price.mean():
        kombi.append(df.price[c])

for c in range(0, 26833+1):
    if df.vehicleType[c] == "bus" and df.price[c] > df.price.mean():
        bus.append(df.price[c])

for c in range(0, 20388+1):
    if df.vehicleType[c] == "cabrio" and df.price[c] > df.price.mean():
        cabrio.append(df.price[c])

for c in range(0, 19447+1):
    if df.vehicleType[c] == "Other" and df.price[c] > df.price.mean():
        Other.append(df.price[c])

for c in range(0, 16920+1):
    if df.vehicleType[c] == "coupe" and df.price[c] > df.price.mean():
        coupe.append(df.price[c])

for c in range(0, 13585+1):
    if df.vehicleType[c] == "suv" and df.price[c] > df.price.mean():
        suv.append(df.price[c])

for c in range(0, 2908+1):
    if df.vehicleType[c] == "andere" and df.price[c] > df.price.mean():
        andere.append(df.price[c])

dados = [limousine, kleinwagen, kombi, bus, cabrio, Other, coupe, suv, andere]
ax = sns.boxplot(data=dados)

# Crie um Count Plot que mostre o número de veículos pertencentes a cada categoria
# Aumentar tamanho da figura
plt.figure(figsize=(10, 10))
ax2 = sns.countplot(x="vehicleType", data=df, palette=sns.light_palette("purple"))
ax2.set_ylabel("Total de veiculos para venda")
ax2.set_xlabel("Tipo de veiculo")
for p in ax2.patches:
  ax2.annotate(p.get_height(), (p.get_x(), p.get_height()))