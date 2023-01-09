from telebot import types

#меню каарты лояльности
markupLoyalnost= types.ReplyKeyboardMarkup(resize_keyboard=True)
btnSaleCard = types.KeyboardButton('Скидочная карта')
btnNazad = types.KeyboardButton('Назад')

markupLoyalnost.add(btnSaleCard,btnNazad)

#кнопка отмены (назад)
markupOtmena = types.ReplyKeyboardMarkup(resize_keyboard=True)
btnOtmena = types.KeyboardButton('Назад')

markupOtmena.add(btnOtmena)

#выбор столика для клиента(номера столов)
markupTableNumber = types.ReplyKeyboardMarkup(resize_keyboard=True)
btnTablenumber1 = types.KeyboardButton('стол номер 1')
btnTablenumber2 = types.KeyboardButton('2')
btnTablenumber3 = types.KeyboardButton('3')
btnTablenumber4 = types.KeyboardButton('4')
btnTablenumber5 = types.KeyboardButton('5')
btnTablenumber6 = types.KeyboardButton('6')
btnBack = types.KeyboardButton('Отмена')

markupTableNumber.add(btnTablenumber1,btnTablenumber2,btnTablenumber3,btnTablenumber4,btnTablenumber5,btnTablenumber6,btnBack)

#главное меню (начальное меню)
markupMainMenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton('меню')
item2 = types.KeyboardButton('наши мероприятия')
item3 = types.KeyboardButton('оставить отзыв')
item4 = types.KeyboardButton('доставка')
item5 = types.KeyboardButton('вызвать официанта')
item6 = types.KeyboardButton('Программа лояльности')
item7 = types.KeyboardButton('Путь к нам')

markupMainMenu.add(item1, item2, item3, item4, item5, item6, item7)