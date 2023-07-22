import psutil, time, datetime

while True:
    time.sleep(10)
    for p in psutil.process_iter():
        if "python" in p.name():
            for i in p.cmdline():
                if "TelegramBotHalls.py" not in i:
                    import TelegramBotHalls
                    f = open("logbot.txt", "a")
                    now = datetime.datetime.now().strftime("%Y" "%h" "%m")
                    f.write(f"Телеграм бот вновь запущен {now}\n")
                    f.close()
