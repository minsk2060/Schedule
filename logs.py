# The script makes a log of sent actions
# from datetime import datetime, timedelta
import datetime
from plants import plant
from pywinauto.application import Application
logs =[]
pathcur = "./logging/log_scheduling.txt"
pathall = "./logging/alllogs.txt"
def logall(logwrite):
    """запись в лог файл всех отправленных заданий"""
    logfile = open(pathall,"a")
    logfile.write("".join(logwrite)+"\n")
    logfile.close()

def closing():
    """закрытие лог файла, если на момент записи в него он открыт"""
    ntp = Application()
    try:
        ntp.connect(title_re="log_scheduling")
        ntp.window().close()
    except:
        pass


def logging(plantcode, act):
    closing()
    logwrite = [datetime.datetime.now().strftime("%d-%m-%Y  %H:%M  "),
                plant[f"{plantcode}"],
                acting(plantcode, act)]
    logall(logwrite)
    logs.append(logwrite)
    allwriting()


def acting (singlecode, whattodo):
    """определение действия"""
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


def partwriting(d):
    """запись последних заданий в лог файл"""
    f = open(pathcur, "w")
    b=[]
    for c in d:
        b.append(f'{"".join(c)}\n')
    f.write("".join(b))
    f.close()


def allwriting():
    """запись всех команд в лог файл"""
    f = open(pathall, "r")
    current = f.read().split("\n")
    d = []
    for i in range(len(current)-1):
        if datetime.datetime.now() - datetime.timedelta(days=2) < datetime.datetime.strptime(current[i][0:16], "%d-%m-%Y  %H:%M"):
            d.append(current[i])
        f.close()
    partwriting(d)