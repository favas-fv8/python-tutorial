import pandas as pd
df=pd.DataFrame({'Name':['A','B'],'Age':[20,21]})
df.to_excel('file.xlsx',index=False)
