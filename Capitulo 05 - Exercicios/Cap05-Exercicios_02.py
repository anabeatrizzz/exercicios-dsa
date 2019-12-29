# Exercício 2 - Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. Use pelo menos 2 métodos especiais na sua classe. Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos especiais.
class Pessoa():
  def __init__(self, n, c, t, e):
    self.nome = n
    self.cidade = c
    self.telefone = t
    self.email = e
  def mostrando(self):
    print(f'Nome: {self.nome}\nCidade: {self.cidade}\nTelefone: {self.telefone}\nE-mail: {self.email}')

alguem = Pessoa("Ana", "Itanhaem", 13981040639, "anaaugusto2012@bol.com.br")
alguem.mostrando()