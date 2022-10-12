import telebot
from settings import API_NUM

bot = telebot.TeleBot(API_NUM)


@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи, пиши)')


@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)


bot.polling(none_stop=True, interval=0)