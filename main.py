import telebot
from Config import *
from Markups import *
from Cities import *
from flask import Flask, request
import os
import random


bot = telebot.TeleBot(Token)
server = Flask(__name__)


class Game:
    def __init__(self):
        self.count = 0
        self.current_city = None
        self.all_cities = None
        self.first_letters = {'а': 0, 'б': 0, 'в': 0, 'г': 0, 'д': 0, 'е': 0, 'ё': 0, 'ж': 0, 'з': 0, 'и': 0, 'й': 0,
                              'к': 0, 'л': 0, 'м': 0, 'н': 0, 'о': 0, 'п': 0, 'р': 0, 'с': 0, 'т': 0, 'у': 0, 'ф': 0,
                              'х': 0, 'ц': 0, 'ч': 0, 'ш': 0, 'щ': 0, 'ю': 0, 'я': 0}


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, f'{start_mess1}{message.from_user.first_name}! {start_mess2}', parse_mode='html',
                     reply_markup=markup_main)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, help_mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def play(message):
    if message.chat.type == 'private':
        # else:
        #     bot.send_message(message.chat.id, ' А я чибурик!')
        pass


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'you':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Начинаю!',
                                      reply_markup=None)
            elif call.data == 'me':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Начинай!', reply_markup=None)
            elif call.data == 'play':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Кто начинает?',
                                 reply_markup=markup_choice_first)
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text='')
    except Exception as e:
        print(repr(e))


@server.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=APP_Url)
    return '!', 200


@server.route(f'/{Token}', methods=['POST'])
def get_message():
    json_str = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    return '!', 200


if __name__ == '__main__':
    game = Game()
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
