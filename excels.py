from openpyxl import load_workbook
from datetime import datetime
from plants import alarms_A

schedule_book = "./excel/Расписание.xlsm"
status_book   = "./excel/Cостояние.xlsx"
single=[] # This list contains a single schedule: the plant, the day, what to do, when to do.

# Clear the single[] list and pop up the tasks[] list
def refresh(tasks):
    single[0].replace(" ","")
    tasks.append(single.copy())                                                               # Append single[] list to the end of the tasks[] list
    single.clear()                                                                            # Clear the list

def readschedule(tasks):
    workbook = load_workbook(schedule_book)
    for j in range(53, 383, 10):
        for k in range(7):
            single.append(str(workbook.active.cell(row=j,         column=4).value))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=2).value))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=5).value))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=3).value))
            refresh(tasks)
            single.append(str(workbook.active.cell(row=j,         column=4).value))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=2).value))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=6).value))
            driers = str(workbook.active.cell(row=j, column=4).value)
            if driers == "79691782&did=33556432" or driers == "79691777&did=33555432":
                single.append("5")
            else:
                single.append("0")
            driers = ""
            refresh(tasks)
            single.append(str(workbook.active.cell(row=j,         column=4).value))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=2).value))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=8).value))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=10).value))
            refresh(tasks)
            single.append(str(workbook.active.cell(row=j,         column=4).value))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=2).value))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=9).value))
            driers = str(workbook.active.cell(row=j, column=4).value)
            if driers == "79691782&did=33556432" or driers == "79691777&did=33555432":
                single.append("5")
            else:
                single.append("0")
            driers = ""
            refresh(tasks)
    return tasks

def writestatus(alarms_A_list):
    statusbook=load_workbook(status_book)
    for i, j, k in range(len(alarms_A_list)), alarms_A_list:
        statusbook.active.cell(row=3+i, column=1).value = datetime.now().strftime("%d-%m-%Y")
        statusbook.active.cell(row=3+i, column=2).value = datetime.now().strftime("%H:%M")
        statusbook.active.cell(row=3+i, column=3).value = alarms_A_list[j]
        statusbook.active.cell(row=3+i, column=4).value = alarms_A_list[k]
    statusbook.save(status_book)
    #statusbook.active.cell(row=3 ,column=1).value=datetime.datetime.now().strftime("%d-%m-%Y")


if __name__ == "__main__":
    # emptytasks=[]
    # readschedule(emptytasks)
    # print(tasks)
    writestatus('12583680&did=33560432','123')

