from datetime import datetime, timedelta, date
# Вычисление даты трехдневной давности
curtime = datetime.now()
lastime = (curtime - timedelta(days=3))

# print(curtime.strftime("%d-%m-%Y  %H:%M"))
# print(lastime.strftime("%d-%m-%Y  %H:%M"))

c = datetime(2023,12,12,12,12)
b = datetime(2022,12,12,12,12)

print(c-b, type(c-b))
