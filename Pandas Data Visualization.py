import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df3 = pd.read_csv('df3')
plt.style.use('ggplot')

#_1_    df3.plot.scatter(x='a', y='b', figsize=(12,3), s=50, c='red')

#_2_    df3['a'].plot.hist(bins=20,alpha=0.5)

#_3_    df3[['a','b']].plot.box()

#_4_    df3['d'].plot.kde(lw=5,ls='--')     # OR use density instead of kde

#_5_    df3[0:30].plot.area(alpha=0.5)
#       plt.legend(loc='best', bbox_to_anchor=(1.0,0.5))

plt.show()