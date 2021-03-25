import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df= pd.read_csv('TermProject2/data/bf.csv')

plt.figure(figsize=(20,10))
sns.heatmap(df.corr(), annot =True, linewidth = 0.5, cmap='Blues')
plt.title("Bigfoot Sightings Heat Map")
plt.show()