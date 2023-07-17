import telebot
from telebot import types
from tokens import telegramtoken, telegram_users
from duties import onduties

def to_telegram(msg):
    """
    telegram()     - отправка события в мессенджер Telegram
    msg            - текст сообщения
    bot            - объект класса TeleBot для работы с Telegram
    telegramtoken  - токен мессенджера Telegram
    telegramusers  - идентификаторы получателей сообщений в Telegram
    """
    bot = telebot.TeleBot(telegramtoken)
    for i in telegram_users.values():
        bot.send_message(i, msg)

    # получаем ключ (имя получателя) для словаря с именами и id
    # worker = onduties()

    # отправляем сообщение тому, кто сейчас на смене
    # bot.send_message(chat_id_workers[worker], msg)

# Первый шаг к созданию кнопки в боте
# bot = telebot.TeleBot(telegramtoken)
# @bot.message_handler(commands=["start"])
# def start(message):
#     markup = types.InlineKeyboardMarkup()
#     button1 = types.InlineKeyboardButton("Пробная кнопка", url = "www.google.com")
#     markup.add(button1)
#     bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)
# bot.polling(none_stop=True)

# if __name__ =="__main__":
#     bot = telebot.TeleBot(telegramtoken)
#     msg="Авария на объекте, просьба относиться с пониманием!"
#     for i in telegram_users.values():
#         bot.send_message(i, msg)