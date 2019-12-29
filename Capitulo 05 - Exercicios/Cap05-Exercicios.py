# Os enunciados: https://github.com/dsacademybr/PythonFundamentos/blob/master/Cap05/Notebooks/DSA-Python-Cap05-Exercicios.ipynb

print("Exercicio 1")
class Rocket():
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
        
  def move_rocket(self, x_increment=0, y_increment=1):
    self.x += x_increment
    self.y += y_increment
      
  def print_rocket(self):
    print([self.x, self.y])

roc1 = Rocket(1, 2)
print([roc1.x, roc1.y])
roc1.move_rocket(2, 2)
roc1.print_rocket()

print("\n")
print("Exercicio 2")
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

print("\n")
print("Exercicio 3")
class Smartphone():
  def __init__(self, t, i):
    self.tamanho = t
    self.interface = i


class MP3Player(Smartphone):
  def __init__(self, c):
    self.capacidade = c