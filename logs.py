# The script makes a log of sent actions
from datetime import datetime, timedelta
from plants import plant

logs =[]


def logging(plantcode, act):

    logwrite = [datetime.now(),
                datetime.now().strftime("%d-%m-%Y  %H:%M  "),
                plant[f"{plantcode}"],
                acting(plantcode, act)]
    logs.append(logwrite)
    clearlogs = logs.copy()

    for i in range(len(logs)):
        if (datetime.now() - timedelta(days = 1)) > logs[i][0]:
            clearlogs.remove(logs[i])

    f = open("./logging/log_scheduling.txt", "w")
    b=""
    for c in clearlogs:
        b+=(f'{"".join(c[1:])}\n')
    f.write(b)
    f.close()

def acting (singlecode, whattodo):
    action = ""
    a = whattodo[-1:]
    # If other plants
    if   a == "1": action = "  Пуск на низкой скорости"
    elif a == "2": action = "  Пуск на высокой скорости"
    elif a == "0": action = "  Cтоп"
    # If swimming pool
    if singlecode == "8388883&did=33560432":
        if   a == "0": action = "  Выключение подсветки"
        elif a == "2": action = "  Включение желтой подсветки"
        elif a == "1": action = "  Включение синей подсветки"
    # If dryers
    elif singlecode == "79691782&did=33556432" or singlecode == "79691777&did=33555432":
        if   a == "5": action = "  Стоп"
        elif a == "1": action = "  Пуск в режиме хоккей"
        elif a == "2": action = "  Пуск в режиме фигурное катание"
    return action
