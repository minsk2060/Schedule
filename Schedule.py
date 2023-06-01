import webbrowser
import schedule
import time
from pyautogui import hotkey
from pywinauto.application import Application
from logs import log
from excels import readschedule
from request import switch


print("РАБОТАЕТ УПРАВЛЕНИЕ ОБОРУДОВАНИЕМ ПО РАСПИСАНИЮ, НЕ ЗАКРЫВАЙТЕ ЭТО ОКНО")

tasks = []

def browsing():
    """
    browsing()   - открытие и установка фокуса на окне браузера Edge
    app          - объект для подключения и установки фокуса на окне браузера Edge
    try/except:  - проверка на предмет на закрыт ли браузер, открытие
    """
    app =Application(backend ="uia")
    try:
        app.connect(title_re=u".*Microsoft\u200b Edge", timeout =10)
    except:
        app.start("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe")
        app.connect(title_re=u".*Microsoft\u200b Edge", timeout =10)
        webbrowser.open("http://192.168.250.50/svo/graphic?oid=121634830&did=-1&vid=80")
        time.sleep(3)
        hotkey("ctrl", "tab")
        hotkey("ctrl", "w")
        time.sleep(3)
    app.window().set_focus()


def turn(get_plant, par):
    """
    turn()       - выполнение действия (включить, выключить и т.п.)
    get_plant    - код установки для вставки в строку запроса
    par          - параметр ( 0 -стоп, 1 пуск и т.п.)
    logging()    - запись в лог файлы
    webbrowser   - отправка запроса в браузер
    time.sleep() - задержка времени
    hotkey()     - закрытие вкладки браузера с запросом
    browsing()   - управление браузером
    """
    log(get_plant, par)
    browsing()
    switch(get_plant, par)
    # webbrowser.open_new_tab("http://192.168.250.50/ajaxjson/bac/setValue?pid=85&oid=" + get_plant + par)
    # time.sleep(3)
    # hotkey("ctrl", "w")


def runschedule():
    """
    runschedule()    - получение расписания, улаоение пустых значений, компоновка задач и запуск действий по расписанию.
    readschedule()   - чтение расписания из excel файла принимает пустой список tasks, возвращает заполненный список
    cleartasks       - список, где не будет пустых расписаний
    tasks            - полный список расписаний, в т.ч. пустых
    schedule.clear() - очистка предыдущего  schedule, т.к. периодически происходит чтение и его формирование заново
    exec()           - автоматическая компоновка задачи для shedule
    """
    cleartasks = readschedule(tasks).copy()
    for t in range(len(tasks)):
        if tasks[t][2] == "None":
            cleartasks.remove(tasks[t])
    schedule.clear()
    for i in range(len(cleartasks)):
        exec(f"""schedule.every().{cleartasks[i][1]}.at('{cleartasks[i][2]}').do(turn,'{cleartasks[i][0]}','&vid=17&value={cleartasks[i][3]}')""")
    cleartasks.clear()
    tasks.clear()


schedule.every(10).seconds.do(runschedule)


while True:
    schedule.run_pending()
    time.sleep(1)






