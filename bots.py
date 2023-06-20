import telebot
from tokens import telegramtoken, chat_id_bosses, chat_id_workers
import datetime


def telegram(msg):
    """
    telegram()     - отправка события в мессенджер Telegram
    msg            - текст сообщения
    bot            - объект класса TeleBot для работы с Telegram
    telegramtoken  - токен мессенджера Telegram
    chat_id        - идентификаторы получателей сообщений в Telegram
    """
    bot = telebot.TeleBot(telegramtoken)
    for i in chat_id_bosses.values():
        bot.send_message(i, msg)
    # worker = onduties()  # выполняя функцию, получаем ключ (имя получателя) для словаря с именами и id
    # bot.send_message(chat_id_workers[worker], msg)  # отправляем сообщение тому, кто сейчас на смене

def onduties():
    """Функция предусматривает определение кто сегодня на смене в хладоцентре.
    Восстановить эту функцию когда окончится сезон отпусков и график восстановится"""
    dat = datetime.datetime().now() # определить сегодняшнюю дату
    d = dat.toordinal() % 4         # найти порядковый номер даты и найти остаток от деления на 4
    if datetime.time(8, 00) < dat.time() < datetime.time(23, 59): # определить период первой части смены (8:00...0:00)
        # Фамилия, результат деления для первой части смены и второй
        # Вульфов  1, 2
        # Клышко   2, 3
        # Басыров  3, 0
        # Федорчук 0, 1
        if d == 1:
            onduty = "Alexandr"
        elif d == 2:
            onduty = "Nikita"
        elif d == 3:
            onduty = "Yura"
        elif d == 0:
            onduty = "Zhenia"
    elif datetime.time(0, 00) < dat.time() < datetime.time(8, 00): # определить период второй части смены 0:00...8:00
        if d == 2:
            onduty = "Alexandr"
        elif d == 3:
            onduty = "Nikita"
        elif d == 0:
            onduty = "Yura"
        elif d == 1:
            onduty = "Zhenia"
    return onduty



if __name__ =="__main__":
    bot = telebot.TeleBot(telegramtoken)
    msg="Авария класса А - вызывает останов установки. Авария класса B,C - в основном не останавливает оборудование."

    bot.send_message(chat_id_bosses["Yury"], msg)