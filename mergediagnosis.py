import pandas as pd
import numpy as np
from functools import reduce


df2008=pd.read_csv("normal2008.csv", index_col=0)
df2009=pd.read_csv("normal2009.csv", index_col=0)
df2010=pd.read_csv("normal2010.csv", index_col=0)
df2011=pd.read_csv("normal2011.csv", index_col=0)
df2012=pd.read_csv("normal2012.csv", index_col=0)
df2013=pd.read_csv("normal2013.csv", index_col=0)
df2014=pd.read_csv("normal2014.csv", index_col=0)
df2015=pd.read_csv("normal2015.csv", index_col=0)
df2016=pd.read_csv("normal2016.csv", index_col=0)
df2017=pd.read_csv("normal2017.csv", index_col=0)

print(df2008)
array=[df2008, df2009,df2010,df2011,df2012,df2013,df2014,df2015,df2016,df2017]

# result = pd.merge(array, left_index=True ,right_index=True)

result = reduce(lambda left,right: pd.merge(left,right,on='Country'), array)

# result= reduce(lambda left,right: pd.merge(arrayleft_index=True ,right_index=True, how='outer'), array).fillna('void')
print(result)
result.to_csv('merged.csv', sep=',')