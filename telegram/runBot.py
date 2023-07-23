import psutil
import time
import datetime
import schedule
from subprocess import Popen
import sys
from telebot.apihelper import ApiTelegramException


def runbot():
    for p in psutil.process_iter():
        if "python" not in p.name():
            continue
        if "python" in p.name() and "TelegramBotHalls" in p.cmdline()[1]:
            f = open("logbot.txt", "a")
            f.write(f"{datetime.datetime.now()} Выполнилось условие.. in .. in..\n")
            f.close()
            continue
        if "python" in p.name() and "TelegramBotHalls" not in p.cmdline()[1]:
            f = open("logbot.txt", "a")
            f.write(f"{datetime.datetime.now()} Выполнилось условие.. in .. not in..\n")
            f.write(f"{datetime.datetime.now()} Телеграм бот вновь запущен \n")
            f.write(f"{datetime.datetime.now()} Путь: {p.cmdline()[1]} \n")
            f.close()
            Popen([sys.executable, "TelegramBotHalls.py"])
            break

schedule.every(180).seconds.do(runbot)

while True:
    schedule.run_pending()
    time.sleep(1)