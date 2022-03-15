import telebot
from Config import *
from Markups import *
from Cities import *
from flask import Flask, request
import os
from random import choice


bot = telebot.TeleBot(Token)
server = Flask(__name__)


class Game:
    def __init__(self):
        self.count = 0
        self.current_city = ''
        self.all_cities = ''
        self.max_first_letters = ('', 0)
        self.is_started = False
        self.is_me_first = False
        self.first_city = False
        self.is_he_first = False
        self.is_finished = False
        self.first_letters = {'а': 0, 'б': 0, 'в': 0, 'г': 0, 'д': 0, 'е': 0, 'ё': 0, 'ж': 0, 'з': 0, 'и': 0, 'й': 0,
                              'к': 0, 'л': 0, 'м': 0, 'н': 0, 'о': 0, 'п': 0, 'р': 0, 'с': 0, 'т': 0, 'у': 0, 'ф': 0,
                              'х': 0, 'ц': 0, 'ч': 0, 'ш': 0, 'щ': 0, 'ю': 0, 'я': 0}

    def more_first_letters(self):
        for i, j in self.first_letters.items():
            if j > self.max_first_letters[-1]:
                self.max_first_letters = (i, j)

    def finish(self):
        self.count = 0
        self.current_city = ''
        self.all_cities = ''
        self.max_first_letters = ('', 0)
        self.is_started = False
        self.is_me_first = False
        self.first_city = False
        self.is_he_first = False
        self.is_finished = False
        self.first_letters = {'а': 0, 'б': 0, 'в': 0, 'г': 0, 'д': 0, 'е': 0, 'ё': 0, 'ж': 0, 'з': 0, 'и': 0, 'й': 0,
                              'к': 0, 'л': 0, 'м': 0, 'н': 0, 'о': 0, 'п': 0, 'р': 0, 'с': 0, 'т': 0, 'у': 0, 'ф': 0,
                              'х': 0, 'ц': 0, 'ч': 0, 'ш': 0, 'щ': 0, 'ю': 0, 'я': 0}


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, '✋', parse_mode='html',
                     reply_markup=markup_helpers)
    bot.send_message(message.chat.id, f'{start_mess1}{message.from_user.first_name}! {start_mess2}', parse_mode='html',
                     reply_markup=markup_main)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, help_mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def play(message):
    if message.chat.type == 'private':
        if message.text == 'Сдаться':
            game.more_first_letters()
            bot.send_message(message.chat.id, f'Всего названо городов: {game.count}. '
                                              f'Большинство городов начинались на {game.max_first_letters[0]}, их было {game.max_first_letters[-1]}',
                             parse_mode='html')
            game.finish()
            bot.send_message(message.chat.id, f'{choice(replay_mess)}',
                             parse_mode='html', reply_markup=markup_again)
        if not (game.first_city and game.is_he_first):
            if (message.text.capitalize().startswith(game.current_city[-1].upper())
                or message.text.capitalize().startswith(game.current_city[-2].upper())) and message.text.capitalize() in cities_only:
                game.all_cities += message.text
                game.first_letters[message.text[0].lower()] += 1
                cities_only.remove(message.text.strip().capitalize())
                game.count += 1
                if message.text[-1].upper() in cities_by_first_letter.keys():
                    game.current_city = choice(cities_by_first_letter[message.text[-1].upper()])
                    mess = f'{game.current_city}, {country[city[game.current_city]]}'
                    bot.send_message(message.chat.id, f'{mess}. Тебе на {game.current_city[-1].upper()}',
                                     parse_mode='html')
                    cities_only.remove(game.current_city)
                    game.count += 1
                elif message.text[-2].upper() in cities_by_first_letter.keys():
                    game.current_city = choice(cities_by_first_letter[message.text[-2].upper()])
                    mess = f'{game.current_city}, {country[city[game.current_city]]}'
                    bot.send_message(message.chat.id, f'{mess}. Тебе на {game.current_city[-1].upper()}',
                                     parse_mode='html')
                    cities_only.remove(game.current_city)
                    game.count += 1
                else:
                    game.more_first_letters()
                    bot.send_message(message.chat.id, f'В итоге получилось слово: {game.all_cities}',
                                     parse_mode='html')
                    bot.send_message(message.chat.id, f'Всего названо городов: {game.count}. '
                                                      f'Большинство городов начинались на {game.max_first_letters[0]}, их было {game.max_first_letters[-1]}',
                                     parse_mode='html')
                    game.finish()
                    bot.send_message(message.chat.id, f'{choice(replay_mess)}',
                                     parse_mode='html', reply_markup=markup_again)
            elif message.text.capitalize().startswith(game.current_city[-1].upper()) and message.text.capitalize() not in cities_only:
                bot.send_message(message.chat.id, f'{some_phrases[-1]}, говори заново. Тебе на {game.current_city[-1].upper()}', parse_mode='html')
            else:
                bot.send_message(message.chat.id, f'{choice(some_phrases[:-1])} говори заново. Тебе на {game.current_city[-1].upper()}', parse_mode='html')
            game.first_city = False
        else:
            get_city()
            get_country()
            if message.text.capitalize() in cities_only:
                game.all_cities += message.text
                game.first_letters[message.text[0].lower()] += 1
                cities_only.remove(message.text.strip().capitalize())
                if message.text[-1].upper() in cities_by_first_letter.keys():
                    game.current_city = choice(cities_by_first_letter[message.text[-1].upper()])
                elif message.text[-2].upper() in cities_by_first_letter.keys():
                    game.current_city = choice(cities_by_first_letter[message.text[-2].upper()])
                mess = f'{game.current_city}, {country[city[game.current_city]]}'
                bot.send_message(message.chat.id, f'{mess}. Тебе на {game.current_city[-1].upper()}',
                                 parse_mode='html')
                cities_only.remove(game.current_city)
                game.count += 2
            else:
                bot.send_message(message.chat.id,
                                 f'{choice(some_phrases[:-1])} говори заново',
                                 parse_mode='html')
            game.first_city = False


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'you':
                game.is_started = True
                game.is_me_first = True
                game.is_he_first = False
                get_city()
                get_country()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Начинаю!',
                                      reply_markup=None)
                game.current_city = choice(cities_only)
                game.all_cities += game.current_city
                game.first_letters[game.current_city[0].lower()] += 1
                game.count += 1
                mess = f'{game.current_city}, {country[city[game.current_city]]}'
                bot.send_message(call.message.chat.id, f'{mess}. Тебе на {game.current_city[-1].upper()}', parse_mode='html')
                cities_only.remove(game.current_city)

            elif call.data == 'me':
                game.is_me_first = False
                game.is_he_first = True
                game.first_city = True
                game.is_started = True
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Начинай!', reply_markup=None)
            elif call.data == 'play' or call.data == 'play_again':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Кто начинает?',
                                 reply_markup=markup_choice_first)
            elif call.data == 'not_play_again':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='👋',
                                      reply_markup=None)
                bot.send_message(call.message.chat.id, 'Захочется поиграть, приходи!',
                                 parse_mode='html', reply_markup=markup_main)
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
    bot.process_new_updates([update])
    return '!', 200


if __name__ == '__main__':
    game = Game()
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
