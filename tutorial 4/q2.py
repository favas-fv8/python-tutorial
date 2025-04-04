class Rectangle:
 def __init__(self,l,b):
  self.l=l
  self.b=b
 def area(self):
  return self.l*self.b
r=Rectangle(4,5)
print(r.area())
