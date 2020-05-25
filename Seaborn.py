import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')

#_1_    sns.jointplot(x='fare',y='age',data=titanic)

#_2_    sns.distplot(titanic['fare'],kde=False,color='red',bins=30)

#_3_    sns.boxplot(x='class', y='age', data=titanic, palette='rainbow')

#_4_    sns.swarmplot(x='class', y='age', data=titanic, palette='rainbow')

#_5_    sns.countplot(titanic['sex'])

#_6_    sns.heatmap(titanic.corr(), cmap='coolwarm')
#       plt.title('titanic.corr()')

#_7_    g = sns.FacetGrid(data=titanic, col='sex')
#       g.map(plt.hist, 'age')

plt.show()