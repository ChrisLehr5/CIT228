import datetime
#weekdays tuple
weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
#retreiving current date 
now = datetime.date.today()
#retreive the day of the week which is an integer 
dayOfWeek= now.weekday()
#subscript into weekDays using dayOfWeek
today = weekDays[dayOfWeek]
#calculate and print days until weekend 
daysToWeekend = 6-dayOfWeek
print("There are ", daysToWeekend-1, " days until the weekend.")
#flag to only print 1 quote in for loop
quotePrinted = "false"
#prints week days left until weekend with a quote 
for left in weekDays[dayOfWeek:daysToWeekend]:
    if today =="Sunday" and quotePrinted=="false":
        print(left, "Sunday is the day before the end!") 
        quotePrinted ="true"
    elif (today =="Monday" or today== "Tuesday" or today =="Wednesday") and quotePrinted=="false":
        print(left, "Not quite time to be excited.")
        quotePrinted="true"
    elif today =="Thursday" and quotePrinted=="false":
        print(left, "So close..")
        quotePrinted="true"
    elif quotePrinted =="false":
        print(left, "Weekend bliss!")
        quotePrinted ="true"
    else:
        print(left)
