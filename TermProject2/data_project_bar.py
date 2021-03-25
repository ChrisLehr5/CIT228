
import matplotlib.pyplot as plt
import csv
from datetime import datetime

filename = 'TermProject2/data/tempUs.csv'
with open(filename) as f:    
    reader = csv.reader(f)
    header_row = next(reader)
    temps = []
    years = []

    for row in reader:      
        temp = float(row[1])
        temps.append(temp)
        year = int(row[0])
        years.append(year)    

# filename2 = 'TermProject2/data/bf3.csv'
# with open(filename2) as f2:    
#     reader = csv.reader(f2)
#     header_row = next(reader)
#     highs = []
#     dates = []

#     for row in reader:      
#         high = int(row[12])
#         highs.append(high)
#         date = int(row[8])
#         dates.append(date)    


#Plot the high and low temsps
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(years, temps, c='red', alpha=0.5)
#ax.plot(dates, highs, c='darkblue', alpha=0.5)
#ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Format plot
ax.set_title("Global Temperature Trends 1901-2015", fontsize=22)
ax.set_xlabel("Years", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature Anomaly (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=18)

plt.show()


