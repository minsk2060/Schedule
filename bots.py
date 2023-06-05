import telebot
from tokens import telegramtoken, chat_id

def telegram(msg):
    bot = telebot.TeleBot(telegramtoken)
    bot.send_message(chat_id, msg)




if __name__ =="__main__":
    telegram("FooBarBaz")