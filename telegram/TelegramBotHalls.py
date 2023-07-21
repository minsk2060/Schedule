import telebot
from telegramtokens import telegramtoken_venthalls
from telebot import types
import requests
import time
from headers import header, sauter_cookie


bot = telebot.TeleBot(telegramtoken_venthalls)
places = {"Игровой зал": "ПВ-2.7, ПВ-2.8",
          "Раздевалки игрового зала": "ПВ-2.4",
          "Зал хореографии 2015": "ПВ-2.5",
          "Зал хореографии 2041": "ПВ-2.6" }

all_plants = {"ПВ-2.4": "8388808&did=33561432",
              "ПВ-2.5": "8388778&did=33560432",
              "ПВ-2.6": "8388770&did=33560432",
              "ПВ-2.7": "8388827&did=33561432",
              "ПВ-2.8": "8388835&did=33561432",}

starts    = ["Запуск  " + x for x in places.values()]
stops     = ["Останов  " + x for x in places.values()]
curstates = ["Состояние  " + x for x in places.values()]
scheds    = ["Расписание  " + x for x in places.values()]


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


@bot.callback_query_handler(func=lambda callback: callback.data in ['1', '2'])
def check_speed(callback):
    tex = callback.message.text.replace("Выберите скорость работы вентустановки", "Запуск ")
    bot.send_message(callback.message.chat.id, f"Стартуем.... ")
    switch_plant(callback.message, tex, callback.data, "Запуск")


@bot.message_handler(content_types=['text'])
def func(message):
    m = message.chat.id
    msg = message.text
    if msg == "Главное меню":
        start(message)
    # Информация
    elif msg in places.keys():
        #time.sleep(1)
        sms(m, f"{msg}\nобслуживает вентустановка  {places[msg]}")
        #bot.send_message(message.chat.id, text=f"{msg}\nобслуживает вентустановка  {places[msg]}")
        #time.sleep(1)
        reply(message, msg)
    # Расписание
    elif msg in scheds:
        sms(m, f"Ждите, сейчас узнаем ...")
        #bot.send_message(message.chat.id, text=f"Ждите, сейчас узнаем ...")
        time.sleep(4)
        plt = msg[-6:]
        fil = open("../logging/readlogs.txt", "r")
        sts = []
        als = fil.read().split("\n")
        for i in als:
            if plt in i:
                sts.append(i.replace(f"{plt}    ", ""))
        prn = "\n".join(sts).replace("\n","\n\n").replace("0   ", "0\n")
        sms(m, f'{msg} на эти дни:\n\n{prn}')
        sms(m, "Выберите действие")
        #bot.send_message(message.chat.id, text=f'{msg} на эти дни:\n\n{prn}')
        #bot.send_message(message.chat.id, "Выберите действие")
    # Состояние
    elif msg in curstates:
        sms(m, f"Ждите, идет опрос ...")
        #bot.send_message(message.chat.id, text=f"Ждите, идет опрос ...")
        #time.sleep(5)
        #Здесь необходимо вставить код для опроса состояия вентустановки
        sms(m, f"Текущее {msg} :\n...\n...\n...")
        sms(m,"Выберите действие")
        #bot.send_message(message.chat.id, text=f"Текущее {msg} :\n...\n...\n...")
        #bot.send_message(message.chat.id, "Выберите действие")
    # Запуск
    elif msg in starts:
        markup = types.InlineKeyboardMarkup()
        button2 = types.InlineKeyboardButton("Низкая", callback_data="1")
        button1 = types.InlineKeyboardButton("Высокая", callback_data="2")
        markup.add(button2, button1)
        mes = "Выберите скорость работы вентустанов"
        if "ПВ-2.7" in msg:
            bot.send_message(message.chat.id, f"{mes}ок {msg[-14:]}", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, f"{mes}ки {msg[-6:]}", reply_markup=markup)
    # Останов
    elif msg in stops:
        p = "0"
        sms(m, "Останавливаемся....")
        #bot.send_message(message.chat.id, "Останавливаемся....")
        #time.sleep(5)
        switch_plant(message, msg, p, "Останов")
    # Иное
    else:
        sms(m, "Что за команда, не понял?" )
        sms(m, "Чувак, здесь не надо набирать текст \nПросто жмем кнопки")
        sms(m, "Идем на главную")
        start(message)



def sms(m, t):
    bot.send_message(m, t)
    time.sleep(4)


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
    bot.send_message(message.chat.id, "Выберите действие".format(message.from_user), reply_markup=answer)


bot.polling(none_stop=True, timeout=600, long_polling_timeout=600)
