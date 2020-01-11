import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white")

cd = "/storage/emulated/0/Documents/autos.csv"
df = pd.read_csv(cd, encoding="latin-1")

listaMarcas2 = df.brand.value_counts().index
listaVeiculos2 = df.vehicleType.value_counts().index

t = pd.DataFrame()
for a in listaMarcas2:
	for b in listaVeiculos2:
		z = df[(df["brand"] == a) & (df["vehicleType"] == b)]["price"].mean() # Linha copiada da resolução
		t = t.append(
			pd.DataFrame(
				{'brand': a, 'vehicleType': b, 'avgPrice': z},
				index=[0]
			)
		) # Linhas copiadas da resolucao
t = t.reset_index(drop=True)
t["avgPrice"].fillna(0, inplace=True)
t["avgPrice"] = t["avgPrice"].astype(int)
print(t.head(5))

"""
t3 = t.copy()
print(t3.head(5))

t2 = pd.DataFrame(t3["avgPrice"], index=None, columns=["PrecoMedio"])
print(t2.head(5))
"""