# Exercício 1 - Crie um objeto a partir da classe abaixo, chamado roc1, passando 2 parâmetros e depois faça uma chamada aos atributos e métodos
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