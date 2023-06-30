from viberbot.api.messages.text_message import TextMessage
from tokens import viberwebhook
from tokens import viber_users
from ViberBot import viber

def sethook():
    viber.set_webhook(viberwebhook)

def toviber(msg):
    msgtext = TextMessage(text=msg)
    for i in viber_users.values():
        try:
            viber.send_messages(i, [msgtext])
        except:
            pass


if __name__ == "__main__":
    sethook()