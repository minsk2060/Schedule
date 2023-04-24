from openpyxl import load_workbook

schedule_book="./excel/Расписание.xlsm"
# tasks=[]
single=[]


def refresh(tasks):
    copysingle = single.copy()
    tasks.append(copysingle)
    single.clear()


def readschedule(tasks):
    workbook = load_workbook(schedule_book)
    for j in range(53, 383, 10):
        for k in range(7):
            single.append(str(workbook.active.cell(row=j, column=4).value))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=2).value))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=5).value))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=3).value))
            refresh(tasks)
            single.append(str(workbook.active.cell(row=j, column=4).value))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=2).value))
            single.append(str(workbook.active.cell(row=j + 1 + k, column=6).value))
            driers = str(workbook.active.cell(row=j, column=4).value)
            if driers == "79691782&did=33556432" or driers == "79691777&did=33555432":
                single.append("5")
            else:
                single.append("0")
            driers = ""
            refresh(tasks)
            single.append(str(workbook.active.cell(row=j, column=4).value))
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
    # Deleting empty tasks
    # cleartasks = tasks.copy()

    # for t in range(len(tasks)):
    #     if tasks[t][2] == "None":
    #         cleartasks.remove(tasks[t])
    # # schedule.clear()
    #
    # for i in range(len(cleartasks)):
    #     exec(f"""schedule.every().{cleartasks[i][1]}\
    #     .at('{cleartasks[i][2]}').do(turn, '{(cleartasks[i][0])}\
    #     ','&vid=17&value={cleartasks[i][3]}')""")
    # schedule.every(10).seconds.do(runschedule)
    # for i in cleartasks:
    #     print(i)

    # cleartasks.clear()
    # tasks.clear()


# readschedule()