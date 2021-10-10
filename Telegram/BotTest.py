import telebot
import ConfigBotTest

from telebot import types

bot = telebot.TeleBot(ConfigBotTest.TOKEN)


def keyboard(where_call):
    if where_call == 'H':
        markup = types.InlineKeyboardMarkup(row_width=2)
        InlineButton1 = types.InlineKeyboardButton(text='Да', callback_data='wp')
        InlineButton2 = types.InlineKeyboardButton(text='Нет', callback_data='gg')
        InlineButton3 = types.InlineKeyboardButton(text='Хз', callback_data='gl')
        markup.add(InlineButton1, InlineButton2, InlineButton3)

        return markup
    elif where_call == 'G':
        markup = types.InlineKeyboardMarkup(row_width=1)
        PiButton = types.InlineKeyboardButton(text='Хочу питсу', callback_data='pi')

        markup.add(PiButton)

        return markup


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Да', 'Нет')

    bot.send_message(message.chat.id, 'Можно задать тебе вопрос?', reply_markup=markup, parse_mode='html')


@bot.message_handler(commands=['test'])
def Test(message):
    bot.send_message(message.chat.id, 'Привет жрик\n'
                                      '{Text}', disable_web_page_preview=True, parse_mode='html')


@bot.message_handler(content_types=['text'])
def Knopka(message):
    if message.chat.type == 'private':
        if message.text == 'Да':
            bot.send_message(message.chat.id, "Дота говно ?", parse_mode='html', reply_markup=keyboard('H'))
        elif message.text == 'Нет':
            bot.send_message(message.chat.id, 'Ну и ладно', parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def Klace(call):
    try:
        if call.message:
            if call.data == 'wp':
                # bot.delete_message(call.message.chat.id, call.message.message_id)
                # bot.send_photo(call.message.chat.id, Photo, 'Какойто текст', reply_markup=keyboard('Gag'))
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(call.message.chat.id, 'Здравый человек!', parse_mode='html')
            elif call.data == 'gg':
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(call.message.chat.id, 'Ясно, позер...', parse_mode='html')
            elif call.data == 'gl':
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(call.message.chat.id, 'Ясно, лох без мнения', parse_mode='html', reply_markup=keyboard('G'))
            elif call.data == 'pi':
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_message(call.message.chat.id, 'О, добро', parse_mode='html')
    except Exception as e:
        print(repr(e))


#Misha lox
# RUN
bot.polling(none_stop=True)
