from datetime import datetime

#Get the current day, month, year, hour, minute and timestamp from datetime module
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print(day, month, year, hour, minute, timestamp)
#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print(now.strftime("%m/%d/%Y, %H:%M:%S"))
#Today is 5 December, 2019. Change this time string to time.
timeString = "5 December, 2019"
today = datetime.strptime(timeString, "%d %B, %Y")
print(today)
#Calculate the time difference between now and new year.
newYear = datetime(2025, 1, 1)
diff = newYear - now
print(diff)
#Calculate the time difference between 1 January 1970 and now.
time1 = datetime(1970, 1, 1)
diff1 = now - time1
print(diff1)
#Think, what can you use the datetime module for? Examples:
    #Time series analysis
    #To get a timestamp of any activities in an application
    #Adding posts on a blog
