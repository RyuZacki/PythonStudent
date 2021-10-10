import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_game(chat_id=message.chat.id, game_short_name='ValakasG')


@bot.callback_query_handler(func=lambda callback_query: callback_query.game_short_name == 'ValakasG')
def game(call):
    bot.answer_callback_query(callback_query_id=call.id, url='')


# RUN
if __name__ == '__main__':
    bot.polling()
