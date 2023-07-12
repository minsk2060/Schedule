# # ������ ���� ����������� ���������
# from flask import Flask, request, Response, session
# from viberbot import Api
# from viberbot.api.bot_configuration import BotConfiguration
# from viberbot.api.messages import (TextMessage, KeyboardMessage)
# from viberbot.api.viber_requests import ViberMessageRequest, ViberConversationStartedRequest
# import sched  # ����������� �������
# import threading  # ������������ ��������� ������
# import time  # ������ � ��������
# import mysql.connector
#
# token = '��� �����'
#
#
# class UseDataBase:
#
#
# # ������� ����� ��� ������ � ����� ������
# '''�������� ��������� ��� ����������� � ���� ������'''
#
#
# def __init__(self, config: dict) -> None:
#     self.configuration = config
#     # ������� ������� ������ configuration, ������ ������������� ��������� config
#
#
# def __enter__(self):
#     self.conn = mysql.connector.connect(**self.configuration)
#     self.cursor = self.conn.cursor()
#     return self.cursor
#
#
# def __exit__(self, exc_type, exc_val, exc_tb):
#     self.conn.commit()
#     self.cursor.close()
#     self.conn.close()
#
#
# class ViberSay():
#     '''���-���'''
#
#
# def __init__(self, token):
#     # ������������� ���-���� �������, ����������� ��� ����������� �� Admin Panel
#     # �������� �� ���������:
#     self.viber = Api(BotConfiguration(
#         name='TestChatBotByIlya',
#         avatar='http://viber.com/avatar.jpg',
#         auth_token=token))
#     # ������� ������� ������ ������ ViberSay, ������� �������� ����������� ������ Api, ��������
#     # � �������� ���������� ���������� ������ ������ BotConfiguration � �����������������
#     # ������� ������ ����
#
#     self.app = Flask(__name__)
#     # ������� ���������� ���������� Flask
#
#     self.scheduler = sched.scheduler(time.time, time.sleep)
#     # ������� ����������� scheduler - ����� ���������� sched
#     # � ����������� time.time - ?����� ����������, time.sleep - ����� �����
#     # ?���������� ��� ����� ����������� ������������ ��������
#
#     self.scheduler.enter(5, 1, self.set_webhook, ())
#     # ���������� ��� ����� ������������ �����������
#     # ����� enter ��������� ������� ,
#     # 5 - �������� �������, 1 -���������,
#     # set_webhook - ���� �������?
#
#     self.t = threading.Thread(target=self.scheduler.run)
#     # ������� ����� (���� �� ������������� ���������?)
#     # ��� ���������� ������� scheduler
#     # ����� run ���������� �������
#
#     self.t.start()
#     # ��������� �����
#
#     self.app.secret_key = 'YouWillNeverGuess'
#     # ��������� ���������� secret_key ������� app ���������� Flask ��������
#
#     # ������������ ���� ������
#     self.app.config['dbconfig'] = {'host': '127.0.0.1',
#                                    'user': 'ilya',
#                                    'password': 'qwerty123',
#                                    'database': 'siemens', }
#     self.index = 0
#     self.app.add_url_rule('/', 'home', self.poll, methods=['POST', 'GET'])
#     self.app.run(host='0.0.0.0', port=8443, debug=True)  # ���� ����������
#
#
# def set_webhook(self):
#     # ��������� �������
#     self.viber.set_webhook('https://06841b02dbf3.ngrok.io')
#
#
# def poll(self):
#     # ���� �������� ���������, ��������� � �������������
#     viber_request = self.viber.parse_request(request.get_data().decode('utf8'))
#     if isinstance(viber_request, ViberConversationStartedRequest):
#         # ���������� ������ ������� � �����
#
#         session['uid'] = viber_request.user.id
#         # �������� id ������������?
#
#         self.viber.send_messages(session['uid'], [TextMessage(text='����� ����������!')])
#         # �������� ��������� � ������� "���� ����������!"
#
#         self.send_buttons(uid=session['uid'], text=['�������� ������'], btns=1)
#         # �������� ������ � ������������ �������� ������
#
#     elif isinstance(viber_request, ViberMessageRequest):
#         # ���� �� ������ �������, �� ��� ������� ������
#         session['uid'] = viber_request.sender.id
#
#         if viber_request.message.text == '�������� ������':
#             with UseDataBase(self.app.config['dbconfig']) as cursor:
#                 # ��������� ������� � ���� ������
#                 _SQL = """select Id, Value from data"""
#                 cursor.execute(_SQL)
#                 contents = cursor.fetchall()
#                 # �������� ��������� �������� �� ������� ����� � ���������� ������������
#                 if self.index != contents[-1][0]:
#                     self.index = contents[-1][0]
#                     text_mes = '�������� = {}'.format(contents[-1][1])
#
#                     self.viber.send_messages(to=session['uid'], messages=[TextMessage(text=text_mes)])
#
#         self.send_buttons(uid=session['uid'], text=['�������� ������'], btns=1)
#         # ����� ���������� ������ � ������������ �������� ������
#     return Response(status=200)
#
#
# def send_buttons(self, uid, text, btns):
#     # ����� ��������� ������
#     KEYBOARD = {"Type": "keyboard", "Buttons": []}
#
#     for i in range(btns):
#         KEYBOARD["Buttons"].append(
#             {
#                 "Columns": 6,
#                 "Rows": 1,
#                 "BgColor": '#4169E1',
#                 "BgMedia": None,
#                 "BgMediaType": None,
#                 "BgLoop": True,
#                 "ActionType": "reply",
#                 "ActionBody": text[i],
#                 "ReplyType": "message",
#                 "Text": text[i]
#             }
#         )
#
#     message = KeyboardMessage(tracking_data='tracking_data', keyboard=KEYBOARD)
#     self.viber.send_messages(session['uid'], [message])
#
#
# if __name__ == "__main__":
#     ViberSay(token)