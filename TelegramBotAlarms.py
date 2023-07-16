import telebot
from tokens import telegramtoken, telegramtoken_venthalls, telegram_users
from telebot import types
from duties import onduties

bot = telebot.TeleBot(telegramtoken)


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

@bot.message_handler(commands=['start']) #создаем команду
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Сайт Хабр", url='https://habr.com/ru/all/')
    markup.add(button1)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "👋 Поздороваться"):
        bot.send_message(message.chat.id, text="Привеет.. Спасибо что читаешь статью!)")
    elif (message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Как меня зовут?")
        btn2 = types.KeyboardButton("Что я могу?")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif (message.text == "Как меня зовут?"):
        bot.send_message(message.chat.id, "У меня нет имени..")

    elif message.text == "Что я могу?":
        bot.send_message(message.chat.id, text="Поздороваться с читателями")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Поздороваться")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")


bot.polling(none_stop=True)



# if __name__ =="__main__":
#     bot = telebot.TeleBot(telegramtoken)
#     msg="Авария на объекте, просьба относиться с пониманием!"
#     for i in telegram_users.values():
#         bot.send_message(i, msg)