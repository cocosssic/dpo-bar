import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav

TOKEN = '5141314522:AAFeMxB81EAKacxB-VjUyhV8KIoYIQi_Zqg'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет {0.first_name}'.format(message.from_user), reply_markup = nav.mainMenu)


@dp.message_handler()
async def command_start(message: types.Message):
    if message.text == 'меню':
        await bot.send_message(message.from_user.id, 'https://vk.com/album-195566061_28384458')
    elif message.text == 'вызвать официанта':
        await bot.send_message(message.from_user.id, 'Выберите номер столика', reply_markup=nav.tableMenu)


@dp.message_handler()
async def command_start(message: types.Message):
    if message.text == 'вызвать официанта':
        await bot.send_message(message.from_user.id, 'Выберите номер столика', reply_markup=nav.tableMenu)



if __name__  == '__main__':
    executor.start_polling(dp, skip_updates=True)