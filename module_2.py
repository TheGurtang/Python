from collections import Counter

def Elm_count():
    list_1 = range(3,33,3)
    print(list_1)
    list_2 = []
    for i in list_1:
        if i %2 !=0:
            list_2.append(i*2)
            print(Counter(list_2))
print(Elm_count())

## modul  'datetime' for setting and defining date - years, months and days; time - for hours, minutes, seconds; datetime - for date and time simultaneously; timetable - for interbals of date and time$
from datetime import date
halloween = date(2021, 10, 31)
print(halloween.isoformat())

from datetime import datetime
now = date.today()
print(now)

import time
t_now1 = time.ctime()   ### wonderful module to show the current day, month, date of month, current time and year
print(t_now1)


from array import array     ### array allows to create a list with easy-operable functions
arr = array('i', [1,2,3])
print(arr)
print(arr[1])               ## here we may also access list's elements


