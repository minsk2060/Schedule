import webbrowser, schedule, time
from pyautogui import hotkey
from pywinauto.application import Application
from logs import logging
from excels import readschedule


print("РАБОТАЕТ УПРАВЛЕНИЕ ОБОРУДОВАНИЕМ ПО РАСПИСАНИЮ, НЕ ЗАКРЫВАЙТЕ ЭТО ОКНО")

tasks = []

def browsing():
    """
    browsing()  - установка фокуса на окне браузера Edge
    """
    app =Application(backend ="uia")
    app.connect(title_re=u".*Microsoft\u200b Edge", timeout =10)
    app.window().set_focus()


def turn(get_plant, par):
    """
    turn()       - выполнение действия (включить, выключить и т.п.)
    get_plant    - код установки для вставки в строку запроса
    par          - параметр ( 0 -стоп, 1 пуск и т.п.)
    logging()    - запись в лог файл
    app          - объект для подключения и установки фокуса на окне браузера Edge
    webbrowser   - отправка запроса в браузер
    time.sleep() - задержка времени
    hotkey()     - закрытие вкладки браузера с запросом
    """
    logging(get_plant, par)
    browsing()
    webbrowser.open_new_tab("http://192.168.250.50/ajaxjson/bac/setValue?pid=85&oid=" + get_plant + par)
    time.sleep(3)
    hotkey("ctrl", "w")


def runschedule():
    """
    runschedule()  - получение расписания, улаоение пустых значений,
                     компоновка задач и запуск действий по расписанию.
    readschedule() - чтение расписания из excel файла
                     принимает пустой список tasks, возвращает заполненный список
    cleartasks     - список, где не будет пустых значений

    """
    cleartasks = readschedule(tasks).copy()
    for t in range(len(tasks)):
        if tasks[t][2] == "None":
            cleartasks.remove(tasks[t])
    schedule.clear()
    for i in range(len(cleartasks)):
        exec(f"""schedule.every().{cleartasks[i][1]}.at('{cleartasks[i][2]}').do(turn,'{cleartasks[i][0]}','&vid=17&value={cleartasks[i][3]}')""")
    schedule.every(10).minutes.do(runschedule)
    cleartasks.clear()
    tasks.clear()


runschedule()


while True:
    schedule.run_pending()
    time.sleep(1)






