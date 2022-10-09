import calendar
import datetime

for i in range(1, 13):
    newDate = datetime.datetime(datetime.datetime.now().year, i, 1)
    nameOfMonth = newDate.strftime("%B")
    numberOfDays = calendar.monthrange(newDate.year, newDate.month)[1]
    print(nameOfMonth, numberOfDays)
