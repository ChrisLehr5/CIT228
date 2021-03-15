#---------------------------------------Hands On #1---------------------------------------#

import csv
import matplotlib.pyplot as plt

from datetime import datetime

filename = 'Chapter16/data/greenbaytemp.csv' 
with open(filename) as f:    
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    #Get dates,high and low temps from file 
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[3])
        low = int(row[4])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)        

#Finding the index numbers 
#for index, column_header in enumerate(header_row):
    #print(index, column_header)

#Plot the high and low temsps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='darkblue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Format plot
ax.set_title("Green Bay WI Daily Temps (January-March)", fontsize=22)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=18)

plt.show()




