import telebot
from telebot import types
from settings import Token, adm_chat

TOKEN = Token

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start (message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('меню')
    item2 = types.KeyboardButton('наши мероприятия')
    item3 = types.KeyboardButton('оставить отзыв')
    item4 = types.KeyboardButton('доставка')
    item5 = types.KeyboardButton('вызвать официанта')

    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, 'приввет, {0.first_name}'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def message(message):
    if message.chat.type == 'private':
        if message.text == 'меню':
            bot.send_message(message.chat.id, 'https://vk.com/album-195566061_28384458')
        elif message.text == 'наши мероприятия':
            bot.send_message(message.chat.id, 'https://vk.com/album-195566061_275938054')
        #позвать официанта/
        elif message.text == 'вызвать официанта':
           bot.send_message(chat_id=adm_chat, text='новый заказ блять')
           bot.send_message(message.chat.id, 'офик скоро подойдет')
        elif message.text == 'связаться с руководителем':
            bot.send_message(message.chat.id, 'а почему блять тут не рабоатет??????')
           
'''
@bot.message_handler(func=lambda message: True)
def calldirector(message):
    if message.chat.type == 'private':
        if message.text == 'связаться с руководителем':
            bot.send_message(message.chat.id, 'а почему блять тут не рабоатет??????')'''


bot.polling(none_stop = True)
