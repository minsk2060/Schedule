from openpyxl import load_workbook

schedule_book="./excel/Расписание.xlsm"
single=[] # This list contains a single schedule: the plant, the day, what to do, when to do.

# Clear the single[] list and pop up the tasks[] list
def refresh(tasks):
    tasks.append(single.copy())                                                               # Append single[] list to the end of the tasks[] list
    single.clear()                                                                            # Clear the list

def readschedule(tasks):
    workbook = load_workbook(schedule_book)
    for j in range(53, 383, 10):
        for k in range(7):
            single.append(str(workbook.active.cell(row=j, column=4).value).replace(" ", ""))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=2).value))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=5).value))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=3).value))
            refresh(tasks)
            single.append(str(workbook.active.cell(row=j, column=4).value).replace(" ", ""))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=2).value))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=6).value))
            driers = str(workbook.active.cell(row=j, column=4).value.replace(" ", ""))
            if driers == "79691782&did=33556432" or driers == "79691777&did=33555432":
                single.append("5")
            else:
                single.append("0")
            driers = ""
            refresh(tasks)
            single.append(str(workbook.active.cell(row=j, column=4).value).replace(" ", ""))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=2).value))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=8).value))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=10).value))
            refresh(tasks)
            single.append(str(workbook.active.cell(row=j, column=4).value))
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
