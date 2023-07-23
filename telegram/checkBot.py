import runpy
import psutil
import time
import datetime
import schedule
# from subprocess import Popen
# import sys
from telebot.apihelper import ApiTelegramException

def log(text):
    f=open("logbot.txt", "a")
    f.write(f'{datetime.datetime.now()} {text}')
    f.close()

def runbot():
   for p in psutil.process_iter():
        if "ython" not in p.name():
            continue
        if "ython" in p.name() and "TelegramBotHalls" in p.cmdline()[1]:
            log('Бот работает \n')
            break
        if "ython" in p.name() and "TelegramBotHalls" not in p.cmdline()[1]:
            log('Бот стоит \n')
            try:
                log('Попытка запуска \n')
                runpy.run_module("runBot")
                # runpy.run_module("TelegramBotHalls")
                log('Попытка запуска прошла успешно\n')
                time.sleep(60)
                break
            except:
                log('Ошибка запуска \n')
                break



schedule.every(20).seconds.do(runbot)

while True:
    schedule.run_pending()
    time.sleep(1)
