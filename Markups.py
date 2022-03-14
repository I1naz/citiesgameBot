from telebot import types


markup_main = types.InlineKeyboardMarkup(row_width=3)
btn_main = types.InlineKeyboardButton("Играть!", callback_data='play')
markup_main.add(btn_main)

markup_choice_first = types.InlineKeyboardMarkup(row_width=3)
btn_choice_1 = types.InlineKeyboardButton('Я', callback_data='me')
btn_choice_2 = types.InlineKeyboardButton('Ты', callback_data='you')
markup_choice_first.add(btn_choice_1, btn_choice_2)

markup_helpers = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn_help = types.KeyboardButton('/help')
btn_surrender = types.KeyboardButton('Сдаться')
markup_helpers.add(btn_help, btn_surrender)

markup_again = types.InlineKeyboardMarkup(row_width=3)
btn_again = types.InlineKeyboardButton('Да', callback_data='play_again')
btn_not_again = types.InlineKeyboardButton('Нет', callback_data='not_play_again')
markup_choice_first.add(btn_again, btn_not_again)

