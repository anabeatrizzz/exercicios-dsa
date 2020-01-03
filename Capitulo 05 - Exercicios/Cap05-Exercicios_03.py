"""Exercício 3 - Crie a classe Smartphone com 2 atributos, tamanho e interface
e crie a classe MP3Player com os atributos capacidade.
A classe MP3player deve herdar os atributos da classe Smartphone."""

class Smartphone():
  def __init__(self, t, i):
    self.tamanho = t
    self.interface = i


class MP3Player(Smartphone):
  def __init__(self, c):
    self.capacidade = c
