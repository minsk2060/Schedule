import webbrowser, schedule, time
from pyautogui import hotkey
from pywinauto.application import Application
from logs import logging
from excels import readschedule


print("РАБОТАЕТ УПРАВЛЕНИЕ ОБОРУДОВАНИЕМ ПО РАСПИСАНИЮ, НЕ ЗАКРЫВАЙТЕ ЭТО ОКНО")

tasks = []

def turn(get_plant, par):
    PREFX = "http://192.168.250.50/ajaxjson/bac/setValue?pid=85&oid="
    app = Application(backend="uia")
    try:
        app.connect(title_re=".*Microsoft\u200b Edge", timeout=10)
    except:
        pass
    app.window().set_focus()
    webbrowser.open_new_tab(PREFX + get_plant + par)
    time.sleep(3)
    hotkey("ctrl", "w")
    logging(get_plant, par)


# Reading the schedules and matching the list of them
def runschedule():

    cleartasks = readschedule(tasks).copy()

    for t in range(len(tasks)):
        if tasks[t][2] == "None":
            cleartasks.remove(tasks[t])

    schedule.clear()

    for i in range(len(cleartasks)):
        exec(f"""schedule.every().{cleartasks[i][1]}\
        .at('{cleartasks[i][2]}').do(turn, '{(cleartasks[i][0])}\
        ','&vid=17&value={cleartasks[i][3]}')""")
    schedule.every(10).minutes.do(runschedule)

    cleartasks.clear()
    tasks.clear()

runschedule()


while True:
    schedule.run_pending()
    time.sleep(1)






