import psutil
import time
import datetime
import schedule
from subprocess import Popen
import sys
from telebot.apihelper import ApiTelegramException


def runbot():
    for p in psutil.process_iter():
        if p.name() != "python3.10.exe":
            #print(f"{datetime.datetime.now()} {p.name()}")
            continue
        elif p.name() == "python3.10.exe":
            print(f"{datetime.datetime.now()} {p.cmdline()[1]}")
            if "TelegramBotHalls.py" in p.cmdline()[1]:
                f = open("logbot.txt", "a")
                f.write(f"{datetime.datetime.now()} Телеграм бот работает нормально \n")
                f.close()
                break
            else:
                f = open("logbot.txt", "a")
                f.write(f"{datetime.datetime.now()} Телеграм бот вновь запущен \n")
                f.close()
                try:
                    Popen([sys.executable, "TelegramBotHalls.py"])
                except :
                    print(f"Ошибка ")
                    break

schedule.every(180).seconds.do(runbot)

while True:
    schedule.run_pending()
    time.sleep(1)