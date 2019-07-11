
import seaborn as sns
import pandas as pd
import numpy as np


import matplotlib.pyplot as plt
df = pd.read_csv("D:/python/works/HR_comma_sep.csv")

sns.set_style(style="darkgrid")
plt.title("SALARY")
plt.xlabel("salary")
plt.ylabel("number")
plt.xticks(np.arange(len(df["salary"].value_counts())),df["salary"].value_counts().index)
plt.axis([0,4,0,10000])
plt.bar(np.arange(len(df["salary"].value_counts())+0.5),df["salary"].value_counts())
plt.show()