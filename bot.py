import tkinter.filedialog as tk
import pandas as pd
import telebot
from telebot import types

bot = telebot.TeleBot(open('token.conf').read())
already_get = {}


file = tk.askopenfilename()
clas = input('Класс: ')
subject = input('Предмет: ')

db = pd.read_excel(file)
db.index = db['Класс'].tolist()
db = db.loc[clas]
codes = db[subject].tolist()
print('Осталось кодов:', len(codes))


@bot.message_handler(commands=['start'])
def start (message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Получить код'))
    bot.send_message(message.from_user.id, 'Привет!\nЭто бот для получения кодов для олимпиад', reply_markup=markup)

@bot.message_handler(commands=['get_code'])
def get_code (message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text = 'Получить', callback_data = 'get'))
    keyboard.add(types.InlineKeyboardButton(text = 'Отказаться', callback_data = 'delete'))
    bot.send_message(message.from_user.id, f'Выдача кодов на предмет: {subject} ({clas} класс)', reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Получить код':
        get_code (message)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    bot.delete_message(call.from_user.id, call.message.id)
    if call.data == 'get':
        try:
            bot.send_message(call.from_user.id, already_get[call.from_user.id])
        except KeyError:
            bot.send_message(call.from_user.id, codes[0])
            already_get.update([[call.from_user.id, codes[0]]])
            del codes[0]
            print('Осталось кодов:', len(codes))
            if len(codes) == 0:
                bot.stop_polling()

print('Бот запущен')
# bot.polling(non_stop=True, interval=0)
bot.infinity_polling()
input('Бот отключён')