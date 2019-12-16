# ************* Desafio ************* (pesquise na documentação Python)
# Exercício 10 - Crie uma função que receba o arquivo abaixo como argumento e retorne um resumo estatístico descritivo do arquivo. Dica, use Pandas e um de seus métodos, describe(). Arquivo: "binary.csv"
abrindo = pd.read_csv("binary.csv")
print(abrindo.describe())