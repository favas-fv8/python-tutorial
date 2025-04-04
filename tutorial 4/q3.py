class Car:
 def __init__(self,model,year,price):
  self.model=model
  self.year=year
  self.price=price
 def cost(self):
  print(self.price)
c1=Car("A",2020,500000)
c2=Car("B",2022,700000)
c1.cost()
c2.cost()
