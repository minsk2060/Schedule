from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration
from viberbot.api.messages.text_message import TextMessage


from tokens import viber_users, vibertoken
from ViberBot import viber

# bot_config = BotConfiguration(name="Вентиляция ФСК", avatar="C:/Users/BMS/projects/schedules/logo.jpg", auth_token=vibertoken)
# viber = Api(bot_config)

# webhook = "https://d60d-37-45-171-18.ngrok-free.app"
# viber.set_webhook(webhook)
# viber.unset_webhook()
# print(viber.get_account_info())

# msg = TextMessage(text="Пробный текст")
# viber.send_messages(viber_users["Mikhail"], [msg])

def toviber(msg):
    msgtext = TextMessage(text=msg)
    for i in viber_users.values():
        try:
            viber.send_messages(i, [msgtext])
        except:
            pass