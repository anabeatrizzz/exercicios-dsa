# Importações
import os
import subprocess
import stat
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
sns.set(style="white")

# Informando onde o arquivo se encontra
clean_data_path = "../input/autos.csv"

# Carregando o arquivo em df
df = pd.read_csv(clean_data_path, encoding="latin-1")

# Crie um Barplot com o Preço médio do veículo por tipo de combustível e tipo de caixa de câmbio

# Definindo tamanho da figura, como há varias barras no grafico, usa-se subplots()
plt.subplots(figsize=(10, 10))

# Lista de cores
cores = ["#E68193", "#58A141", "#529FD6"]

# sns.barplot(x="nome_coluna_um", y="nome_coluna_dois", hue="nome_coluna_para_legenda", data="onde_colunas_estao", palette="lista_de_cores")
# x ou y precisa ser uma coluna numerica
ax = sns.barplot(x="fuelType", y="price", hue="gearbox", data=df, palette=sns.color_palette(cores))

# Colocando legenda no eixo x
plt.xlabel("Tipo de Combustivel")

# Colocando legenda no eixo y
plt.ylabel("Preço médio")

# Colocando titulo no grafico
plt.title("Preço médio do veiculo por tipo de combustivel e tipo de caixa de cambio")

# Crie um Barplot com a Potência média de um veículo por tipo de veículo e tipo de caixa de câmbio

# Definindo tamanho da figura, como há varias barras no grafico, usa-se subplots()
plt.subplots(figsize=(10, 10))

# Lista de cores
cores2 = ["#4879AE", "#DFA727", "#A6A397"]

# sns.barplot(x="nome_coluna_um", y="nome_coluna_dois", hue="nome_coluna_para_legenda", data="onde_colunas_estao", palette="lista_de_cores")
# x ou y precisa ser uma coluna numerica
ax = sns.barplot(x="vehicleType", y="powerPS", hue="gearbox", data=df, palette=sns.color_palette(cores2))

# Colocando legenda no eixo x
plt.xlabel("Tipo de Veiculo")

# Colocando legenda no eixo y
plt.ylabel("Potencia media")

# Colocando titulo no grafico
plt.title("Potencia media de um veiculo por tipo de veiculo e tipo de caixa de cambio")
