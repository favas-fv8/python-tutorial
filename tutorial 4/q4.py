class Student:
 def __init__(self,name,roll):
  self.name=name
  self.roll=roll
 def dataprint(self):
  print(self.name,self.roll)
s1=Student("Ram",1)
s2=Student("Sam",2)
s1.dataprint()
s2.dataprint()
