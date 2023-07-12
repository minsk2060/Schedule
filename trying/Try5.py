# # Импорт всех необходимых библиотек
# from flask import Flask, request, Response, session
# from viberbot import Api
# from viberbot.api.bot_configuration import BotConfiguration
# from viberbot.api.messages import (TextMessage, KeyboardMessage)
# from viberbot.api.viber_requests import ViberMessageRequest, ViberConversationStartedRequest
# import sched  # планировщик событий
# import threading  # параллельная обработка данных
# import time  # работа с временем
# import mysql.connector
#
# token = 'ВАШ ТОКЕН'
#
#
# class UseDataBase:
#
#
# # создали класс для работы с базой данных
# '''Менеджер контекста для подключения к базе данных'''
#
#
# def __init__(self, config: dict) -> None:
#     self.configuration = config
#     # создали атрибут класса configuration, равный передаваемому аргументу config
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
#     '''Чат-бот'''
#
#
# def __init__(self, token):
#     # Инициализация чат-бота данными, полученными при регистрации на Admin Panel
#     # Атрибуты по умолчанию:
#     self.viber = Api(BotConfiguration(
#         name='TestChatBotByIlya',
#         avatar='http://viber.com/avatar.jpg',
#         auth_token=token))
#     # создали атрибут нашего класса ViberSay, который является экземпляром класса Api, которому
#     # в качестве параметров передается объект класса BotConfiguration с конфигурационными
#     # данными нашего бота
#
#     self.app = Flask(__name__)
#     # создали экземпляра приложения Flask
#
#     self.scheduler = sched.scheduler(time.time, time.sleep)
#     # создали планировщик scheduler - метод библиотеки sched
#     # с параметрами time.time - ?время выполнения, time.sleep - время паузы
#     # ?определили как будут выполняться периодичские действия
#
#     self.scheduler.enter(5, 1, self.set_webhook, ())
#     # определили что будет периодически выполняться
#     # метод enter планирует событие ,
#     # 5 - задержка времени, 1 -приоритет,
#     # set_webhook - само событие?
#
#     self.t = threading.Thread(target=self.scheduler.run)
#     # создали поток (один из одновременных процессов?)
#     # для выполнения функции scheduler
#     # метод run запкускает функцию
#
#     self.t.start()
#     # запустили поток
#
#     self.app.secret_key = 'YouWillNeverGuess'
#     # присвоили переменной secret_key фонкции app библиотеки Flask значение
#
#     # конфигурация базы данных
#     self.app.config['dbconfig'] = {'host': '127.0.0.1',
#                                    'user': 'ilya',
#                                    'password': 'qwerty123',
#                                    'database': 'siemens', }
#     self.index = 0
#     self.app.add_url_rule('/', 'home', self.poll, methods=['POST', 'GET'])
#     self.app.run(host='0.0.0.0', port=8443, debug=True)  # пуск приложения
#
#
# def set_webhook(self):
#     # установка вебхука
#     self.viber.set_webhook('https://06841b02dbf3.ngrok.io')
#
#
# def poll(self):
#     # приём входящих сообщений, обработка и декодирование
#     viber_request = self.viber.parse_request(request.get_data().decode('utf8'))
#     if isinstance(viber_request, ViberConversationStartedRequest):
#         # Определяем начало диалога с ботом
#
#         session['uid'] = viber_request.user.id
#         # получаем id пользователя?
#
#         self.viber.send_messages(session['uid'], [TextMessage(text='Добро пожаловать!')])
#         # отправка сообщения с текстом "Добр пожаловать!"
#
#         self.send_buttons(uid=session['uid'], text=['Получить данные'], btns=1)
#         # отправка кнопки с предложением получить данные
#
#     elif isinstance(viber_request, ViberMessageRequest):
#         # если не начало диалога, то ждём запроса данных
#         session['uid'] = viber_request.sender.id
#
#         if viber_request.message.text == 'Получить данные':
#             with UseDataBase(self.app.config['dbconfig']) as cursor:
#                 # ыполнение запроса к базу данных
#                 _SQL = """select Id, Value from data"""
#                 cursor.execute(_SQL)
#                 contents = cursor.fetchall()
#                 # Выбираем последнее значение из массива чисел и отправляем пользователю
#                 if self.index != contents[-1][0]:
#                     self.index = contents[-1][0]
#                     text_mes = 'Значение = {}'.format(contents[-1][1])
#
#                     self.viber.send_messages(to=session['uid'], messages=[TextMessage(text=text_mes)])
#
#         self.send_buttons(uid=session['uid'], text=['Получить данные'], btns=1)
#         # снова отправляем кнопку с предложением получить данные
#     return Response(status=200)
#
#
# def send_buttons(self, uid, text, btns):
#     # метод формирует кнопку
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