import calendar

# create a plaintext calendar
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2022, 1, 0, 0)
print(str)

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2023,1)
print(str)

# loop over the days of a month
for i in c.itermonthdays(2023,3):
    print(i)

# the calendar module provides useful utilities for the given local,
# such as the names of days and mnths in both full and abreviated forms
for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)

# calculate days based on a rule: for example, consider a team meeting on the first 
# Friday of every month. to figure out what days that would be for each month,
# we can use this script:
print("team meetings will be on")
for m in range(1,13):
    cal = calendar.monthcalendar(2023, m)
    weekone = cal[0]
    weektwo = cal[1]
    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print(calendar.month_name[m], meetday)


