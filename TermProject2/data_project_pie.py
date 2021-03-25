import pandas as pd
from matplotlib.pyplot import pie, axis, show
import matplotlib.pyplot as plt

df= pd.read_csv('TermProject2/data/bf.csv')
print(df.head())
 
#Fall, Spring, Summer, Unknown, Winter
colors=('#FFC857','#F224C8','#F56652','#17F50D', '#2C70D4')
sums = df.groupby(df["season"])["humidity"].sum()
fig1, ax1 = plt.subplots()
ax1.pie(sums, labels=sums.index, startangle=2, colors=colors, autopct='%.2f%%')
plt.legend(bbox_to_anchor=(5,0), loc="right", fontsize=6)

plt.suptitle("Seasonal Sightings By Humidity Levels 1899-2017")
plt.tight_layout()
plt.show()

