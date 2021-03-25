import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  
import csv


df= pd.read_csv('TermProject2/data/bf.csv')
print(df.head())

high = df["temperature_high"]
low = df["temperature_low"]
date = df["date"]

ax=plt.subplot()
ax.scatter(date, high, c=date, cmap="Reds", label="Jan Temps")
ax.scatter(date,low, c=date, cmap="Blues", label="Feb Temps")
plt.ylabel('Temperatures')
plt.xlabel('Years')
plt.suptitle('Sighting Temperature Density Comparison')
plt.title('Low temperature sightings vs High temperatures sightings')

plt.grid()
plt.show()



