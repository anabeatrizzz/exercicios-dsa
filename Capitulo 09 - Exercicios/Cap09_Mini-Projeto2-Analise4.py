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

# Indicando onde o conjunto de dados está
clean_data_path = "../input/autos.csv"

# Guardando o conjunto de dados em uma variavel
df = pd.read_csv(clean_data_path, encoding="latin-1")

# Calcule a média de preço por marca e por veículo
# Todas as marcas de carro
listaMarcas2 = df.brand.value_counts().index

# Todos os tipos de carros
listaVeiculos2 = df.vehicleType.value_counts().index

# DataFrame vazio
t = pd.DataFrame()

# Para cada marca e tipo de carros:
for a in listaMarcas2:
    for b in listaVeiculos2:
        z = df[(df["brand"] == a) & (df["vehicleType"] == b)]["price"].mean() # Linha copiada da resolução
        t = t.append(
                pd.DataFrame(
                    {'brand': a, 'vehicleType': b, 'avgPrice': z},
                    index=[0]
            )
        ) # Linhas acima copiadas da resolucao

# Redefinindo o index com reset_index e passando drop como True para a coluna index ser excluida
t = t.reset_index(drop=True)

# Preenchendo os valores missing com zero e passando inplace como True para preencher no local
t["avgPrice"].fillna(0, inplace=True) # Linha copiada da resolução

# Definindo que a coluna avgPrice é numerica do tipo int
t["avgPrice"] = t["avgPrice"].astype(int) # Linha copiada da resolução
print(t.head(5))

# Crie um Heatmap com Preço médio de um veículo por marca, bem como tipo de veículo
t3 = t.copy()
t3 = t3.pivot("brand", "vehicleType", "avgPrice")
plt.figure(figsize=(12, 12))
ax = sns.heatmap(t3, annot=True, fmt="d", cmap="YlGnBu")
plt.xlabel("Tipo de Veiculo")
plt.ylabel("Marca")
plt.title("Heatmap - Preço médio de um veiculo por marca e tipo de veiculo")
