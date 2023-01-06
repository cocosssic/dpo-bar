import telebot
from telebot import types

TOKEN = '5141314522:AAFeMxB81EAKacxB-VjUyhV8KIoYIQi_Zqg'

bot = telebot.TeleBot(TOKEN)


markupOtmena = types.ReplyKeyboardMarkup(resize_keyboard=True)
btnOtmena = types.KeyboardButton('Отмена')

markupOtmena.add(btnOtmena)


markupTableNumber = types.ReplyKeyboardMarkup(resize_keyboard=True)
btnTablenumber1 = types.KeyboardButton('стол номер 1')
btnTablenumber2 = types.KeyboardButton('2')
btnTablenumber3 = types.KeyboardButton('3')
btnTablenumber4 = types.KeyboardButton('4')
btnTablenumber5 = types.KeyboardButton('5')
btnTablenumber6 = types.KeyboardButton('6')
btnBack = types.KeyboardButton('Отмена')

markupTableNumber.add(btnTablenumber1,btnTablenumber2,btnTablenumber3,btnTablenumber4,btnTablenumber5,btnTablenumber6,btnBack)

markupMainMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('меню')
item2 = types.KeyboardButton('наши мероприятия')
item3 = types.KeyboardButton('оставить отзыв')
item4 = types.KeyboardButton('доставка')
item5 = types.KeyboardButton('вызвать официанта')

markupMainMenu.add(item1, item2, item3, item4, item5)

@bot.message_handler(commands=['start'])
def start (message):
    bot.send_message(message.chat.id, 'приввет, {0.first_name}'.format(message.from_user), reply_markup = markupMainMenu)

@bot.message_handler(content_types=['text'])
def message(message):
    if message.chat.type == 'private':
        #меню
        if message.text == 'меню':
            bot.send_message(message.chat.id, 'https://vk.com/album-195566061_28384458')
        #мероприятия
        elif message.text == 'наши мероприятия':
            bot.send_message(message.chat.id, 'https://vk.com/album-195566061_275938054')
        #вызвать официанта
        elif message.text == 'вызвать официанта':
            bot.send_message(message.chat.id, 'выберете столик', reply_markup = markupTableNumber)
        elif message.text == 'стол номер 1':
            bot.send_message(chat_id=-1001796534245, text=message.text)
            bot.send_message(message.chat.id, 'официант скоро подойдет')
        elif message.text == '2':
            bot.send_message(chat_id=-1001796534245, text='стол номер 2')
            bot.send_message(message.chat.id, 'офик скоро подойдет')
        elif message.text == 'Отмена':
            bot.send_message(message.chat.id,'Вызов персонала отменен',reply_markup =markupMainMenu)
        elif message.text == 'оставить отзыв':
            bot.send_message(message.chat.id, 'напишите сюда свой отзыв',reply_markup=markupOtmena)
            bot.send_message(chat_id=-1001796534245, text=message.text)



bot.polling(none_stop = True)