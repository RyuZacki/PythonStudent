import telebot
import ConfigBotTest

from telebot import types

bot = telebot.TeleBot(ConfigBotTest.TOKEN)


def keyboard(where_call):
    markup = types.InlineKeyboardMarkup()
    if where_call == 'Tet':
        InlineButton = types.InlineKeyboardButton(text='Тыкай', callback_data='TT')
        markup.add(InlineButton)

        return markup
    elif where_call == 'Gag':
        # markup = types.InlineKeyboardMarkup(row_width=5)
        markup = types.InlineKeyboardMarkup()

        Value1 = types.InlineKeyboardButton("1", callback_data='One2')
        Value2 = types.InlineKeyboardButton("2", callback_data='Two2')
        Value3 = types.InlineKeyboardButton("3", callback_data='Three2')
        Value4 = types.InlineKeyboardButton("4", callback_data='Four2')
        Value5 = types.InlineKeyboardButton("5", callback_data='Five2')
        Value6 = types.InlineKeyboardButton("6", callback_data='Six2')
        Value7 = types.InlineKeyboardButton("7", callback_data='Seven2')
        Value8 = types.InlineKeyboardButton("8", callback_data='Eight2')
        Value9 = types.InlineKeyboardButton("9", callback_data='Nine2')
        Value10 = types.InlineKeyboardButton("10", callback_data='Ten2')

        Back = types.InlineKeyboardButton("Назад", callback_data='Back2')
        BackCategories = types.InlineKeyboardButton("Назад ко всем категориям", callback_data='BackCategories1')

        markup.row(Value1, Value2, Value3, Value4, Value5)
        markup.row(Value6, Value7, Value8, Value9, Value10)
        markup.row(Back)
        markup.row(BackCategories)

        return markup
    elif where_call == 'Jej':
        InlineButon3 = types.InlineKeyboardButton(text='Ну и еще раз на последок', callback_data='JJ')
        InlineButtonBack3 = types.InlineKeyboardButton(text='Назад', callback_data='Back2')
        markup.add(InlineButon3, InlineButtonBack3)

        return markup


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Ну шо, тыкай!')

    bot.send_message(message.chat.id, 'Если сработает, то я гений', reply_markup=markup)
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton("Тестовая кнопка")
    #
    # markup.add(item1)
    # bot.send_message(message.chat.id, "Тестовое сообщение", parse_mode='html', reply_markup=keyboard('Tet'))


@bot.message_handler(commands=['test'])
def Test(message):
    text = '[ ](https://i.mycdn.me/i?r=AzEPZsRbOZEKgBhR0XGMT1Rkq1f4QBh50MhGLzBu0WvqHKaKTM5SRkZCeTgDn6uOyic&fn=sqr_288)'
    bot.send_message(message.chat.id, 'Привет жрик\n'
                                      '{Text}'.format(Text=text), disable_web_page_preview=True, parse_mode='Markdown')


@bot.message_handler(content_types=['text'])
def Knopka(message):
    if message.chat.type == 'private':
        if message.text == 'Ну шо, тыкай!':
            # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            # item1 = types.KeyboardButton("Тестовая кнопка")
            #
            # markup.add(item1)
            bot.send_message(message.chat.id, "Тестовое сообщение", parse_mode='html', reply_markup=keyboard('Tet'))
        else:
            bot.send_message(message.chat.id, "Не туда тыкнул", parse_mode='html')


@bot.callback_query_handler(func=lambda call: True)
def Klace(call):
    try:
        if call.message:
            if call.data == 'TT':
                Photo = open('photo_2021-05-28_13-52-15.jpg', 'rb')
                bot.delete_message(call.message.chat.id, call.message.message_id)
                bot.send_photo(call.message.chat.id, Photo, 'Какойто текст', reply_markup=keyboard('Gag'))
            elif call.data == 'GG':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Гигрягут', reply_markup=keyboard('Jej'))
            elif call.data == 'JJ':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Ураааааааа!!!!!!!')
            elif call.data == 'Back1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Тестовое сообщение", reply_markup=keyboard('Tet'))
            elif call.data == 'Back2':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text='Гигрягут', reply_markup=keyboard('Gag'))
    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)