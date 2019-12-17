# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
"""palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print (i)"""

palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
def Retorno(palavra):
  resultado = [[palavra.upper(), palavra.lower(), len(palavra)]]
  for c in resultado:
    print(c)
print(list(map(Retorno, palavras)))
print("\033[36mNão ficou igual, ficou aparecendo None na ultima linha, verei a resolução.\033[m")