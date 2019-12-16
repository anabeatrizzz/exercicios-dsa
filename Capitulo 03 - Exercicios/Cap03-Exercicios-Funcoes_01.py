# Exercício 1 - Crie uma função que imprima a sequência de números pares entre 1 e 20 (a função não recebe parâmetro) e depois faça uma chamada à função para listar os números
def Pares():
  for c in range(1, 20+1):
    if c % 2 == 0:
      print(f'{c} ', end="")

Pares()