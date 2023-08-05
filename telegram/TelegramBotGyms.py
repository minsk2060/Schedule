import telebot
from telegramtokens import telegramtoken_ventgyms
from telebot import types
import requests
import time
from headers import header, header_alarm_A, sauter_cookie
from plants import alarms_A, alarms_BC
from helpmsg import helpmsg_gyms

bot = telebot.TeleBot(telegramtoken_ventgyms)

# Наименования оборудования
places = {"Игровая комната": "ПВ-2.9",
          "Раздевалки залов": "ПВ-2.15",
          "Тренажерный зал": "ПВ-2.12",
          "Зал Ёги": "ПВ-2.11"}

# Парметры для запроса к оборудованию
all_plants = {"ПВ-2.11": "8388739&did=33559432",
              "ПВ-2.12": "8388750&did=33559432",
              "ПВ-2.15": "8388845&did=33559432",
              "ПВ-2.9": "8388815&did=33561432", }

# Состояния работы
states = {"2": "работает на высокой скорости",
          "1": "работает на низкой скорости",
          "0": "остановлена",
          "3": "работает на низкой скорости", }

# Сообщения - команды
starts = ["Запуск  " + x for x in places.values()]
stops = ["Останов  " + x for x in places.values()]
curstates = ["Состояние  " + x for x in places.values()]
scheds = ["Расписание  " + x for x in places.values()]


def alrm_params(alrm_dict):
    """ Преобразование с целью получения параметров для запроса

    :param alrm_dict: словарь с параметрами (...'12583575&did=33559432':  'ПВ-2.9 ',)
    :return:          словарь с корректными параметрами (...'ПВ-2.9': '12583575&did=33559432')
    """
    return {v.replace(" ", ""): k for k, v in alrm_dict.items()
            if v.replace(" ", "") in all_plants.keys()}



@bot.message_handler(commands=['help'])
def help(message):
    """
    Обработчик сообщения "help"

    :param message: объект "сообщение" (содержит в т.ч. текст сообщения)
    """
    uid = message.chat.id
    if root(uid):
        sms(uid, helpmsg_gyms)
    else:
        no_root(uid)


@bot.message_handler(commands=['start'])
def start(message):
    """
    Обработчик сообщений, поступающих после команды "start"

    :param message: объект "сообщение" (содержит в т.ч. текст сообщения)
    """
    uid = message.chat.id
    if root(uid):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Игровая комната")
        btn2 = types.KeyboardButton("Раздевалки залов")
        btn3 = types.KeyboardButton("Тренажерный зал")
        btn4 = types.KeyboardButton("Зал Ёги")
        markup.add(btn3, btn4)
        markup.add(btn2)
        markup.add(btn1)
        bot.send_message(uid, "Выберите помещение", reply_markup=markup)
    else:
        no_root(uid)


@bot.callback_query_handler(func=lambda callback: callback.data in ['1', '2'])
def check_speed(callback):
    uid = callback.message.chat.id
    if root(uid):
        tex = callback.message.text.replace("Выберите скорость работы", "Запуск ")
        sms(uid,  "Стартуем.... ", 4)
        switch_plant(callback.message, tex, callback.data, "Запуск")
    else:
        no_root(uid)


@bot.message_handler(content_types=['text'])
def func(message):
    uid = message.chat.id

    # Проверка прав доступа
    if root(uid):
        msg = message.text
        if msg == "Главное меню":
            start(message)

        pv = 0
        if "ПВ" in message.text:
            pv = message.text.index("ПВ")

        # Информация
        elif msg in places.keys():
            vor = "обслуживается вентустановкой"
            sms(uid, f"{msg}\n{vor}  {places[msg]}", 1)
            reply(message, msg)

        # Расписание
        elif msg in scheds:
            sms(uid, f"Ждите, сейчас узнаем ...", 4)
            fil = open("../logging/readlogs.txt", "r")
            sts = []
            for i in fil.read().split("\n"):
                if msg[pv:] in i:
                    sts.append(i.replace(f"{msg[:pv]}    ", ""))
            prn = "\n".join(sts).replace("\n", "\n\n").replace("0   ", "0\n")
            if prn == "":
                prn = "не задано"
            sms(uid, f'{msg}\nна эти дни:\n\n{prn}', 1)
            sms(uid)

        # Состояние
        elif msg in curstates:
            sms(uid, f"Ждите, идет опрос ...", 2)
            sms(uid, f"В текущий момент установка"
                   f" {msg[pv:]}  {get_state(msg[pv:])}."
                   f"{get_alarm(msg[pv:], alrm_params(alarms_BC), 'Авария класса ВС')}"
                   f"{get_alarm(msg[pv:], alrm_params(alarms_A),  'Авария класса А')}", 2)
            sms(uid)

        # Запуск
        elif msg in starts:
            markup = types.InlineKeyboardMarkup()
            button2 = types.InlineKeyboardButton("Низкая", callback_data="1")
            button1 = types.InlineKeyboardButton("Высокая", callback_data="2")
            markup.add(button2, button1)
            mes = "Выберите скорость работы"
            bot.send_message(message.chat.id, f"{mes} {msg[pv:]}", reply_markup=markup)

        # Останов
        elif msg in stops:
            p = "0"
            sms(uid, "Останавливаемся....", 3)
            switch_plant(message, msg, p, "Останов")

        # Иное
        else:
            start(message)
    else:
        no_root(uid)


