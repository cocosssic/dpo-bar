import telebot
import markups as nav

TOKEN = '5141314522:AAFeMxB81EAKacxB-VjUyhV8KIoYIQi_Zqg'

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def start (message):
    bot.send_message(message.chat.id, 'приввет, {0.first_name}'.format(message.from_user), reply_markup = nav.markupMainMenu)

@bot.message_handler(content_types=['text'])
def OsnovnoeMenu(message):
    if message.chat.type == 'private':
        #меню
        if message.text == 'меню':
            bot.send_message(message.chat.id, 'https://vk.com/album-195566061_28384458')
        #мероприятия
        elif message.text == 'наши мероприятия':
            bot.send_message(message.chat.id, 'https://vk.com/album-195566061_275938054')
        #вызвать официанта
        elif message.text == 'вызвать официанта':
            bot.send_message(message.chat.id, 'выберете столик', reply_markup = nav.markupTableNumber)
        elif message.text == 'Путь к нам':
            bot.send_message(message.chat.id,'Наш адрес: \nПолитехническая 6')
            bot.send_location(message.chat.id,latitude= 59.99323, longitude = 30.35611)
        elif message.text == 'Программа лояльности':
            bot.send_message(message.chat.id,'Условия программы лояльности',reply_markup = nav.markupLoyalnost,)
        if message.text == 'стол номер 1':
            bot.send_message(chat_id=-1001796534245, text=message.text)
            bot.send_message(message.chat.id, 'официант скоро подойдет')
        elif message.text == '2':
            bot.send_message(chat_id=-1001796534245, text=message.text)
            bot.send_message(message.chat.id, 'официант скоро подойдет')
        elif message.text == '3':
            bot.send_message(chat_id=-1001796534245, text=message.text)
            bot.send_message(message.chat.id, 'официант скоро подойдет')
        elif message.text == '4':
            bot.send_message(chat_id=-1001796534245, text=message.text)
            bot.send_message(message.chat.id, 'официант скоро подойдет')
        elif message.text == '5':
            bot.send_message(chat_id=-1001796534245, text=message.text + 'счет')
            bot.send_message(message.chat.id, 'официант скоро подойдет')
        elif message.text == 'Отмена':
            bot.send_message(message.chat.id,'Вызов персонала отменен',reply_markup = nav.markupMainMenu)
        elif message.text == 'оставить отзыв':
            bot.send_message(message.chat.id, 'напишите сюда свой отзыв',reply_markup=nav.markupOtmena)
            bot.send_message(chat_id=-1001796534245, text=message.text)
        elif message.text == 'Назад':
            bot.send_message(message.chat.id,'Главное меню',reply_markup = nav.markupMainMenu)
        elif message.text == 'Путь к нам':
            bot.send_message(message.chat.id,'Наш адрес: \nПолитехническая 6')
            bot.send_location(message.chat.id,latitude= 59.99323, longitude = 30.35611)
        elif message.text == 'Программа лояльности':
            bot.send_message(message.chat.id,'Условия программы лояльности',reply_markup = nav.markupLoyalnost,)
        elif message.text == 'Скидочная карта':
            bot.send_message(message.chat.id,'что то написать надо')


def text(message):
    if message.text == 'Программа лояльности':
        bot.send_message(message.chat.id,'Условия программы лояльности',reply_markup = nav.markupLoyalnost,)
    elif message.text == 'Скидочная карта':
        bot.send_message(message.chat.id,'что то написать надо')
    elif message.text == '':
        bot.send_message(chat_id=-1001796534245, text=message.text)
    

bot.polling(none_stop = True)