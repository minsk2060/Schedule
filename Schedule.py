import webbrowser, schedule, time
from pyautogui import hotkey
from pywinauto.application import Application
from logs import logging
from excels import readschedule


print("РАБОТАЕТ УПРАВЛЕНИЕ ОБОРУДОВАНИЕМ ПО РАСПИСАНИЮ, НЕ ЗАКРЫВАЙТЕ ЭТО ОКНО")

tasks = []                                                                        # The list holds all the single[] lists  even the blank ones

# Sending the request to the browser string
def turn(get_plant, par):
    logging(get_plant, par)                                                       # Log this action in a log_scheduling.txt
    PREFX = "http://192.168.250.50/ajaxjson/bac/setValue?pid=85&oid="             # The common text in every request string
    app = Application(backend="uia")                                              # Get an object of the class
    app.window().set_focus()                                                      # Set focus on the browser window
    webbrowser.open_new_tab(PREFX + get_plant + par)                              # Make a request
    time.sleep(3)

    #hotkey("ctrl", "w")                                                           # Close the current browser window

def runschedule():                                                                # Call the function to start the process
    cleartasks = readschedule(tasks).copy()                                       # Call the function to read excel. Make a copy of the result list
    for t in range(len(tasks)):                                                   # Run through the list of all of the lists
        if tasks[t][2] == "None":                                                 # If there is no data in it
            cleartasks.remove(tasks[t])                                           # Delete a nested empty list
    schedule.clear()                                                              # Clear the previous schedule, cause it might been changed
    # Execute all the schedules
    for i in range(len(cleartasks)):
        exec(f"""schedule.every().{cleartasks[i][1]}.at('{cleartasks[i][2]}').do(turn,'{cleartasks[i][0]}','&vid=17&value={cleartasks[i][3]}')""")
<<<<<<< HEAD
=======
    schedule.every(10).minutes.do(runschedule)                                    # Repeat reading The schedule
>>>>>>> a0c2627dc35cd83a0ed3f857ba46c336e8623754


    # for i in cleartasks:
    #     print(i, len(i[0]), type(i[0]))
    cleartasks.clear()                                                            # Clear the list of no empty lines
    tasks.clear()

#runschedule()

schedule.every(1).minutes.do(runschedule)                                         # Repeat reading The schedule


while True:
    schedule.run_pending()
    time.sleep(1)






