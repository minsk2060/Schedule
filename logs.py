# The script makes a log of sent actions
import datetime
from plants import plant
from pywinauto.application import Application

logs =[]
pathcur = "./logging/log_scheduling.txt"
pathall = "./logging/alllogs.txt"

def log(plantcode, acting):
    close()
    logwrite = [datetime.datetime.now().strftime("%d-%m-%Y  %H:%M  "), plant[f"{plantcode}"], act(plantcode, acting)]
    logall(logwrite)
    logs.append(logwrite)
    sort()

def logall(logwrite):
    """запись в лог файл всех отправленных заданий"""
    logfile = open(pathall, "a")
    logfile.write("".join(logwrite)+"\n")
    logfile.close()

def close():
    """закрытие лог файла, если на момент записи в него он открыт"""
    ntp = Application()
    try:
        ntp.connect(title_re="log_scheduling")
        ntp.window().close()
    except:
        pass

def act (singlecode, whattodo):
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

def writelog(parttasks):
    """запись в лог файл команд за последние несколько дней"""
    f = open(pathcur, "w")
    logtasks=[]
    for c in range(len(parttasks)):
        if c >= 1 :
            if int(parttasks[c][0:2])-int(parttasks[c-1][0:2]) >= 1:
               logtasks.append('\n')

        logtasks.append(f'{"".join(parttasks[c])}\n')
    f.write("".join(logtasks))
    f.close()

def sort():
    """сортировка для записи в лог файл команд за последнее несколько дней"""
    f = open(pathall, "r")
    current = f.read().split("\n")
    parttasks = []
    for i in range(len(current)-1):
        if datetime.datetime.now() - datetime.timedelta(days=3) < datetime.datetime.strptime(current[i][0:16], "%d-%m-%Y  %H:%M"):
            parttasks.append(current[i])
        f.close()
    writelog(parttasks)

if __name__ == "__main__":
    sort()
    log('8388762&did=33560432',"0")
    act('8388762&did=33560432',"0")