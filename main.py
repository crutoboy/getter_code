import tkinter.filedialog as tk

import pandas as pd
import telebot
from telebot import types

bot = telebot.TeleBot(open('token.conf').read())