def sms(uid, t="Выберите действие", s=0):
    """
    Отправка текстовых сообщений в бот

    :param uid: идентификатор адресата сообщения (chat.id)
    :param t:   текст сообщения (по умолчанию - "Выберите действие")
    :param s:   задержка времени после отправки сообщения
    """
    bot.send_message(uid, t)
    time.sleep(s)


def switch_plant(message, msg, p, action):
    """
    Подготовка к выполнению действия над вентустановкой

    :param message: объект "сообщение", содержит в т.ч. текст полученного сообщения
    :param msg:     текст полученного сообщения
    :param p:       параметр, определяющий действие (0-стоп, 1-запуск на низкой и т.п.)
    :param action:  текст, соответствующий действию ("Запуск", "Останов" и т.п)
    """
    g = all_plants[msg.replace(f"{action}  ", "")]
    pv = msg.index("ПВ")
    bot.send_message(message.chat.id, f"{msg} {do_switch(g, p, msg[pv:])}")


def do_switch(g, p, plt):
    """
    Выполнение действия над вентустановкой

    :param g:    параметр, определяющий адрес установки для формирования строки запроса
    :param p:    параметр, определяющий действие (0-стоп, 1-запуск на низкой и т.п.)
    :param plt:  наименование установки (ПВ-2.9, ПВ-2.11 и т.п.)
    """
    stmsg = "не выполнен.\n"
    url = f"http://192.168.250.50/ajaxjson/bac/setValue?pid=85&oid={g}&vid=17&value={p}"
    if check_alarm(plt):
        stmsg = stmsg + "Авария класса А"
    else:
        r = requests.get(url, headers=header_alarm_A, cookies=sauter_cookie)
        time.sleep(4)
        if '"message":"Value was successfully written"' in r.text:
            stmsg = "выполнен успешно.\n "
    return stmsg


def get_state(plt):
    """
    Получение состояния вентустановки

    :param plt:  наименование установки (ПВ-2.9, ПВ-2.11 и т.п.)
    :return:     полученное состояние вентустановки (работает, остановено, в аварии и т.п.)
    """
    url = f"http://192.168.250.50/svo/details/?oid={all_plants[plt]}&vid=17&mode=cached"
    resp = requests.get(url, headers=header_alarm_A, cookies=sauter_cookie)
    time.sleep(3)
    r = resp.text
    n = r[r.index('<tr data-pid="85">')+18:]
    e = n[:n.index('</tr>')]
    g = e[e.index("property-value")+16]
    return states[g]


def get_alarm(plt, dic, txt):
    """
    Получения сведений о возможной аварии вентустановки

    :param plt:   наименование вентустановки (например "ПВ-2.9")
    :param dic:   словарь с параметрами для строки запроса
    :param txt:   текст сообщения об аварии
    :return:      текст сообщения об аварии (например "Авария класса А")
    """
    url = f"http://192.168.250.50/svo/details/update?oid={dic[plt]}&vid=17&mode=cached"
    resp = requests.get(url, headers=header, cookies=sauter_cookie)
    time.sleep(3)
    almsg = ""
    if "Alarm: true" in resp.text:
        if 'title="Fault: true"' not in resp.text:
            almsg = txt
    return almsg


def check_alarm(plt):
    """
    Проверка на наличие аварии перед пуском

    :param plt: наименование вентустановки (например "ПВ-2.9")
    :return:    True - есть авария, False - нет аварии
    """
    alm = 'Авария класса А'
    if get_alarm(plt, alrm_params(alarms_A), alm) == alm:
        return True
    return False


def reply(message, place=""):
    """
    Обработчик сообщения "выберите действие"

    :param message: объект "собщение" (например "Состояние ПВ-2.9")
    :param place:   наименование помещения (например "Игровая комната")
    """
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


def root(uid):
    """
    Идентификация пользователоей

    :param uid:  идентификатор пользователя (chat.id)
    :return:     True если пользователь в списке пользователей
    """
    return True   # if str(uid) in botGyms_users.values() else False


def no_root(uid):
    """
    Идентификация пользователей

    :param uid:   идентификатор пользователя (chat.id)
    :return:      сообщени еоб отсутсии прав доступа к боту
    """
    bot.send_message(uid, "У Вас нет прав доступа к этому боту")


try:
    bot.infinity_polling(none_stop=True, timeout=180, long_polling_timeout=180)
except Exception as e:
    time.sleep(3)
    print(e)
    pass
