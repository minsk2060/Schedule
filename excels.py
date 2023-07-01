from openpyxl import load_workbook
from datetime import datetime
from logs import logall, sort
#from plants import alarms_A
from TelegramBot import to_telegram
from ViberSet import to_viber

schedule_book = "./excel/Расписание.xlsm"
status_book   = "./excel/Cостояние.xlsx"
single=[] # This list contains a single schedule: the plant, the day, what to do, when to do.

# Clear the single[] list and pop up the tasks[] list
def refresh(tasks):
    """
    refresh()        - предобработка заданий с расписанием
    tasks            - полный список расписаний, в т.ч. пустых
    single           - по итогу список с одной задачей
    replace()        - исправление не корректного чтения
    """
    single[0].replace(" ", "")
    tasks.append(single.copy())
    single.clear()
    
def readschedule(tasks):
    """
    readschedule()   - чтение расписания из excel файла принимает пустой список tasks, возвращает заполненный список
    tasks            - полный список расписаний, в т.ч. пустых
    workbook         - работа с рабочей книгой excel
    refresh()        - предобработка заданий с расписанием
    """
    workbook = load_workbook(schedule_book)
    for j in range(53, 383, 10):
        for k in range(7):
            single.append(str(workbook.active.cell(row=j, column=4).value))
            for s in [2, 5, 3]:
                single.append(str(workbook.active.cell(row=j + 1 + k, column=s).value))
            #single.append(str(workbook.active.cell(row=j + 1 + k, column=5).value))
            #single.append(str(workbook.active.cell(row=j + 1 + k, column=3).value))
            refresh(tasks)
            for s in [4, 2, 6]:
                single.append(str(workbook.active.cell(row=j, column=s).value))
            #single.append(str(workbook.active.cell(row=j + 1 + k, column=2).value))
            #single.append(str(workbook.active.cell(row=j + 1 + k, column=6).value))
            driers = str(workbook.active.cell(row=j, column=4).value)
            if driers == "79691782&did=33556432" or driers == "79691777&did=33555432":
                single.append("5")
            else:
                single.append("0")
            driers = ""
            refresh(tasks)
            for s in [4, 2, 8, 10]:
                single.append(str(workbook.active.cell(row=j, column=s).value))
            #single.append(str(workbook.active.cell(row=j + 1 + k, column=2).value))
            #single.append(str(workbook.active.cell(row=j + 1 + k, column=8).value))
            #single.append(str(workbook.active.cell(row=j + 1 + k, column=10).value))
            refresh(tasks)
            for s in [4, 2, 9]:
                single.append(str(workbook.active.cell(row=j, column=s).value))
            #single.append(str(workbook.active.cell(row=j + 1 + k, column=2).value))
            #single.append(str(workbook.active.cell(row=j + 1 + k, column=9).value))
            driers = str(workbook.active.cell(row=j, column=4).value)
            if driers == "79691782&did=33556432" or driers == "79691777&did=33555432":
                single.append("5")
            else:
                single.append("0")
            driers = ""
            refresh(tasks)
    return tasks

def writestatus(i, plant, alarm, column):
    """
    writestatus()  - запись сведений об аварии в файл Состояние.xlsx
    i              - сдвиг номера строки для внесения записей в файл Состояние.xlsx
    plant          - имя установки, заносимое в файл Состояние.xlsx (например "ПВ-1.6")
    alarm          - запись об аварии, заносимая в файл Состояние.xlsx (например "Авария класса А")
    column         - номер колонки для записи в файл Состояние.xlsx
    statusbook     - объект для работы с файлом Состояние.xlsx
    date_now       - текущая дата, заносимая в файл Состояние.xlsx
    time_now       - текущее время, заносимая в файл Состояние.xlsx
    alarm_happen   - сторка типа "04-06-2023  11:00  ПВ-2.8   Авария класса А"
    logall()       - занесение события об аварии в лог файл alllogs.txt
    sort()         - занесение события об аварии в лог файл log_scheduling.txt
    to_telegram()  - отправка сообщения об аварии в чат бот в Телеграм
    to_viber()     - отправка сообщения об аварии в чат бот в Viber
    """
    statusbook = load_workbook(status_book)
    date_now = datetime.now().strftime("%d-%m-%Y")
    time_now = datetime.now().strftime("%H:%M")
    statusbook.active.cell(row=3+i, column=1).value = date_now
    statusbook.active.cell(row=3+i, column=2).value = time_now
    statusbook.active.cell(row=3+i, column=3).value = plant
    a = statusbook.active.cell(row=3+i, column=column).value
    if a != alarm:
        alarm_happen = [f"{date_now}  ", f"{time_now}  ", f"{plant}  ",  alarm]
        logall(alarm_happen)
        sort()
        logmsg = "\n".join(alarm_happen[2:])
        to_telegram(logmsg)
        to_viber(logmsg)
    statusbook.active.cell(row=3 + i, column=column).value = alarm
    statusbook.save(status_book)



