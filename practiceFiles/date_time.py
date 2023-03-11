# import datetime
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def main():
    # print today's date from the simple today() method from the date class
    today = date.today()
    print("Today's date is", today)

    # print out the date's individual components
    print("date components:", today.day, today.month, today.year)

    # retrieve today's weekday (0=Monday, 6=Sunday)
    print("today's weekeday number is", today.weekday())
    days = ["mon","tue","wed","thur","fri","sat","sun"]
    print("which is a ", days[today.weekday()])

    # get today's date from the datetime class
    today = datetime.now()
    print("the current date and time is", today)

    # get the current time
    t = datetime.time(datetime.now())
    print("the current time is", t)

    # date formatting
    # %y/%Y is year, %1/%A is weekday, %b/%B is month, %d is day of month
    now = datetime.now()
    print(now.strftime("the current year is: %y"))
    print(now.strftime("the current year is: %Y"))
    print(now.strftime("%a, %d %B, %Y"))

    # %c is locale's date and time, %x is locates date, %X is locale's time
    print(now.strftime("locale date and time: %c"))
    print(now.strftime("locale date: %x"))
    print(now.strftime("locale time: %X"))

    # time formatting
    # %I/%H is 12/24 hour, %M is minute, %S is second, %p is locale's AM/PM
    print(now.strftime("current time is, %I:%M:%S %p"))
    print(now.strftime("24-hour time is, %H:%M"))

    # consturct a basic timedelta and print it
    print(timedelta(days=365, hours=5, minutes=1))

    # print today's date one year from now
    print("one year from now it will be", str(now + timedelta(days=365)))

    # create a timedelta that uses more than one argument
    print("in two weeks and 3 days it will be", str(now + timedelta(weeks=2, days=3)))

    # calculate the date 1 week ago, formatting as a string
    t = datetime.now() - timedelta(weeks=1)
    s = t.strftime("%A %B %d, %Y")
    print("one week ago it was", s)

    # how many days until April Fool's Day?
    today = date.today()
    afd = date(today.year, 4, 1)

    if afd < today:
        print("april fool day already went by:", ((today-afd).days))
        afd = afd.replace(year = today.year +1)

    time_to_afd = afd - today
    print("it is", time_to_afd.days, "days until the next april fools day")
                                              
if __name__ == "__main__":
    main()

