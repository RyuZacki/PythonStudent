import telebot
from telebot import apihelper

bot = telebot.TeleBot("1134893210:AAGYgSgPus38BIwriMRPjY6iXMfIFwTlazA")

proxy_ip = 'orbtl.s5.opennetwork.cc'
proxy_port = '999'
proxy_user = '505188988'
proxy_pass = '0ZqTerSY'

apihelper.proxy = {
  'https': 'socks5://{}:{}@{}:{}'.format(proxy_user, proxy_pass, proxy_ip, proxy_port)
}


@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
