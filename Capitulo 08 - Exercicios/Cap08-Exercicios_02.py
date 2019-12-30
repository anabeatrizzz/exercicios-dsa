"""
Crie um array de 10 elementos.
Altere o valores de todos os elementos dos índices 5 a 8 para 0
"""

array2 = np.array([2, 4, 6, 8, 1, 3, 5, 7, 9, 10])
for c in range(5, 8+1):
	array2[c] = 0;
print(array2)