import pandas as pd
import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import cufflinks as cf

init_notebook_mode(connected=True)
cf.go_offline()
df = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())
df2 = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Values': [32, 43, 50]})

#_1_    df.iplot(kind='scatter', x='A', y='B', mode='markers', size=10)

#_2_    df2.iplot(kind='bar', x='Category', y='Values')

#_3_    df.count().iplot(kind='bar')

#_4_    df.iplot(kind='box')

#_5_    df3 = pd.DataFrame({'x'=[1,2,3,4,5], 'y'=[10,20,30,40,50], 'z'=[5,4,3,2,1]})
#       df3.iplot(kind='surface', colorscale='rdylbu')

#_6_    df[['A','B']].iplot(kind='spread')

#_7_    df['A'].iplot(kind='hist', bins=25)

#_8_    df.iplot(kind='bubble', x='A', y='B', size='C')

#_9_    df.scatter_matrix()