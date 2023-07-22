import psutil
import time
import datetime
import schedule
import subprocess
import sys


def runbot():
    for p in psutil.process_iter():
        if p.name() != "python.exe":
            continue
        elif "TelegramBotHalls.py" in p.cmdline()[1]:
            # f = open("logbot.txt", "a")
            # f.write(f"Телеграм бот работает нормально {datetime.datetime.now()}\n")
            # f.close()
            break
        else:
            f = open("logbot.txt", "a")
            f.write(f"Телеграм бот вновь запущен {datetime.datetime.now()}\n")
            f.close()
            subprocess.Popen([sys.executable, "TelegramBotHalls.py"])


schedule.every(10).seconds.do(runbot)

while True:
    schedule.run_pending()
    time.sleep(1)