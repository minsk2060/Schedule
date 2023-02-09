import webbrowser, schedule, time
from pyautogui import hotkey
print("РАБОТАЕТ АВТОМАТИЧЕСКОЕ УПРАВЛЕНИЕ, НЕ ЗАКРЫВАЙТЕ ЭТО ОКНО")


def turn_light(par):
    webbrowser.open(f"http://192.168.250.50/ajaxjson/bac/setValue?pid=85&oid=8388883&did=33560432&vid=17&value={par}", new =0)
    time.sleep(3)
    hotkey('ctrl', 'w')
    hotkey('ctrl', 'ц')

def children_room(par):
    webbrowser.open(f"http://192.168.250.50/ajaxjson/bac/setValue?pid=85&oid=8388815&did=33561432&vid=17&value={par}", new =0)
    time.sleep(3)
    hotkey('ctrl', 'w')
    hotkey('ctrl', 'ц')

def sports_hall(par):
    webbrowser.open(f"http://192.168.250.50/ajaxjson/bac/setValue?pid=85&oid=8388827&did=33561432&vid=17&value={par}", new =0)
    webbrowser.open(f"http://192.168.250.50/ajaxjson/bac/setValue?pid=85&oid=8388835&did=33561432&vid=17&value={par}", new =0)
    time.sleep(3)
    hotkey('ctrl', 'w')
    hotkey('ctrl', 'ц')
    hotkey('ctrl', 'w')
    hotkey('ctrl', 'ц')



schedule.every().monday.at("07:00").do(turn_light,1)
schedule.every().monday.at("23:00").do(turn_light,0)
schedule.every().monday.at("17:00").do(children_room,2)
schedule.every().monday.at("19:00").do(children_room,0)


schedule.every().tuesday.at("07:00").do(turn_light,1)
schedule.every().tuesday.at("23:00").do(turn_light,0)
schedule.every().tuesday.at("17:00").do(children_room,2)
schedule.every().tuesday.at("19:00").do(children_room,0)


schedule.every().wednesday.at("07:00").do(turn_light,1)
schedule.every().wednesday.at("23:00").do(turn_light,0)
schedule.every().wednesday.at("17:00").do(children_room,2)
schedule.every().wednesday.at("19:00").do(children_room,0)


schedule.every().thursday.at("07:00").do(turn_light,1)
schedule.every().thursday.at("23:00").do(turn_light,0)
schedule.every().thursday.at("17:00").do(children_room,2)
schedule.every().thursday.at("19:00").do(children_room,0)


schedule.every().friday.at("07:00").do(turn_light,1)
schedule.every().friday.at("23:00").do(turn_light,0)
schedule.every().friday.at("17:00").do(children_room,2)
schedule.every().friday.at("19:00").do(children_room,0)
schedule.every().friday.at("15:00").do(sports_hall,2)
schedule.every().friday.at("21:45").do(sports_hall,0)


schedule.every().saturday.at("09:00").do(turn_light,1)
schedule.every().saturday.at("22:00").do(turn_light,0)
schedule.every().saturday.at("09:30").do(sports_hall,2)
schedule.every().saturday.at("13:00").do(sports_hall,0)


schedule.every().sunday.at("09:00").do(turn_light,1)
schedule.every().sunday.at("22:00").do(turn_light,0)
schedule.every().sunday.at("09:00").do(sports_hall,2)
schedule.every().sunday.at("21:00").do(sports_hall,0)


while True:
    schedule.run_pending()
    time.sleep(1)





#webbrowser.open(url_update, new=0)
"""включение света в будние в 7:00, в выходные в 9:00
выключение света в будние в 23:00 в выходные в 22:00"""