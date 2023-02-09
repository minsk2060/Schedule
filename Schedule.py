import webbrowser, schedule, time
from pyautogui import hotkey
from openpyxl import load_workbook


schedule_book="C:/Users/BMS/projects/schedules/Расписание.xlsm"
#schedule_book="C:/Users/Ev/Documents/Python/Sauter/Sauter_excel/Расписание.xlsm"
tasks=[]
single=[]

# Refreshing the list
def refresh():
    copysingle = single.copy()
    tasks.append(copysingle)
    single.clear()

def turn(get_plant, par):
    PREFX = "http://192.168.250.50/ajaxjson/bac/setValue?pid=85&oid="
    webbrowser.open(PREFX + get_plant + par, new=0, autoraise= True)
    time.sleep(3)
    hotkey('ctrl', 'w')
    hotkey('ctrl', 'ц')

# Reading the schedule and matching the list of them
def runschedule():
    workbook = load_workbook(schedule_book)
    for j in range(53, 383, 10):
        for k in range(7):
            single.append(str(workbook.active.cell(row=j,     column=4).value))
            single.append(str(workbook.active.cell(row=j+1+k, column=2).value))
            single.append(str(workbook.active.cell(row=j+1+k, column=5).value))
            single.append(str(workbook.active.cell(row=j+1+k, column=3).value))
            refresh()
            single.append(str(workbook.active.cell(row=j,     column=4).value))
            single.append(str(workbook.active.cell(row=j+1+k, column=2).value))
            single.append(str(workbook.active.cell(row=j+1+k, column=6).value))
            single.append("0")
            refresh()
            single.append(str(workbook.active.cell(row=j,     column=4).value))
            single.append(str(workbook.active.cell(row=j+1+k, column=2).value))
            single.append(str(workbook.active.cell(row=j+1+k, column=8).value))
            single.append(str(workbook.active.cell(row=j+1+k, column=10).value))
            refresh()
            single.append(str(workbook.active.cell(row=j,     column=4).value))
            single.append(str(workbook.active.cell(row=j+1+k, column=2).value))
            single.append(str(workbook.active.cell(row=j+1+k, column=9).value))
            single.append("0")
            refresh()

    # Deleting empty tasks
    cleartasks = tasks.copy()
    for t in range(len(tasks)):
        if tasks[t][2] == "None":
            cleartasks.remove(tasks[t])
    schedule.clear()
    for i in range(len(cleartasks)):
        exec(f"""schedule.every().{cleartasks[i][1]}.at('{cleartasks[i][2]}').do(turn, '{(cleartasks[i][0])}','&vid=17&value={cleartasks[i][3]}')""")
    schedule.every(10).minutes.do(runschedule)
    cleartasks.clear()
    tasks.clear()
    alljobs = schedule.get_jobs()
    print(alljobs)

runschedule()


while True:
    schedule.run_pending()
    time.sleep(1)






