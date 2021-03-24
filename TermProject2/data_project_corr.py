import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df= pd.read_csv('TermProject2/data/ufo.csv')
print(df.head())

sns.pairplot(df)
plt.show()
