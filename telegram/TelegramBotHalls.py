import telebot
from telegramtokens import telegramtoken_venthalls
from telebot import types
import requests
import time


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
              "Запуск  ПВ-2.4": "",
              "Запуск  ПВ-2.5": "",
              "Запуск  ПВ-2.6": "",}

stopplant = {"Останов  ПВ-2.7, ПВ-2.8": "",
             "Останов  ПВ-2.4": "",
             "Останов  ПВ-2.5": "",
             "Останов  ПВ-2.6": "",}

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
    bot.send_message(message.chat.id,
                     text="Выберите помещение".format(
                         message.from_user), reply_markup=markup)

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


@bot.message_handler(content_types=['text'])
def func(message):
    msg = message.text
    if msg == "Главное меню":
        start(message)

    elif msg in places.keys():
        bot.send_message(message.chat.id, text=f"{msg}\nобслуживает вентустановка  {places[msg]}")
        reply(message, msg)

    elif msg in schedules.keys():
        bot.send_message(message.chat.id, text=f"Ждите, идет опрос {msg}...")
        time.sleep(5)
        #Здесь необходимо вставить код для опроса расписания работы
        bot.send_message(message.chat.id, text=f"{msg} на ближайшие пару дней:\n...\n...\n...")
        bot.send_message(message.chat.id, "Выберите действие")

    elif msg in curstates.keys():
        bot.send_message(message.chat.id, text=f"Ждите, идет опрос {msg}...")
        time.sleep(5)
        #Здесь необходимо вставить код для опроса расписания работы
        bot.send_message(message.chat.id, text=f"Текущее {msg} :\n...\n...\n...")
        bot.send_message(message.chat.id, "Выберите действие")

    elif msg in startplant.keys():
        # Здесь код для запуска уствновки
        bot.send_message(message.chat.id, "Стартуем....")
        time.sleep(5)
        bot.send_message(message.chat.id, f"{msg} выполнен успешно")

    elif msg in stopplant.keys():
        # Здесь код для останова уствновки
        bot.send_message(message.chat.id, "Останавливаемся....")
        time.sleep(5)
        bot.send_message(message.chat.id, f"{msg} выполнен успешно")

    else:
        bot.send_message(message.chat.id, text="Нет такой команды, Идем на главную.")
        start(message)


bot.polling(none_stop=True)
#
#
# # Пример кнопки в ответе
# # @bot.message_handler(commands=['start']) #создаем команду
# # def start(message):
# #     markup = types.InlineKeyboardMarkup()
# #     button1 = types.InlineKeyboardButton("Сайт Хабр", url='https://habr.com/ru/all/')
# #     markup.add(button1)
# #     bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)kup)
# # bot.polling(none_stop=True)
#
#
# # Пример рабочего бота с кнопками
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("Поздороваться")
#     btn2 = types.KeyboardButton("Задать вопрос")
#     markup.add(btn1, btn2)
#     bot.send_message(message.chat.id,
#                      text="Привет, {0.first_name}! Я тестовый бот для твоей статьи для habr.com".format(
#                          message.from_user), reply_markup=markup)
#
#
# @bot.message_handler(content_types=['text'])
# def func(message):
#     if (message.text == "Поздороваться"):
#         bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
#     elif (message.text == "Задать вопрос"):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton("Как меня зовут?")
#         btn2 = types.KeyboardButton("Что я могу?")
#         back = types.KeyboardButton("Вернуться в главное меню")
#         markup.add(btn1, btn2, back)
#         bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)
#
#     elif (message.text == "Как меня зовут?"):
#         bot.send_message(message.chat.id, "У меня нет имени..")
#
#     elif message.text == "Что я могу?":
#         bot.send_message(message.chat.id, text="Поздороваться с читателями")
#
#     elif (message.text == "Вернуться в главное меню"):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         button1 = types.KeyboardButton("Поздороваться")
#         button2 = types.KeyboardButton("Задать вопрос")
#         markup.add(button1, button2)
#         bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")
#
#
# bot.polling(none_stop=True)
