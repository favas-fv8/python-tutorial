import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('sales.csv')
plt.scatter(df['month_number'],df['toothpaste'])
plt.show()
df[['facecream','facewash']].plot(kind='bar')
plt.show()
df.drop(['month_number','total_units','total_profit'],axis=1).sum().plot.pie()
plt.show()
