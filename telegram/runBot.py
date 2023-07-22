import psutil, time, datetime
import schedule
import TelegramBotHalls
# from TelegramBotHalls import bot

def runbot():
    for p in psutil.process_iter():
        if "python" in p.name():
            for i in p.cmdline():
                if "TelegramBotHalls.py" in i:
                    print("123")
                    print(i)
                    continue
                else:
                    f = open("logbot.txt", "a")
                    f.write(f"Телеграм бот вновь запущен {datetime.datetime.now()}\n")
                    f.close()
                    # bot.polling(none_stop=True, timeout=600, long_polling_timeout=600)
                    import TelegramBotHalls

schedule.every(1).minutes.do(runbot)

while True:
    schedule.run_pending()
    time.sleep(1)