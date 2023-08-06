import telebot
from telegramtokens import telegramtoken_ventgyms, botGyms_users
from telebot import types
import requests
import time
from headers import header, header_alarm_A, sauter_cookie
from plants import alarms_A, alarms_BC
from helpmsg import helpmsg_gyms

# Инициализация бота
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

# Коды состояний работы
states = {"2": "работает на высокой скорости",
          "1": "работает на низкой скорости",
          "0": "остановлена",
          "3": "работает на низкой скорости", }

# Тексты команд на кнопках
starts = ["Запуск  " + x for x in places.values()]
stops = ["Останов  " + x for x in places.values()]
curstates = ["Состояние  " + x for x in places.values()]
scheds = ["Расписание  " + x for x in places.values()]


def if_root(permit):
    """
    Ограничение доступа к боту

    :param permit: функция, для которой будет применяться ограничение прав доступа
    :return: функция для сравнения входящего id со списком пользователей
    """
    def check_root(message):
        """
        Ограничение прав доступа

        :param message: входной параметр для определения id пользователя
        """
        uid = str(message.chat.id)
        if uid in botGyms_users.values():
            permit(message)
        else:
            sms(uid, "У Вас НЕТ прав доступа к этому боту")
        return check_root


def alrm_params(alrm_dict):
    """ Преобразование с целью получения параметров для запроса

    :param alrm_dict: словарь с параметрами (...'12583575&did=33559432':  'ПВ-2.9 ',)
    :return:          словарь с корректными параметрами (...'ПВ-2.9': '12583575&did=33559432')
    """
    return {v.replace(" ", ""): k for k, v in alrm_dict.items()
            if v.replace(" ", "") in all_plants.keys()}


@bot.message_handler(commands=['help'])
# @if_root
def hepl(message):
    """
    Обработчик сообщения "help"

    :param message: объект "сообщение" (содержит в т.ч. текст сообщения)
    """
    uid = message.chat.id
    sms(uid, helpmsg_gyms)


@bot.message_handler(commands=['start'])
# @if_root
def start(message):
    """
    Обработчик сообщений, поступающих после команды "start"

    :param message: объект "сообщение" (содержит в т.ч. текст сообщения)
    """
    uid = message.chat.id
    # if root(uid):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Игровая комната")
    btn2 = types.KeyboardButton("Раздевалки залов")
    btn3 = types.KeyboardButton("Тренажерный зал")
    btn4 = types.KeyboardButton("Зал Ёги")
    markup.add(btn3, btn4)
    markup.add(btn2)
    markup.add(btn1)
    bot.send_message(uid, "Выберите помещение", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data in ['1', '2'])
def check_speed(callback):
    """
    Обработчик сообщения с инлайн кнопками

    :param callback: объект, содержащий в т.ч. инфо о нажатой кнопке
    """
    uid = callback.message.chat.id
    tex = callback.message.text.replace("Выберите скорость работы", "Запуск ")
    sms(uid,  "Стартуем.... ", 4)
    switch_plant(callback.message, tex, callback.data, "Запуск")


@bot.message_handler(content_types=['text'])
# @if_root
def func(message):
    """
    Обработчик текстовых сообщений (основная логика)

    :param message: объект "сообщение"
    """
    uid = message.chat.id
    msg = message.text
    pv = msg.index("ПВ") if "ПВ" in msg else 0
    print(message.chat.id, message.from_user.first_name, message.from_user.last_name)
    #(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)kup)

    # Главное меню
    if msg == "Главное меню":
        start(message)
    # Информация
    elif msg in places.keys():
        sms(uid, f"{msg}\nобслуживается вентустановкой  {places[msg]}", 1)
        reply(message, msg)
    # Расписание
    elif msg in scheds:
        sms(uid, f"Ждите, сейчас узнаем ...", 4)
        fil = open("../logging/readlogs.txt", "r")
        sts = []
        for i in fil.read().split("\n"):
            if msg[pv:] in i:
                sts.append(i.replace(f"{msg[pv:]}    ", ""))
        prn = "\n".join(sts).replace("\n", "\n\n").replace("0   ", "0\n")
        if prn == "":
            prn = "не задано"
        sms(uid, f'{msg}\nна эти дни:\n\n{prn}', 1)
        sms(uid)
    # Состояние
    elif msg in curstates:
        sms(uid, f"Ждите, идет опрос ...", 2)
        sms(uid, f"В текущий момент установка "
                 f"{msg[pv:]}  {get_state(msg[pv:])}.\n"
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
        r = requests.get(url, headers=header, cookies=sauter_cookie)
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
    resp = requests.get(url, headers=header, cookies=sauter_cookie)
    time.sleep(3)
    rsp = resp.text
    num = rsp[rsp.index('<tr data-pid="85">')+18:]
    end = num[:num.index('</tr>')]
    stt = end[end.index("property-value")+16]
    return states[stt]

class Alarms:
    pass

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
    prs = alrm_params(alarms_A)
    alm = 'Авария класса А'
    return True if get_alarm(plt, prs, alm) == alm else False


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


try:
    bot.infinity_polling(none_stop=True, timeout=180, long_polling_timeout=180)
except Exception as err:
    time.sleep(3)
    print(err)
    pass
