import telebot
from telegramtokens import telegramtoken_venthalls
from telebot import types
import requests
import time
from headers import header, sauter_cookie
#import Schedule
#from ..plants import ...


bot = telebot.TeleBot(telegramtoken_venthalls)
places = {"Игровой зал": "ПВ-2.7, ПВ-2.8",
          "Раздевалки игрового зала": "ПВ-2.4",
          "Зал хореографии 2015": "ПВ-2.5",
          "Зал хореографии 2041": "ПВ-2.6" }

schedules = {"Расписание  ПВ-2.7, ПВ-2.8":"",
             "Расписание  ПВ-2.4":"",
             "Расписание  ПВ-2.5":"",
             "Расписание  ПВ-2.6":"",}

curstates = {"Состояние  ПВ-2.7, ПВ-2.8":"",
             "Состояние  ПВ-2.4":"",
             "Состояние  ПВ-2.5":"",
             "Состояние  ПВ-2.6":"",}

startplant = {"Запуск  ПВ-2.7, ПВ-2.8": "",
              "Запуск  ПВ-2.4": "8388808&did=33561432",
              "Запуск  ПВ-2.5": "8388778&did=33560432",
              "Запуск  ПВ-2.6": "8388770&did=33560432",
              "Запуск  ПВ-2.7": "8388827&did=33561432",
              "Запуск  ПВ-2.8": "8388835&did=33561432",}

stopplant = {"Останов  ПВ-2.7, ПВ-2.8": "",
             "Останов  ПВ-2.4": "8388808&did=33561432",
             "Останов  ПВ-2.5": "8388778&did=33560432",
             "Останов  ПВ-2.6": "8388770&did=33560432",}

all_plants = {"ПВ-2.4": "8388808&did=33561432",
              "ПВ-2.5": "8388778&did=33560432",
              "ПВ-2.6": "8388770&did=33560432",
              "ПВ-2.7": "8388827&did=33561432",
              "ПВ-2.8": "8388835&did=33561432",}


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Игровой зал")
    btn2 = types.KeyboardButton("Раздевалки игрового зала")
    btn3 = types.KeyboardButton("Зал хореографии 2015")
    btn4 = types.KeyboardButton("Зал хореографии 2041")
    markup.add(btn3, btn4)
    markup.add(btn2)
    markup.add(btn1)
    bot.send_message(message.chat.id, text="Выберите помещение".format(message.from_user), reply_markup=markup)

def reply(message, place=""):
    answer = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(f"Состояние  {places[place]}")
    button2 = types.KeyboardButton(f"Расписание  {places[place]}")
    button3 = types.KeyboardButton(f"Запуск  {places[place]}")
    button4 = types.KeyboardButton(f"Останов  {places[place]}")
    button5 = types.KeyboardButton("Главное меню")
    answer.add(button1, button2)
    answer.add(button3, button4)
    answer.add(button5)
    #print(message.chat.id)
    bot.send_message(message.chat.id, "Выберите действие".format(message.from_user), reply_markup=answer)


@bot.message_handler(content_types=['text'])
def func(message):
    msg = message.text
    if msg == "Главное меню":
        start(message)

    # Информация
    elif msg in places.keys():
        time.sleep(1)
        bot.send_message(message.chat.id, text=f"{msg}\nобслуживает вентустановка  {places[msg]}")
        time.sleep(1)
        reply(message, msg)

    # Расписание
    elif msg in schedules.keys():
        bot.send_message(message.chat.id, text=f"Ждите, сейчас узнаем ...")
        time.sleep(5)
        path = "C:/Users/milli/Documents/Programming/Python/Projects/schedules/logging/readlogs.txt"
        f = open(path, "r")
        s = []
        for i in f.read().replace("   ", " ").split("\n"):
            s.append(i.split(" "))

        #Здесь необходимо вставить код для опроса расписания работы
        bot.send_message(message.chat.id, text=f"{msg} на ближайшие пару дней:\n...\n...\n...")
        bot.send_message(message.chat.id, "Выберите действие")

    # Состояние
    elif msg in curstates.keys():
        bot.send_message(message.chat.id, text=f"Ждите, идет опрос ...")
        time.sleep(5)
        #Здесь необходимо вставить код для опроса состояия вентустановки
        bot.send_message(message.chat.id, text=f"Текущее {msg} :\n...\n...\n...")
        bot.send_message(message.chat.id, "Выберите действие")

    # Запуск
    elif msg in startplant.keys():
        p = "1"
        bot.send_message(message.chat.id, "Стартуем....")
        time.sleep(5)
        switch_plant(message, msg, p, "Запуск")

    # Останов
    elif msg in stopplant.keys():
        p = "0"
        bot.send_message(message.chat.id, "Останавливаемся....")
        time.sleep(5)
        switch_plant(message, msg, p, "Останов")
        # g = stopplant[msg]
        # p = "0"
        # url = f"http://192.168.250.50/ajaxjson/bac/setValue?pid=85&oid={g}&vid=17&value={p}"
        # r = requests.get(url, headers=header, cookies=sauter_cookie)
        # stmsg = "не выполнен"
        # if r:
        #     if '"message":"Value was successfully written"' in r.text:
        #         stmsg = "выполнен успешно"
        # time.sleep(5)
        # bot.send_message(message.chat.id, f"{msg} {stmsg}")

    # Иное
    else:
        bot.send_message(message.chat.id, text="Что за команда, не понял?")
        time.sleep(2)
        bot.send_message(message.chat.id, text="Чувак, здесь не надо набирать текст \nПросто жмем кнопки")
        time.sleep(3)
        bot.send_message(message.chat.id, text="Идем на главную")
        time.sleep(1)
        start(message)


def switch_plant(message, msg, p, action):
    if "ПВ-2.7, ПВ-2.8" in msg:
        ssg = f"{action}  ПВ-2.7"
        bot.send_message(message.chat.id, ssg)
        g = all_plants[ssg.replace(f"{action}  ", "")]
        bot.send_message(message.chat.id, f"{ssg} {do_switch(g, p)}")

        psg = f"{action}  ПВ-2.8"
        bot.send_message(message.chat.id, psg)
        g = all_plants[psg.replace(f"{action}  ", "")]
        bot.send_message(message.chat.id, f"{psg} {do_switch(g, p)}")


    else:
        g = all_plants[msg.replace(f"{action}  ", "")]
        # url = f"http://192.168.250.50/ajaxjson/bac/setValue?pid=85&oid={g}&vid=17&value={p}"
        # r = requests.get(url, headers=header, cookies=sauter_cookie)
        # stmsg = "не выполнен"
        # if r:
        #     if '"message":"Value was successfully written"' in r.text:
        #         stmsg = "выполнен успешно"
        # time.sleep(5)
        bot.send_message(message.chat.id, f"{msg} {do_switch(g, p)}")

def do_switch(g, p):
    url = f"http://192.168.250.50/ajaxjson/bac/setValue?pid=85&oid={g}&vid=17&value={p}"
    r = requests.get(url, headers=header, cookies=sauter_cookie)
    time.sleep(5)
    if '"message":"Value was successfully written"' in r.text:
        stmsg = "выполнен успешно"
    else:
        stmsg = "не выполнен"
    return stmsg



bot.polling(none_stop=True, timeout=86400, long_polling_timeout=86400)

