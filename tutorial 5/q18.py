import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('weather.csv')
print(df.head(10))
print(df['temperature'].max())
print(df['temperature'].min())
print(df[df['temperature']<28]['place'])
print(df[df['weather']=='Cloudy']['place'])
print(df['weather'].value_counts().sort_index())
plt.bar(df['date'],df['temperature'])
plt.show()
