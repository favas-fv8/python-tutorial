x=int(input())
y=int(input())
if x>0 and y>0:
 print("Quadrant I")
elif x<0 and y>0:
 print("Quadrant II")
elif x<0 and y<0:
 print("Quadrant III")
elif x>0 and y<0:
 print("Quadrant IV")
else:
 print("On axis")
