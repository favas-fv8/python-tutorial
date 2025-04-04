class Student:
 def readData(self,roll,mark1,mark2):
  self.roll=roll
  self.mark1=mark1
  self.mark2=mark2
 def computeTotal(self):
  self.total=self.mark1+self.mark2
 def printDetails(self):
  print(self.roll,self.mark1,self.mark2,self.total)
s=Student()
s.readData(1,60,70)
s.computeTotal()
s.printDetails()
