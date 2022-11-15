import tkinter.filedialog as tk
import json
import random

import pandas as pd
import telebot
from telebot import types

config = json.load(open('config.json', encoding="utf-8"))
token, admins, file, secrets_words = config['token'], config['admins'], config['table'], config['secret_words']
map(int, admins)

db = pd.read_excel(file)
bot = telebot.TeleBot(token)

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
            bot.send_message(message.from_user.id, f'Есть активное сектное слово: {list(active_secret_word.keys())[0]}, для {list(active_secret_word.values())[0]} класса', reply_markup=keyboard)
        else:
            keyboard = types.InlineKeyboardMarkup()
            keyboard.add(types.InlineKeyboardButton(text = 'Сгенерировать слово', callback_data = 'admin|gen'))
            bot.send_message(message.from_user.id, f'Активных секретных слов нет', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # print(call)
    # print(call.data)
    call_data = call.data.split('|')
    if call_data[0] == 'admin':
        bot.delete_message(call.from_user.id, call.message.id)
        if call_data[1] == 'gen':
            active_secret_word.clear()
            active_secret_word.update([[]])



bot.infinity_polling()