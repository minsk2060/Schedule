# #
# #
# # # ˜˜˜˜˜˜ ˜˜˜˜˜˜ ˜ ˜˜˜˜˜˜
# @bot.message_handler(commands=['start']) #˜˜˜˜˜˜˜ ˜˜˜˜˜˜˜
# def start(message):
#     markup = types.InlineKeyboardMarkup()
#     button1 = types.InlineKeyboardButton("˜˜˜˜ ˜˜˜˜", url='https://habr.com/ru/all/')
#     markup.add(button1)
#     bot.send_message(message.chat.id, "˜˜˜˜˜˜, {0.first_name}! ˜˜˜˜˜ ˜˜ ˜˜˜˜˜˜ ˜ ˜˜˜˜˜˜˜ ˜˜ ˜˜˜˜)".format(message.from_user), reply_markup=markup)kup)
# bot.polling(none_stop=True)
#
#
# # ˜˜˜˜˜˜ ˜˜˜˜˜˜˜˜ ˜˜˜˜ ˜ ˜˜˜˜˜˜˜˜
# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("˜˜˜˜˜˜˜˜˜˜˜˜˜")
#     btn2 = types.KeyboardButton("˜˜˜˜˜˜ ˜˜˜˜˜˜")
#     markup.add(btn1, btn2)
#     bot.send_message(message.chat.id,
#                      text="˜˜˜˜˜˜, {0.first_name}! ˜ ˜˜˜˜˜˜˜˜ ˜˜˜ ˜˜˜ ˜˜˜˜˜ ˜˜˜˜˜˜ ˜˜˜ habr.com".format(
#                          message.from_user), reply_markup=markup)
#
#
# @bot.message_handler(content_types=['text'])
# def func(message):
#     if (message.text == "˜˜˜˜˜˜˜˜˜˜˜˜˜"):
#         bot.send_message(message.chat.id, text="˜˜˜˜˜˜˜.. ˜˜˜˜˜˜˜ ˜˜˜ ˜˜˜˜˜˜˜ ˜˜˜˜˜˜!)")
#     elif (message.text == "˜˜˜˜˜˜ ˜˜˜˜˜˜"):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         btn1 = types.KeyboardButton("˜˜˜ ˜˜˜˜ ˜˜˜˜˜?")
#         btn2 = types.KeyboardButton("˜˜˜ ˜ ˜˜˜˜?")
#         back = types.KeyboardButton("˜˜˜˜˜˜˜˜˜ ˜ ˜˜˜˜˜˜˜ ˜˜˜˜")
#         markup.add(btn1, btn2, back)
#         bot.send_message(message.chat.id, text="˜˜˜˜˜ ˜˜˜ ˜˜˜˜˜˜", reply_markup=markup)
#
#     elif (message.text == "˜˜˜ ˜˜˜˜ ˜˜˜˜˜?"):
#         bot.send_message(message.chat.id, "˜ ˜˜˜˜ ˜˜˜ ˜˜˜˜˜..")
#
#     elif message.text == "˜˜˜ ˜ ˜˜˜˜?":
#         bot.send_message(message.chat.id, text="˜˜˜˜˜˜˜˜˜˜˜˜˜ ˜ ˜˜˜˜˜˜˜˜˜˜")
#
#     elif (message.text == "˜˜˜˜˜˜˜˜˜ ˜ ˜˜˜˜˜˜˜ ˜˜˜˜"):
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#         button1 = types.KeyboardButton("˜˜˜˜˜˜˜˜˜˜˜˜˜")
#         button2 = types.KeyboardButton("˜˜˜˜˜˜ ˜˜˜˜˜˜")
#         markup.add(button1, button2)
#         bot.send_message(message.chat.id, text="˜˜ ˜˜˜˜˜˜˜˜˜ ˜ ˜˜˜˜˜˜˜ ˜˜˜˜", reply_markup=markup)
#     else:
#         bot.send_message(message.chat.id, text="˜˜ ˜˜˜˜˜ ˜˜˜˜˜˜˜˜ ˜ ˜˜ ˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜..")
#
#
# bot.polling(none_stop=True)
