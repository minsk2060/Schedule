import datetime
from plants import plant
from pywinauto.application import Application

# logs =[]
pathcur = "./logging/log_scheduling.txt"
pathall = "./logging/alllogs.txt"
readlog = "./logging/readlogs.txt"

def log(plantcode, acting):
    """
    log()       -  основная функция логгирования"
    plantcode   -  код установки
    acting      -  действие в читаемом виде
    close()     -  закрытие лог файла, если на момент записи в него он открыт
    """
    close()
    logwrite = [datetime.datetime.now().strftime("%d-%m-%Y  %H:%M  "), plant[f"{plantcode}"], act(plantcode, acting)]
    logall(logwrite)
    sort()

def logall(logwrite):
    """
    logall()    -  запись в лог файл всех отправленных заданий построчно
    logwrite    -  текст задания, пример:   "17-05-2023  20:30  ПВ-2.6   Cтоп"
    logfile     -  файл alllogs.txt
    """
    logfile = open(pathall, "a")
    logfile.write("".join(logwrite)+"\n")
    logfile.close()

def close():
    """
    close()  - закрытие лог файла, если на момент записи в него он открыт
    try      - попытка найти открытый файл с заголовком "log_scheduling" и закрыть его
    """
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

def writelog(parttasks, partlogs):
    """
    writelog()  - запись в лог файл команд за заданный период
    abs()       - необходима для корректной вставки пустой строки при наступлении  нового месяца
    logtasks    - список для записи в файл log_scheduling.txt
    alllogs     - список для записи в файл alllogs.txt
    parttasks - список списков заданий за короткий заданный период
    partlogs  - список списков заданий за длинный заданный период
    в первом цикле также вставка пустой строки между разными датами
    """
    f = open(pathcur, "w")
    d = open(pathall, "w")
    logtasks=[]
    alllogs =[]
    for c in range(len(parttasks)):
        if c >= 1 :
            if abs(int(parttasks[c][0:2])-int(parttasks[c-1][0:2])) >= 1:
               logtasks.append('\n')
        logtasks.append(f'{"".join(parttasks[c])}\n')
    for c in range(len(partlogs)):
        alllogs.append(f'{"".join(partlogs[c])}\n')
    f.write("".join(logtasks))
    d.write("".join(alllogs))
    f.close()
    d.close()

def sort():
    """
    sort()    - сортировка команд за заданный период для записи в лог-файл
    current   - список из всех записей в alllogs, разделенный по символу переноса
    parttasks - список списков заданий за короткий заданный период
    partlogs  - список списков заданий за длинный заданный период
    в цикле проверка на предмет выдавать записи за несколько дней и ограничение всего периода записей"""
    f = open(pathall, "r")
    current = f.read().split("\n")
    parttasks = []
    partlogs  = []
    rightnow = datetime.datetime.now()
    for i in range(len(current)-1):
        logtime = datetime.datetime.strptime(current[i][0:16], "%d-%m-%Y  %H:%M")
        if rightnow - datetime.timedelta(days=1) <= logtime:
            parttasks.append(current[i])
        if rightnow - datetime.timedelta(days=10) < logtime:
            partlogs.append(current[i])
    f.close()
    writelog(parttasks, partlogs)

days={   "sunday": "Воскресенье",
         "monday": "Понедельник",
        "tuesday": "Вторник    ",
      "wednesday": "Среда      ",
       "thursday": "Четверг    ",
         "friday": "Пятница    ",
       "saturday": "Суббота    "}

def readlogs(logs_read):
    """
    readlogs()   - запись прочитанных заданий с расписаниями в лог файл readlogs.txt
    logs_read    - список списков , где нет пустых расписаний
    reads        - список прочитанных заданий за 7 дней для записи в файл readlogs.txt
    ttdys        - список прочитанных заданий за 2 дня для записи в файл readlogs.txt
    today        - текущий день недели в формате одной цифры
    yrday        - вчерашний день недели в формате одной цифры
    str_today    - текущий день недели
    str_yrday    - вчерашний день недели
    readlog      - путь к файлу readlogs.txt
    """
    reads = []
    ttdys = []
    today = datetime.datetime.now().date()
    yrday = today - datetime.timedelta(days=1)
    str_today = today.strftime("%A").lower()
    str_yrday = yrday.strftime("%A").lower()
    for i in logs_read:
        if i[1] == str_today or i[1] == str_yrday:
            ttdys.append(i)
    for i in ttdys:
        reads.append(f"{plant[i[0]]}   {''.join(days[i[1]])}   {''.join(i[2])} {(act(i[0], i[3]))} \n")
    f = open(readlog, "w")
    f.write("".join(reads))
    f.close()



if __name__ == "__main__":
    pass
    # pass
    # sort()
    # log('8388762&did=33560432',"0")
    # act('8388762&did=33560432',"0")
