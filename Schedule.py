import webbrowser, schedule, time
from pyautogui import hotkey
from pywinauto.application import Application
from logs import logging
from excels import readschedule


print("РАБОТАЕТ УПРАВЛЕНИЕ ОБОРУДОВАНИЕМ ПО РАСПИСАНИЮ, НЕ ЗАКРЫВАЙТЕ ЭТО ОКНО")

schedule_book="./excel/Расписание.xlsm"
tasks=[]
single=[]


# Refreshing the list
def refresh():
    copysingle = single.copy()
    tasks.append(copysingle)
    single.clear()

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
    # readschedule(tasks)
    # workbook = load_workbook(schedule_book)
    # for j in range(53, 383, 10):
    #     for k in range(7):
    #         single.append(str(workbook.active.cell(row=j,     column=4).value))
    #         single.append(str(workbook.active.cell(row=j+1+k, column=2).value))
    #         single.append(str(workbook.active.cell(row=j+1+k, column=5).value))
    #         single.append(str(workbook.active.cell(row=j+1+k, column=3).value))
    #         refresh()
    #         single.append(str(workbook.active.cell(row=j,     column=4).value))
    #         single.append(str(workbook.active.cell(row=j+1+k, column=2).value))
    #         single.append(str(workbook.active.cell(row=j+1+k, column=6).value))
    #         driers = str(workbook.active.cell(row=j, column=4).value)
    #         if driers == "79691782&did=33556432" or driers == "79691777&did=33555432":
    #             single.append("5")
    #         else:
    #             single.append("0")
    #         driers = ""
    #         refresh()
    #         single.append(str(workbook.active.cell(row=j,     column=4).value))
    #         single.append(str(workbook.active.cell(row=j+1+k, column=2).value))
    #         single.append(str(workbook.active.cell(row=j+1+k, column=8).value))
    #         single.append(str(workbook.active.cell(row=j+1+k, column=10).value))
    #         refresh()
    #         single.append(str(workbook.active.cell(row=j,     column=4).value))
    #         single.append(str(workbook.active.cell(row=j+1+k, column=2).value))
    #         single.append(str(workbook.active.cell(row=j+1+k, column=9).value))
    #         driers = str(workbook.active.cell(row=j, column=4).value)
    #         if driers == "79691782&did=33556432" or driers == "79691777&did=33555432":
    #             single.append("5")
    #         else:
    #             single.append("0")
    #         driers = ""
    #         refresh()

    # Deleting empty tasks
    cleartasks = readschedule(tasks).copy()

    for t in range(len(tasks)):
        if tasks[t][2] == "None":
            cleartasks.remove(tasks[t])

    for i in cleartasks:
        print (i)

    schedule.clear()

    for i in range(len(cleartasks)):
        exec(f"""schedule.every().{cleartasks[i][1]}\
        .at('{cleartasks[i][2]}').do(turn, '{(cleartasks[i][0])}\
        ','&vid=17&value={cleartasks[i][3]}')""")
    schedule.every(10).seconds.do(runschedule)

    cleartasks.clear()
    tasks.clear()

runschedule()


while True:
    schedule.run_pending()
    time.sleep(1)






