import webbrowser, schedule, time
from pyautogui import hotkey
from pywinauto.application import Application
from logs import logging
from excels import readschedule


print("РАБОТАЕТ УПРАВЛЕНИЕ ОБОРУДОВАНИЕМ ПО РАСПИСАНИЮ, НЕ ЗАКРЫВАЙТЕ ЭТО ОКНО")

tasks = []                                                                        # The list holds all the single[] lists  even the blank ones

# Sending the request to the browser string
def turn(get_plant, par):
    PREFX = "http://192.168.250.50/ajaxjson/bac/setValue?pid=85&oid="             # The common text in every request string
    app = Application(backend="uia")                                              # Get an object of the class
    try:                                                                          # Cause any number of objects may be connected
        app.connect(title_re=".*Microsoft\u200b Edge", timeout=10)                # Connect to the first of them, doesn't matter
    except:
        pass                                                                      # Pass if there is more than one object
    app.window().set_focus()                                                      # Set focus on the browser window
    webbrowser.open_new_tab(PREFX + get_plant + par)                              # Make a request
    logging(get_plant, par)                                                       # Log this action in a log_scheduling.txt
    time.sleep(3)
    #hotkey("ctrl", "w")                                                           # Close the current browser window


# Reading the schedules and matching the list of them
def runschedule():                                                                # Call the function to start the process
    cleartasks = readschedule(tasks).copy()                                       # Call the function to read excel. Make a copy of the result list
    for t in range(len(tasks)):                                                   # Run through the list of all of the lists
        if tasks[t][2] == "None":                                                 # If there is no data in it
            cleartasks.remove(tasks[t])                                           # Delete a nested empty list
    # for i in cleartasks:
    #     print(i)
    schedule.clear()                                                              # Clear the previous schedule, cause it might been changed
    # Execute all the schedules
    for i in range(len(cleartasks)):
<<<<<<< HEAD
<<<<<<< HEAD
        exec(f"""schedule.every().{cleartasks[i][1]}\
        .at('{cleartasks[i][2]}').do(turn, '{(cleartasks[i][0])}','&vid=17&value={cleartasks[i][3]}')""")
    schedule.every(10).seconds.do(runschedule)
=======
        exec(f"""schedule.every().{cleartasks[i][1]}.at('{cleartasks[i][2]}').do(turn, '{(cleartasks[i][0])}','&vid=17&value={cleartasks[i][3]}')""")
=======
        exec(f"""schedule.every().{cleartasks[i][1]}.at('{cleartasks[i][2]}').do(turn,'{cleartasks[i][0]}','&vid=17&value={cleartasks[i][3]}')""")
>>>>>>> cfd9aa9d16011db517782d501bc378f6c6ec0444
    schedule.every(10).minutes.do(runschedule)                                    # Repeat reading The schedule

    cleartasks.clear()                                                            # Clear the list of no empty lines
<<<<<<< HEAD
    tasks.clear()                                                                 # Clear the list of all the lines
>>>>>>> ebe18050f6eeb10c993f0f976e2a597415318e6c
=======
    tasks.clear()
# Clear the list of all the lines
>>>>>>> cfd9aa9d16011db517782d501bc378f6c6ec0444


runschedule()


while True:
    schedule.run_pending()
    time.sleep(1)






