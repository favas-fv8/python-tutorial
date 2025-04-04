import numpy as np
a=np.random.randint(0,20,(3,3))
b=np.random.randint(0,20,(3,3))
add=a+b
prod=a@b
t=prod.T
print(add)
print(prod)
print(t)
