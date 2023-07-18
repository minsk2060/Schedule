import schedule
import time
from logs import log, readlogs
from excels import readschedule
from request import switch, getalarms
from plants import alarms_A, alarms_BC



print("РАБОТАЕТ УПРАВЛЕНИЕ ОБОРУДОВАНИЕМ ПО РАСПИСАНИЮ, НЕ ЗАКРЫВАЙТЕ ЭТО ОКНО")

tasks = []

def turn(get_plant, par):
    """
    turn()       - выполнение действия (включить, выключить и т.п.)
    get_plant    - параметр для формирования url, определяющий код установки
    par          - параметр для формирования url, определяющий действие ( 0 -стоп, 1 пуск и т.п.)
    log()        - запись отправленных команд в лог файлы
    switch()     - выполнение запроса на сервер при помощи библиотеки requests
    """
    log(get_plant, par)
    switch(get_plant, par)

def runschedule():
    """
    runschedule()    - получение расписания, удаление пустых значений, компоновка задач и запуск действий по расписанию.
    readschedule()   - чтение расписания из excel файла принимает пустой список tasks, возвращает заполненный список
    cleartasks       - список, где не будет пустых расписаний
    tasks            - полный список расписаний, в т.ч. пустых
    clear('cleared') - очистка предыдущего  schedule c тегом 'cleared', т.к. периодически происходит чтение и его формирование заново
    exec()           - автоматическая компоновка задачи для функции schedule
    """
    clearlogs = readschedule(tasks)
    cleartasks = clearlogs.copy()
    for t in range(len(tasks)):
        if tasks[t][2] == "None":
            cleartasks.remove(tasks[t])
    schedule.clear('cleared')
    for i in range(len(cleartasks)):
        exec(f"schedule.every().{cleartasks[i][1]}.at('{cleartasks[i][2]}').do(turn,'{cleartasks[i][0]}','&vid=17&value={cleartasks[i][3]}').tag('cleared')")
    readlogs(cleartasks)
    cleartasks.clear()
    tasks.clear()


schedule.every(1).minutes.do(runschedule)
schedule.every(13).minutes.do(getalarms, alarms_dict=alarms_A,  column_number=4, alarm_text='Авария класса А')
schedule.every(23).minutes.do(getalarms, alarms_dict=alarms_BC, column_number=5, alarm_text='Авария класса B,C')


while True:
    schedule.run_pending()
    time.sleep(1)






