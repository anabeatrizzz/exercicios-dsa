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
df = pd.read_csv(clean_data_path, encoding="latin-1")

# Crie um Plot que mostre o número de veículos pertencentes a cada marca
plt.figure(figsize=(10, 10))
height = df.brand.value_counts().values
bars = df["brand"].unique()
y_pos = np.arange(len(bars))
 
plt.barh(y_pos, height)
 
plt.yticks(y_pos, bars)

plt.xlabel("Numero de Veiculos")
plt.ylabel("Marca")
plt.title("Veiculos por Marca")
 
plt.show()

# Crie um Plot com o Preço médio dos veículos com base no tipo de veículo, bem como no tipo de caixa de câmbio
fig, ax = plt.subplots(figsize=(10, 10)) # Linha copiada da resolução
sns.barplot(x="vehicleType", y="price", hue="gearbox", data=df) # Linha copiada da resolução
plt.xlabel("Tipo de Veiculo")
plt.ylabel("Preço médio")
plt.title("Preço médio dos veiculos por tipo de veiculo e tipo de caixa de cambio")
print("Minha resolução não estava dando certo pois, esqueci que tinha que usar a coluna price e só pensei no tipo de veiculo e gearbox. Não sabia que teria que chamar o subplot() tambem")
