import matplotlib.pyplot as plt
x=[1,2,3]
y1=[2,4,1]
y2=[1,3,5]
plt.plot(x,y1,label='Line1')
plt.plot(x,y2,label='Line2')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multiple Lines')
plt.legend()
plt.show()
