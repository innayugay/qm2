import pandas as pd
import numpy as np
from mlxtend.preprocessing import minmax_scaling
from sklearn import preprocessing



diagnosis=pd.read_csv("qm2/python/practice/data/diagnosis per country .csv", index_col=0)
print(diagnosis.columns.tolist())


# std_scale = preprocessing.StandardScaler().fit(diagnosis[['Recorded diagnosis, 2008', 'Recorded diagnosis, 2009', 'Recorded diagnosis, 2010', 'Recorded diagnosis, 2011', 'Recorded diagnosis, 2012', 'Recorded diagnosis, 2013', 'Recorded diagnosis, 2014', 'Recorded diagnosis, 2015', 'Recorded diagnosis, 2016', 'Recorded diagnosis, 2017']])
# df_std = std_scale.transform(diagnosis[['Recorded diagnosis, 2008', 'Recorded diagnosis, 2009', 'Recorded diagnosis, 2010', 'Recorded diagnosis, 2011', 'Recorded diagnosis, 2012', 'Recorded diagnosis, 2013', 'Recorded diagnosis, 2014', 'Recorded diagnosis, 2015', 'Recorded diagnosis, 2016', 'Recorded diagnosis, 2017']])

scaled2008 = minmax_scaling(diagnosis,columns=['Recorded diagnosis, 2008'], min_val=0, max_val=1)
scaled2009 = minmax_scaling(diagnosis,columns=['Recorded diagnosis, 2009'], min_val=0, max_val=1)
scaled2010 = minmax_scaling(diagnosis,columns=['Recorded diagnosis, 2010'], min_val=0, max_val=1)
scaled2011 = minmax_scaling(diagnosis,columns=['Recorded diagnosis, 2011'], min_val=0, max_val=1)
scaled2012 = minmax_scaling(diagnosis,columns=['Recorded diagnosis, 2012'], min_val=0, max_val=1)
scaled2013 = minmax_scaling(diagnosis,columns=['Recorded diagnosis, 2013'], min_val=0, max_val=1)
scaled2014 = minmax_scaling(diagnosis,columns=['Recorded diagnosis, 2014'], min_val=0, max_val=1)
scaled2015 = minmax_scaling(diagnosis,columns=['Recorded diagnosis, 2015'], min_val=0, max_val=1)
scaled2016 = minmax_scaling(diagnosis,columns=['Recorded diagnosis, 2016'], min_val=0, max_val=1)
scaled2017 = minmax_scaling(diagnosis,columns=['Recorded diagnosis, 2017'], min_val=0, max_val=1)

# print(scaled)

# print(df_std)
scaled2008.to_csv('normal2008.csv', sep='\t')
scaled2009.to_csv('normal2009.csv', sep='\t')
scaled2010.to_csv('normal2010.csv', sep='\t')
scaled2011.to_csv('normal2011.csv', sep='\t')
scaled2012.to_csv('normal2012.csv', sep='\t')
scaled2013.to_csv('normal2017.csv', sep='\t')
scaled2014.to_csv('normal2014.csv', sep='\t')
scaled2015.to_csv('normal2015.csv', sep='\t')
scaled2016.to_csv('normal2016.csv', sep='\t')
scaled2017.to_csv('normal2017.csv', sep='\t')