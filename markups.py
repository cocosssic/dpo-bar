from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


#main menu
btnMenu = KeyboardButton('меню')
btnIvent= KeyboardButton('наши мероприятия')
btnDelivery = KeyboardButton('доставка')
btnCalloficiant = KeyboardButton('вызвать официанта')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMenu, btnDelivery, btnCalloficiant, btnIvent)


#call oficiant table number
btnTablenumber1 = KeyboardButton('1')
btnTablenumber2 = KeyboardButton('2')
btnTablenumber3 = KeyboardButton('3')
btnTablenumber4 = KeyboardButton('4')
btnTablenumber5 = KeyboardButton('5')
btnTablenumber6 = KeyboardButton('6')
btnBack = KeyboardButton('назад в главное меню')
tableMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnTablenumber1,btnTablenumber2,btnTablenumber3,btnTablenumber4,btnTablenumber5,btnTablenumber6,btnBack)
