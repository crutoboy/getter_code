import tkinter.filedialog as tk
import json
from random import choice

import pandas as pd
import telebot
from telebot import types

config = json.load(open('config.json', encoding="utf-8"))
token, admins, file, secrets_words = config['token'], config['admins'], config['table'], config['secret_words']
map(int, admins)

db = pd.read_excel(file)
bot = telebot.TeleBot(token, 'MARKDOWN')

registered_users = set(db['ФИО'].to_list())
active_secret_word = {}

# file = tk.askopenfilename()
# clas = input('Класс: ')
# subject = input('Предмет: ')


# db.index = db['Класс'].tolist()
# db = db.loc[clas]
# codes = db[subject].tolist()
# print('Осталось кодов:', len(codes))


@bot.message_handler(commands=['admin'])
def admin (message):
    if message.from_user.id in admins:
        if len(active_secret_word) > 0:
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text = 'Сгенерировать новое', callback_data = 'admin|gen'))
            keyboard.add(types.InlineKeyboardButton(text = 'Деактивировать слово', callback_data = 'admin|delete'))
            bot.send_message(message.from_user.id, f'Есть активное сектное слово: *{list(active_secret_word.keys())[0]}*, для *{list(active_secret_word.values())[0]}* класса', reply_markup=keyboard)
        else:
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text = 'Сгенерировать слово', callback_data = 'admin|gen'))
            bot.send_message(message.from_user.id, f'Активных секретных слов нет', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == list(active_secret_word.keys())[0] and str(message.from_user.id) not in registered_users:
        if message.from_user.id in admins:
            bot.send_message(message.from_user.id, f'Это слово используется для регистрации в {list(active_secret_word.values())[0]} класс')
        else:
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text = 'Да', callback_data = 'reg|ask_class|y')
            btn2 = types.InlineKeyboardButton(text = 'Нет', callback_data = 'reg|ask_class|n')
            keyboard.add(btn1, btn2)
            bot.send_message(message.from_user.id, f'Ты учиишься в {list(active_secret_word.values())[0]} классе?')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # print(call)
    # print(call.data)
    call_data = call.data.split('|')
    if call_data[0] == 'admin' and call.from_user.id in admins:
        bot.delete_message(call.from_user.id, call.message.id)
        if call_data[1] == 'gen':
            keyboard = types.InlineKeyboardMarkup()
            tmp = list(set(db['Класс'].to_list()))
            # tmp.sort()
            for i in tmp:
                keyboard.add(types.InlineKeyboardButton(text = i, callback_data = f'admin|create|{i}'))
            bot.send_message(call.from_user.id, f'Выберите класс для которого сгенерируется слово', reply_markup=keyboard)
        elif call_data[1] == 'create':
            active_secret_word.clear()
            active_secret_word.update([[choice(secrets_words), call_data[2]]])
            admin (call)
        elif call_data[1] == 'delete':
            active_secret_word.clear()
            admin (call)
    if call_data[0] == 'reg':
        if call_data[1] == 'ask_class':
            if call_data[2] == 'y':
                registered_users.add(str(call.from_user.id))
            if call_data[2] == 'n':
                bot.delete_message(call.from_user.id, call.message.id)




bot.infinity_polling()

bot.edit_message_reply_markup()
bot.edit_message_text()