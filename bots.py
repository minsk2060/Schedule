import telebot
from tokens import telegramtoken, chat_id

# chat_id = {"Mikhail" : "1140621075",
#            "Michael" : "5740110040",
#            "Roman"   : "1565146153",
#            }

def telegram(msg):
    """
    telegram()     - отправка события в мессенджер Telegram
    msg            - текст сообщения
    bot            - объект класса TeleBot для работы с Telegram
    telegramtoken  - токен мессенджера Telegram
    chat_id        - идентификаторы получателей сообщений в Telegram
    """
    bot = telebot.TeleBot(telegramtoken)
    for i in chat_id.values():
        bot.send_message(i, msg)



if __name__ =="__main__":
    bot = telebot.TeleBot(telegramtoken)
    msg="Авария класса А - вызывает останов установки. Авария класса B,C - в основном не останавливает оборудование."

    bot.send_message(chat_id["Alexandr"], msg)