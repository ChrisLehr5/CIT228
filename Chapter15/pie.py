#---------------------------------------Hands On #7---------------------------------------#
import matplotlib.pyplot as plt

# Pie chart
labels = 'PNG', 'JPEG', 'SVG', 'GIF', 'OTHER'
numUsed = [376, 348, 153, 104, 19]
explode = (.1, .1, 0, 0, .2)  
colors=('#0466c8','#4B3F72','#FFC857','#119DA4', '#83e377')

fig1, ax1 = plt.subplots()
ax1.pie(numUsed, explode=explode, labels=labels, autopct='%3.1f%%', shadow=True, startangle=2, colors=colors)
ax1.axis('equal')  
plt.suptitle("Most Popular Graphic Formats On The Web")

plt.show()