import datetime

# Фамилия, результат деления для первой части смены и второй
# Вульфов  1, 2
# Клышко   2, 3
# Басыров  3, 0
# Федорчук 0, 1

b = datetime.datetime(2023, 5, 31, 7, 10)
d = b.toordinal() % 4
if datetime.time(8, 00) < b.time() < datetime.time(23, 59):
    half = "first"
elif datetime.time(0, 00) < b.time() < datetime.time(8, 00):
    half = "second"
def onduties():
    if datetime.time(8, 00) < b.time() < datetime.time(23, 59):
        if d == 1:
            onduty = "Alexandr"
        elif d ==  2:
            onduty = "Nikita"
        elif d == 3:
            onduty = "Yura"
        elif d == 0:
            onduty = "Zhenia"
    elif datetime.time(0, 00) < b.time() < datetime.time(8, 00):
        if d == 2:
            onduty = "Alexandr"
        elif d == 3:
            onduty = "Nikita"
        elif d == 0:
            onduty = "Yura"
        elif d == 1:
            onduty = "Zhenia"
    return onduty

