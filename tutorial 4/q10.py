class Complex:
 def __init__(self,r,i):
  self.r=r
  self.i=i
 def __add__(self,other):
  return Complex(self.r+other.r,self.i+other.i)
 def display(self):
  print(f"{self.r}+{self.i}i")
c1=Complex(2,3)
c2=Complex(4,5)
c3=c1+c2
c3.display()
