import matplotlib.pyplot as plt
import csv
from datetime import datetime
import pandas as pd

filename2 = 'TermProject2/data/bf3.csv'
with open(filename2, encoding="utf8") as f2:    
    reader = csv.reader(f2)
    header_row = next(reader)
    print(header_row)

    highs, lows, dates = [], [], []
    for row in reader:   
        date = int(row[8])   
        high = int(row[12])
        low = int(row[14])
        highs.append(high)   
        dates.append(date)
        lows.append(low)  

#Plot the high and low temsps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='darkblue', alpha=0.5)
#ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Format plot
ax.set_title("Global Temperature Increase", fontsize=22)
ax.set_xlabel("Years", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=18)

plt.show()