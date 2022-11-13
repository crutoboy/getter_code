import tkinter.filedialog as tk
import json

import pandas as pd
import telebot
from telebot import types

config = json.load(open('config.json'))
token, admins, file = config['token'], map(int, config['admins']), config['table']

db = pd.read_excel(file)
bot = telebot.TeleBot(token)

registered_users = set(db['ФИО'].to_list())

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
        print(1)
    # keyboard = types.InlineKeyboardMarkup()
    # keyboard.add(types.InlineKeyboardButton(text = 'Получить', callback_data = 'get'))
    # keyboard.add(types.InlineKeyboardButton(text = 'Отказаться', callback_data = 'delete'))
    # bot.send_message(message.from_user.id, f'Выдача кодов на предмет: {subject} ({clas} класс)', reply_markup=keyboard)


bot.infinity_polling()