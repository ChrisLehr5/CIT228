import pandas as pd
from matplotlib.pyplot import pie, axis, show
import matplotlib.pyplot as plt

df= pd.read_csv('TermProject2/data/bf.csv')
print(df.head())
 
colors=('#0466c8','#4B3F72','#FFC857','#119DA4', '#83e377')
sums = df.groupby(df["precip_type"])["precip_intensity"].sum()
fig1, ax1 = plt.subplots()
ax1.pie(sums, labels=sums.index, shadow=True, startangle=2, colors=colors, autopct='%.2f%%')

plt.tight_layout()
plt.suptitle("Sightings By Percipitation Type")
plt.show()
