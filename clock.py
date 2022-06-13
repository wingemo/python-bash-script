from datetime import datetime
import pytz

tz_NY = pytz.timezone('America/New_York') 
datetime_NY = datetime.now(tz_NY)
time_new_york = "NY time:", datetime_NY.strftime("%H:%M:%S")

tz_London = pytz.timezone('Europe/London')
datetime_London = datetime.now(tz_London)
time_london = "London time:", datetime_London.strftime("%H:%M:%S")

tz_London = pytz.timezone('Europe/Stockholm')
datetime_London = datetime.now(tz_London)
time_stockholm = "Stockholm time:", datetime_London.strftime("%H:%M:%S")

print(time_new_york + time_london + time_stockholm)