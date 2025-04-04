import pandas as pd
df=pd.read_csv('student.csv')
print(df['CGPA'].mean())
print(df[df['CGPA']>9])
print(df[(df['Branch']=='CSE')&(df['CGPA']>9)])
print(df[df['CGPA']==df['CGPA'].max()])
print(df.groupby('Branch')['CGPA'].mean())
