import calendar

for i in range(2000, 2051):
    if calendar.isleap(i):
        print(i, end = ' ')


