class Person:
  def __init__(self, name, age):
    #O método especial __init__ (construtor)
    self.name = name
    self.age = age
    #self: é uma maneira de identificação. Exemplo
    #p1.name=name
    #p1.age=age

p1 = Person("John", 36)
p2 = Person("Alfredo", 20)

print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)


#modelo 2
print()
def Perso (name, age):
    name = name
    age = age
    return name, age

p1 = Perso("John", 36)
p2 = Perso("Alfredo", 20)

print(p1)
print(p2)