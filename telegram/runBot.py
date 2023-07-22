import psutil, time, datetime

while True:
    time.sleep(30)
    for p in psutil.process_iter():
        if "python" in p.name():
            for i in p.cmdline():
                # print(i)
                if "TelegramBotHalls.py" not in i:
                    import TelegramBotHalls
                    now = datetime.datetime.now()
                    f = open("logbot.txt", "a")
                    f.write(f"Телеграм бот вновь запущен {now}\n")
                    f.close()
