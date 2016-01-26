class Point:
  def __init__(self,x,y):
    self.x = x
    self.y = y

o = Point(0, 0)
unit_x = Point(1, 0)
unit_y = Point(0, 1)


class Person:
  def __init__(self,name,surname,age):
    self.name = name
    self.surname = surname
    self.age = age

johnDoe = Person("John", "Doe", 28)
emperorPalpatine = Person("Sidious", "Darth", 90)


class Car:
  def __init__(self,brand,model,engineSize,productionYear):
    self.brand = brand
    self.model = model
    self.engineSize = engineSize
    self.productionYear = productionYear

cabrio = Car("mercedes", "CLK", 5000, 2004)
cityCar = Car("Fiat", "Cinquecent", 800, 2012)
