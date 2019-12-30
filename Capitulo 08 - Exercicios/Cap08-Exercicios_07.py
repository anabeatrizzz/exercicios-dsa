"""Crie um array A com 10 elementos e salve o array em disco com a extensão npy.
Depois carregue o array do disco no array B"""

A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
with open("teste.npy", "w") as arquivo:
	for c in A:
		arquivo.write(str(f"{c} "))
arquivo = open("teste.npy", "r")
B = arquivo.read()
arquivo.close()
lista2 = []
for c in B.split():
	lista2.append(int(c))
print(lista2)