from viberbot.api.messages.text_message import TextMessage
from tokens import viberwebhook
from tokens import viber_users
from ViberBot import viber

def sethook():
    """
    sethook()     - отправка запроса для установки webhook
    viberwebhook  - адрес приложения в ngr
    """
    viber.set_webhook(viberwebhook)

def to_viber(msg):
    """
    to_viber()    - отправка сообщения об авари в мессенджер Viber
    msg           - текст сообщения
    msgtext       - объект класса TextMessage для корректной передачи параметра в функцию
    в цикле перебор получателей сообщения (сообщения д.быть отправлены только подписчикам)
    try-except    - игнорирование ошибки при отправке тем ,кто отписался
    """
    msgtext = TextMessage(text=msg)
    for i in viber_users.values():
        try:
            viber.send_messages(i, [msgtext])
        except:
            pass


if __name__ == "__main__":
    sethook()