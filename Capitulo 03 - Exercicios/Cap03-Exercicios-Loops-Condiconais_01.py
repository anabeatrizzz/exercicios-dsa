# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. Se o dia for igual a Domingo ou igual a sábado, imprima na tela "Hoje é dia de descanso", caso contrário imprima na tela "Você precisa trabalhar!"
dia = str(input("Qual o dia da semana? "))
if dia == "domingo" or dia == "sabado":
  print("Hoje é dia de descanso")
else:
  print("Você precisa trabalhar!")