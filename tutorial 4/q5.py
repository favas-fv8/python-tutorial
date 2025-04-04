class Person:
 def __init__(self,name,age,salary):
  self.name=name
  self.age=age
  self.salary=salary
 def display(self):
  print(self.name,self.age,self.salary)
p1=Person("A",25,20000)
p2=Person("B",30,30000)
p1.display()
p2.display()
