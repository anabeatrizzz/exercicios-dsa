"""Considere os 3 arrays abaixo.
Retorne o valor do array xarr se o valor for True no array cond.
Caso contrário, retorne o valor do array yarr."""

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
lista = []
for c in range(0, len(cond)):
	if cond[c] == True:
		lista.append(xarr[c])
print()
for c in range(0, len(cond)):
	if cond[c] == False:
		lista.append(yarr[c])
print(lista)