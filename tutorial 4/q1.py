class Arith:
 def read(self,a,b):
  self.a=a
  self.b=b
 def add(self):
  return self.a+self.b
obj=Arith()
obj.read(5,7)
print(obj.add())
