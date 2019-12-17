# Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.

a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]

for d in a:
  for f in b:
    if d == f:
      print(d, end=" ")
print("\n\033[36mNão consegui fazer uma função pois, sempre aparecia o erro \033[4;36m'int' object is not subscriptable\033[m\033[36m, \033[36mverei a resolução.\033[m")