import telebot
from telebot import types

bot = telebot.TeleBot('5541635960:AAFMRc_9kqBHla4yHMs3bL5M1KGfcgEFo7s')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет', {message.from_user.first_name}, {message.from_user.last_name}
    bot.send_message(message.chat.id, mess, parse_mode='html')