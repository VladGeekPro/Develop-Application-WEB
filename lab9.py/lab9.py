import time
from datetime import datetime, timedelta
import calendar 

#Time
starTime = time.time()

time.sleep(5)

endTime = time.time()

sleepDuration = endTime - starTime 

print(f"It sleeped = {sleepDuration:.2f}s")

#Datetime
today = datetime.now()

formattedToday = today.strftime("%Y-%m-%d %H:%M:%S")
print(f"Today's date and time = {formattedToday}")

formattedDay = today.strftime("%B")
print(f"Month = {formattedDay}")

formattedDayOfWeek = today.strftime("%a")
print(f"Day of the week = {formattedDayOfWeek}")

dayAfterTomorrowAndOneHour = today + timedelta(days=2,hours=1)
print(f"Day after tomorrow and plus one hour = {dayAfterTomorrowAndOneHour}", end="\n\n")

#Calendar
c = calendar.TextCalendar(calendar.SUNDAY)
year = c.formatyear(2023, w=3, m=4)

print("{}".format(year))