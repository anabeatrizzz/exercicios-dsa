"""Crie um banco de dados no SQLite, crie uma tabela, insira registros,
consulte a tabela e retorne os dados em dataframe do Pandas."""

print("Exercicio 10")
conexao = sqlite3.connect("ex_dez.db")
cursorr = conexao.cursor()
criar = "create table if not exists assuntos (id integer primary key, titulo varchar(100), qt_videos integer, qt_docs integer, qt_quiz integer)"
cursorr.execute(criar)
inserir = "insert into assuntos values (?, ?, ?, ?, ?)"
registrar = [
	(1, "Introducao", 36, 1, 0),
	(2, "Variaveis Tipos e Estruturas de Dados", 21, 2, 1),
	(3, "Loops Condicionais Metodos e Funcoes", 25, 4, 2)]
for c in registrar:
	cursorr.execute(inserir, c)
conexao.commit()
selecionar = "select * from assuntos"
cursorr.execute(selecionar)
dados = cursorr.fetchall()
frame = pd.DataFrame(dados, columns=["ID", "TITULO", "QT_VIDEOS", "QT_DOCS", "QT_QUIZ"], index=None)
print(frame)