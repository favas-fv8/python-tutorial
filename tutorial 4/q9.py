class RECTANGLE:
 def __init__(self,h,w,x,y):
  self.h=h
  self.w=w
  self.x=x
  self.y=y
 def center(self):
  return(self.x+self.w/2,self.y+self.h/2)
 def area(self):
  return self.h*self.w
 def perimeter(self):
  return 2*(self.h+self.w)
r=RECTANGLE(4,6,0,0)
print(r.center())
print(r.area())
print(r.perimeter())
