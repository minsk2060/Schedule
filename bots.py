import telebot
from tokens import telegramtoken, chat_id

chat_id = {"Mikhail" : "1140621075",
           "Michael" : "5740110040",
           "Roman"   : "1565146153",
           }

def telegram(msg):
    bot = telebot.TeleBot(telegramtoken)
    for i in chat_id.values():
        bot.send_message(i, msg)



if __name__ =="__main__":
    telegram("FooBarBaz")