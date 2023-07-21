import psutil, time

while True:
    time.sleep(10)
    for p in psutil.process_iter():
        if "python" in p.name():
            for i in p.cmdline():
                if "TelegramBotHalls.py" not in i:
                    import TelegramBotHalls
