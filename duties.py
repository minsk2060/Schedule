import datetime
def onduties():
    """Функция предусматривает определение кто сегодня на смене в хладоцентре."""
    dat = datetime.datetime().now() # определить сегодняшнюю дату
    d = dat.toordinal() % 4         # найти порядковый номер даты и найти остаток от деления на 4
    if datetime.time(8, 00) < dat.time() < datetime.time(23, 59): # определить период первой части смены (8:00...0:00)
        # Фамилия, результат деления для первой части смены и второй
        # Женя       0, 1
        # Александп  1, 2
        # Никита     2, 3
        # Юра        3, 0
        if d == 0:
            onduty = "Zhenia"
        elif d == 1:
            onduty = "Alexandr"
        elif d == 2:
            onduty = "Nikita"
        elif d == 3:
            onduty = "Yura"
    elif datetime.time(0, 00) < dat.time() < datetime.time(8, 00): # определить период второй части смены 0:00...8:00
        if d == 0:
            onduty = "Yura"
        elif d == 1:
            onduty = "Zhenia"
        elif d == 2:
            onduty = "Alexandr"
        elif d == 3:
            onduty = "Nikita"

    return onduty

factors = [["Yura", 3, 0], ["Zhenia" , 0, 1], ["Alexandr",1 , 2], ["Nikita", 2, 3]]