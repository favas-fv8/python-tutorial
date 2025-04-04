import pandas as pd
df=pd.DataFrame({'City':['X','Y'],'Temp':[30,32]})
df.to_excel('weather.xlsx',index=False)
