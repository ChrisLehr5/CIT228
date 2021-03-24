import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  

df= pd.read_csv('TermProject2/data/ufo.csv')
print(df.head())

data = pd.read_csv('TermProject2/data/fake.csv')

year = df['Year']
launch = data['Satellite']
# violent_crime =df['Event_Date']

# create figure and axis objects with subplots()
fig,ax = plt.subplots()

# make a plot
ax.plot(year, year, color="green", marker="+")
# set x-axis label
ax.set_xlabel("Year",fontsize=14)
# set y-axis label
ax.set_ylabel("Number of Sightings",color="green",fontsize=14)

# twin object for two different y-axis on the sample plot
ax2=ax.twinx()
# make a plot with different y-axis using second axis object
ax2.plot(launch, launch,color="red",marker="o")
#ax2.set_ylabel("Crime Increase",color="red",fontsize=14)
plt.suptitle('UFO Sightings By Year')
#plt.xlim([1899, 2017])
plt.ylim([0, 20])
plt.title('1899-2017')
plt.show()

