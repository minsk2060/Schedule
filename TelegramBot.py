import telebot
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

if __name__ =="__main__":
    bot = telebot.TeleBot(telegramtoken)
    msg="Авария класса А - вызывает останов установки"
    bot.send_message(telegram_users["Euheny"], msg)