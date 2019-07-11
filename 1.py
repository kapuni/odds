
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(sum(map(ord, 'axis_grids')))
tips = sns.load_dataset('tips')
tips.head()

# 将FacetGrid实例化出来
g = sns.FacetGrid(tips, col='time')
g.map(plt.hist, 'tip')

# 散点图把数据描绘出来 alpha透明程度，越小越透明
g = sns.FacetGrid(tips, col='sex', hue='smoker')
g.map(plt.scatter, 'total_bill', 'tip', alpha=.1)
g.add_legend()
plt.show()