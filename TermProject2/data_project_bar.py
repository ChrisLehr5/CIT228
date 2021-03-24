
import pandas as pd  
import matplotlib.pyplot as plt  

df= pd.read_csv('TermProject2/data/ufo.csv')
print(df.head())

year = df["Year"].value_counts()
sightings = df["Year"].value_counts().keys()

plt.title("UFO Sightings Per Year (1899-2017")
plt.ylabel("Number of Sightings Reported")
plt.xlabel("Years")
plt.xlim([1899, 2017])

plt.bar(sightings, year)
plt.xticks(rotation=90)
plt.show()